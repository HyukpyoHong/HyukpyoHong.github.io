#!/usr/bin/env python3
"""
sync_from_sheets.py
Syncs Google Sheets data to _data/*.yml files as pure strings.
Then generates the CV manuscript and compiles assets/Hong_CV_latest.pdf.

Usage:
    python sync_from_sheets.py          # Sync all tabs and rebuild the CV
    python sync_from_sheets.py papers   # Sync papers and rebuild the CV
"""

import csv, io, re, sys, yaml
import os
import shutil
import ssl
import subprocess
import tempfile
import urllib.request
from pathlib import Path

# ── Configuration ─────────────────────────────────────────────
SHEET_ID = "1-owqWQ7kyy6W56GgadgVBFrUaD3rg_8JvD6E-i6a9-c"
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "_data"
ASSETS_DIR = BASE_DIR / "assets"
DATA_DIR.mkdir(exist_ok=True)

# ── Helpers ───────────────────────────────────────────────────

def fetch_sheet(tab_name):
    """Download a Google Sheets tab as CSV and return list of dicts."""
    url = (f"https://docs.google.com/spreadsheets/d/{SHEET_ID}"
           f"/gviz/tq?tqx=out:csv&sheet={tab_name}")
    context = ssl.create_default_context()
    # Python.org installations may not have their own CA bundle configured.
    system_certs = Path('/etc/ssl/cert.pem')
    if sys.platform == 'darwin' and system_certs.is_file():
        context.load_verify_locations(cafile=str(system_certs))
    with urllib.request.urlopen(url, context=context, timeout=60) as r:
        content = r.read().decode('utf-8')
    reader = csv.DictReader(io.StringIO(content))
    return [row for row in reader]

def clean_date(val):
    """Unwrap y-delimited date string and keep it as a clean string."""
    if not val:
        return None
    val = str(val).strip()
    if val.startswith('y') and val.endswith('y'):
        return val[1:-1]
    return val if val else None

def clean(val):
    """Strip whitespace and return as string, or None if empty."""
    if val is None:
        return None
    v = str(val).strip()
    return v if v else None

def dump_yml(data, path):
    """Save data as YAML, forcing double quotes only for string values."""
    
    # Custom string class to distinguish values from keys
    class QuotedStr(str):
        pass

    # Presenter that forces double quotes only for QuotedStr
    def quoted_str_presenter(dumper, data):
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')

    # Register the presenter for QuotedStr only
    yaml.add_representer(QuotedStr, quoted_str_presenter)

    def prepare_data(obj):
        """Recursively process data to convert all values into QuotedStr."""
        if isinstance(obj, dict):
            # Keep keys as normal str, convert all values to QuotedStr
            return {str(k): prepare_data(v) for k, v in obj.items() if v is not None}
        if isinstance(obj, list):
            return [prepare_data(i) for i in obj]
        # Treat everything (numbers, dates, text) strictly as a quoted string value
        return QuotedStr(str(obj))

    cleaned_data = prepare_data(data)

    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(cleaned_data, f,
                  allow_unicode=True,
                  default_flow_style=False,
                  sort_keys=False)
    print(f"  ✅ {path}")

# ── Builders ──────────────────────────────────────────────────

def build_papers():
    rows = fetch_sheet('papers')
    preprints, published, book_chapters = [], [], []

    for r in rows:
        section = clean(r.get('section', ''))
        if not section:
            continue

        entry = {'cv': clean(r.get('cv'))}
        entry['title']   = clean(r.get('title'))
        entry['authors'] = clean(r.get('authors'))

        # All values including year are kept as clean strings
        if section == 'published':
            entry['year']  = clean(r.get('year'))
            entry['venue'] = clean(r.get('venue'))
        elif section == 'book_chapters':
            entry['venue'] = clean(r.get('venue'))

        if section == 'preprints':
            entry['type'] = clean(r.get('status')) or 'prep'

        for key in ['url_journal', 'url_arxiv', 'url_biorxiv', 'url_medrxiv', 'url_book']:
            v = clean(r.get(key))
            if v:
                entry[key] = v

        if section == 'preprints':
            preprints.append(entry)
        elif section == 'published':
            published.append(entry)
        elif section == 'book_chapters':
            book_chapters.append(entry)

    data = {'preprints': preprints, 'published': published, 'book_chapters': book_chapters}
    dump_yml(data, DATA_DIR / 'papers.yml')
    print(f"     preprints={len(preprints)}, published={len(published)}, book_chapters={len(book_chapters)}")


def build_talks():
    rows = fetch_sheet('talks')
    invited, contributed = [], []

    for r in rows:
        section = clean(r.get('section', ''))
        if not section:
            continue

        entry = {'cv': clean(r.get('cv'))}
        entry['date']     = clean_date(r.get('date'))
        entry['event']    = clean(r.get('event'))
        entry['location'] = clean(r.get('location'))
        entry['title']    = clean(r.get('title'))

        for key in ['url', 'extra_url', 'extra_label', 'slides_url']:
            v = clean(r.get(key))
            if v:
                entry[key] = v

        if section == 'contributed':
            entry['type'] = clean(r.get('type')) or 'contributed'
            contributed.append(entry)
        else:
            invited.append(entry)

    data = {'invited': invited, 'contributed': contributed}
    dump_yml(data, DATA_DIR / 'talks.yml')
    print(f"     invited={len(invited)}, contributed={len(contributed)}")


def build_teaching():
    courses_rows = fetch_sheet('teaching_courses')
    mentor_rows  = fetch_sheet('teaching_mentoring')

    courses = []
    for r in courses_rows:
        if not clean(r.get('term')):
            continue
        entry = {
            'term':        clean(r.get('term')),
            'role':        clean(r.get('role')),
            'course':      clean(r.get('course')),
            'institution': clean(r.get('institution')),
            'cv':          clean(r.get('cv')),
        }
        courses.append(entry)

    mentoring = []
    for r in mentor_rows:
        if not clean(r.get('name')):
            continue
        entry = {
            'period':      clean(r.get('period')),
            'name':        clean(r.get('name')),
            'description': clean(r.get('description')),
            'institution': clean(r.get('institution')),
            'cv':          clean(r.get('cv')),
            'note':        clean(r.get('note')),
            'note_web':    clean(r.get('note_web')),
        }
        mentoring.append(entry)

    data = {
        'award': '2025 Postdoctoral Excellence in Teaching Award, Department of Mathematics, UW\u2013Madison',
        'courses': courses,
        'mentoring': mentoring
    }
    dump_yml(data, DATA_DIR / 'teaching.yml')
    print(f"     courses={len(courses)}, mentoring={len(mentoring)}")


def build_awards():
    rows = fetch_sheet('awards')
    awards = []
    for r in rows:
        if not clean(r.get('title')):
            continue
        entry = {
            'year':  clean(r.get('year')),
            'title': clean(r.get('title')),
            'org':   clean(r.get('org')),
        }
        for key in ['amount', 'url', 'note', 'cv', 'web']:
            v = clean(r.get(key))
            if v:
                entry[key] = v
        awards.append(entry)

    dump_yml(awards, DATA_DIR / 'awards.yml')
    print(f"     awards={len(awards)}")


def build_grants():
    rows = fetch_sheet('grants')
    grants = []
    for r in rows:
        if not clean(r.get('title')):
            continue
        entry = {
            'period':       clean(r.get('period')),
            'title':        clean(r.get('title')),
            'funder':       clean(r.get('funder')),
            'grant_number': clean(r.get('grant_number')),
            'role':         clean(r.get('role')),
            'pi_type':      clean(r.get('pi_type')),
            'amount':       clean(r.get('amount')),
            'institution':  clean(r.get('institution')),
            'status':       clean(r.get('status')),
        }
        for key in ['num_pi', 'pi_names', 'collaborators', 'url', 'note', 'cv']:
            v = clean(r.get(key))
            if v:
                entry[key] = v
        grants.append(entry)

    dump_yml(grants, DATA_DIR / 'grants.yml')
    print(f"     grants={len(grants)}")


def build_service():
    svc_rows = fetch_sheet('service_academic')
    pr_rows  = fetch_sheet('service_peer_review')
    out_rows = fetch_sheet('service_outreach')

    service = []
    for r in svc_rows:
        if not clean(r.get('title')):
            continue
        entry = {'date': clean_date(r.get('date')), 'title': clean(r.get('title'))}
        for key in ['note', 'url', 'cv']:
            v = clean(r.get(key))
            if v:
                entry[key] = v
        service.append(entry)

    peer_review = [clean(r.get('journal')) for r in pr_rows if clean(r.get('journal'))]

    outreach = []
    for r in out_rows:
        if not clean(r.get('title')):
            continue
        entry = {
            'date':       clean_date(r.get('date')),
            'title':      clean(r.get('title')),
            'venue':      clean(r.get('venue')),
            'talk_title': clean(r.get('talk_title')),
        }
        for key in ['slides_url', 'url', 'note', 'cv']:
            v = clean(r.get(key))
            if v:
                entry[key] = v
        outreach.append(entry)

    data = {'service': service, 'peer_review': peer_review, 'outreach': outreach}
    dump_yml(data, DATA_DIR / 'service.yml')
    print(f"     service={len(service)}, peer_review={len(peer_review)}, outreach={len(outreach)}")


def build_news():
    rows = fetch_sheet('news')
    news = []
    for r in rows:
        if not clean(r.get('text')):
            continue
        # Check condition as a raw string filter
        web_val = clean(r.get('web'))
        if not web_val or web_val.upper() != 'TRUE':
            continue
        entry = {'date': clean_date(r.get('date')), 'text': clean(r.get('text'))}
        url = clean(r.get('url'))
        if url:
            entry['url'] = url
        news.append(entry)

    dump_yml(news, DATA_DIR / 'news.yml')
    print(f"     news={len(news)}")


def build_press():
    rows = fetch_sheet('press')
    press = []
    for r in rows:
        if not clean(r.get('title')):
            continue
        entry = {
            'date':                clean_date(r.get('date')),
            'title':               clean(r.get('title')),
            'outlet':              clean(r.get('outlet')),
            'outlet_country':      clean(r.get('outlet_country')),
            'url':                 clean(r.get('url')),
            'related_paper_id':    clean(r.get('related_paper_id')),
            'related_paper_title': clean(r.get('related_paper_title')),
            'language':            clean(r.get('language')),
        }
        note = clean(r.get('note'))
        if note:
            entry['note'] = note
        press.append(entry)

    dump_yml(press, DATA_DIR / 'press.yml')
    print(f"     press={len(press)}")


# ── Main ──────────────────────────────────────────────────────

def find_latexmk():
    """Find latexmk, including MacTeX when launched outside a terminal."""
    executable = shutil.which('latexmk')
    if executable:
        return executable
    mac_executable = Path('/Library/TeX/texbin/latexmk')
    if mac_executable.is_file():
        return str(mac_executable)
    raise RuntimeError('latexmk was not found. Install TeX with latexmk or add it to PATH.')


def rebuild_cv(latexmk, assets_dir=ASSETS_DIR):
    print('\n→ Generate CV manuscript', flush=True)
    subprocess.run(
        [sys.executable, str(assets_dir / 'generate_cv.py')],
        cwd=assets_dir, check=True,
    )
    print('\n→ Compile CV PDF', flush=True)
    tex_env = os.environ.copy()
    tex_env['PATH'] = str(Path(latexmk).parent) + os.pathsep + tex_env.get('PATH', '')
    subprocess.run(
        [latexmk, '-pdf', '-interaction=nonstopmode', '-halt-on-error',
         'Hong_CV_latest.tex'],
        cwd=assets_dir, check=True, env=tex_env,
    )
    pdf = assets_dir / 'Hong_CV_latest.pdf'
    if not pdf.is_file() or not pdf.read_bytes().startswith(b'%PDF-'):
        raise RuntimeError('CV compilation did not produce a valid PDF.')

BUILDERS = {
    'papers':   build_papers,
    'talks':    build_talks,
    'teaching': build_teaching,
    'awards':   build_awards,
    'grants':   build_grants,
    'service':  build_service,
    'news':     build_news,
    'press':    build_press,
}

def publish_files(pairs, backup_dir):
    """Replace completed outputs, restoring earlier files if a replacement fails."""
    backups = []
    for index, (_, destination) in enumerate(pairs):
        backup = backup_dir / str(index)
        if destination.exists():
            shutil.copy2(destination, backup)
            backups.append(backup)
        else:
            backups.append(None)
    replaced = []
    try:
        for (source, destination), backup in zip(pairs, backups):
            os.replace(source, destination)
            replaced.append((destination, backup))
    except BaseException:
        for destination, backup in reversed(replaced):
            if backup is None:
                destination.unlink(missing_ok=True)
            else:
                os.replace(backup, destination)
        raise


def update(targets, *, sync=True):
    """Build in isolation; publish only after sync and compilation both succeed."""
    global DATA_DIR
    unknown = [name for name in targets if name not in BUILDERS]
    if unknown:
        raise RuntimeError(f"Unknown target(s): {', '.join(unknown)}")
    latexmk = find_latexmk()
    original_data_dir = DATA_DIR
    with tempfile.TemporaryDirectory(prefix='.sync-', dir=BASE_DIR) as temp:
        stage = Path(temp)
        staged_data = stage / '_data'
        staged_assets = stage / 'assets'
        shutil.copytree(original_data_dir, staged_data)
        staged_assets.mkdir()
        for name in ('generate_cv.py', 'res.cls'):
            shutil.copy2(ASSETS_DIR / name, staged_assets / name)
        try:
            DATA_DIR = staged_data
            if sync:
                for name in targets:
                    print(f"\n→ {name}", flush=True)
                    BUILDERS[name]()
            rebuild_cv(latexmk, staged_assets)
        finally:
            DATA_DIR = original_data_dir
        pairs = [(staged_data / f'{name}.yml', DATA_DIR / f'{name}.yml')
                 for name in dict.fromkeys(targets)] if sync else []
        pairs.extend((staged_assets / name, ASSETS_DIR / name) for name in
                     ('Hong_CV_latest.tex', 'Hong_CV_latest.pdf'))
        backup_dir = stage / 'backups'
        backup_dir.mkdir()
        publish_files(pairs, backup_dir)
    print(f"\n✅ CV updated: {ASSETS_DIR / 'Hong_CV_latest.pdf'}", flush=True)


def main():
    targets = sys.argv[1:] if len(sys.argv) > 1 else list(BUILDERS.keys())
    update(targets)
    print("\nDone!", flush=True)


if __name__ == '__main__':
    try:
        main()
    except (OSError, RuntimeError, subprocess.CalledProcessError) as exc:
        print(f'\n❌ Update failed: {exc}', file=sys.stderr)
        sys.exit(1)
