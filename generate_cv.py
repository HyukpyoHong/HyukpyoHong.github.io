#!/usr/bin/env python3
"""
generate_cv.py  —  YAML _data/ → CV.tex 자동 생성
Usage:
    python generate_cv.py
    python generate_cv.py --short   # 논문/발표 최근 N개만
"""

import yaml, re, argparse
from pathlib import Path

DATA_DIR = Path("_data")
OUTPUT   = Path("assets/CV_latest.tex")

# ── 헬퍼 ─────────────────────────────────────────────────────

def load(name):
    with open(DATA_DIR / f"{name}.yml", encoding="utf-8") as f:
        return yaml.safe_load(f)

def tex_escape(s):
    if not isinstance(s, str):
        return str(s)
    for old, new in [
        ("\\", r"\textbackslash{}"),
        ("&",  r"\&"),
        ("%",  r"\%"),
        ("#",  r"\#"),
        ("$",  r"\$"),
        ("_",  r"\_"),
        ("~",  r"\textasciitilde{}"),
        ("^",  r"\textasciicircum{}"),
        ("{",  r"\{"),
        ("}",  r"\}"),
    ]:
        s = s.replace(old, new)
    return s

def format_authors(authors):
    s = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', authors)
    s = s.replace('†', r'$\dagger$')
    s = s.replace('[*]', r'${}^*$')
    s = s.replace('&', r'\&')
    return s

def format_links(paper):
    links = []
    for key, label in [
        ('url_arxiv',   'arXiv'),
        ('url_biorxiv', 'bioRxiv'),
        ('url_medrxiv', 'medRxiv'),
        ('url_journal', 'journal'),
        ('url_book',    'link'),
    ]:
        if paper.get(key):
            links.append(rf'[\href{{{paper[key]}}}{{\ul{{{label}}}}}]')
    return '; '.join(links)

# ── 섹션 ─────────────────────────────────────────────────────

def sec_papers(data, short=False):
    lines = []
    lines.append(r"\section{\sc Papers}")
    lines.append(r"$\dagger$: (co-)1st author, ${}^*$: (co-)corresponding author. \\")
    lines.append(r"Note: Where no author is designated as the first author ($\dagger$), "
                 r"names are listed in alphabetical order by last name, as is standard practice in mathematical journals.")
    lines.append("")

    preprints = [p for p in data['papers']['preprints'] if p.get('cv', True)]
    lines.append(r"\vspace{-5pt}")
    lines.append(r"In preparation or preprint: \vspace{7pt}")
    lines.append(r"\begin{enumerate}[leftmargin=*]")
    for p in preprints:
        authors = format_authors(p['authors'])
        ptype   = p.get('type', 'prep')
        status  = {'prep': r'\textit{in preparation}',
                   'submitted': r'\textit{Submitted}',
                   'review': r'\textit{Under review}'}.get(ptype, r'\textit{in preparation}')
        links   = format_links(p)
        entry   = f"    \\item {authors}, {p['title']}, {status}"
        if links:
            entry += f"; {links}"
        lines.append(entry)
        lines.append("")
    lines.append(r"\end{enumerate}")
    lines.append("")

    published = [p for p in data['papers']['published'] if p.get('cv', True)]
    if short:
        published = published[:5]
    lines.append(r"\vspace{-5pt}")
    lines.append(r"Published or accepted: \vspace{7pt}")
    lines.append(r"\begin{enumerate}[leftmargin=*]")
    for p in published:
        links = format_links(p)
        entry = f"    \\item {format_authors(p['authors'])}, {p['title']}, \\textit{{{p['venue']}}}, {p['year']}"
        if links:
            entry += f"; {links}"
        lines.append(entry)
        lines.append("")
    lines.append(r"\end{enumerate}")

    if data['papers'].get('book_chapters'):
        lines.append(r"\vspacesection")
        lines.append(r"\section{\sc Book Chapters}")
        lines.append(r"\begin{enumerate}[leftmargin=*]")
        for p in data['papers']['book_chapters']:
            if not p.get('cv', True):
                continue
            links = format_links(p)
            entry = f"    \\item {format_authors(p['authors'])}, {p['title']}, {p['venue']}"
            if links:
                entry += f"; {links}"
            lines.append(entry)
        lines.append(r"\end{enumerate}")

    return '\n'.join(lines)


def sec_talks(data, short=False):
    lines = []

    lines.append(r"\vspacesection")
    lines.append(r"\section{\sc Invited talks}")
    invited = [t for t in data['talks']['invited'] if t.get('cv', True)]
    if short:
        invited = invited[:10]

    lines.append(r"\begin{itemize}[leftmargin=0pt, label={}]")
    for t in invited:
        date     = t['date']
        event    = tex_escape(t['event'])
        location = tex_escape(t.get('location', ''))
        title    = t.get('title', '')
        url      = t.get('url', '')
        extra_url   = t.get('extra_url', '')
        extra_label = t.get('extra_label', '')

        loc_part   = f", {location}" if location else ""
        event_part = f"\\href{{{url}}}{{{event}}}" if url else event
        item_line  = f"    \\item \\textbf{{{date}{loc_part}, {event_part}}}"
        if title:
            title_line = tex_escape(title)
            if extra_url:
                title_line += f" [\\href{{{extra_url}}}{{\\ul{{{extra_label}}}}}]"
            item_line += f" \\\\\n    \\textit{{{title_line}}}"
        lines.append(item_line)
    lines.append(r"\end{itemize}")

    return '\n'.join(lines)


def sec_teaching(data):
    lines = []
    lines.append(r"\vspacesection")
    lines.append(r"\section{\sc Teaching}")

    uw    = [c for c in data['teaching']['courses'] if c['institution'] == 'UW\u2013Madison']
    kaist = [c for c in data['teaching']['courses'] if c['institution'] == 'KAIST']

    lines.append(r"\textbf{UW--Madison}")
    lines.append(r"\begin{itemize}")
    for c in uw:
        lines.append(f"    \\item {c['term']}: [{c['role']}] {c['course']}")
    lines.append(r"\end{itemize}")
    lines.append(r"\vspacesection")
    lines.append("")
    lines.append(r"\textbf{KAIST}")
    lines.append(r"\begin{itemize}")
    for c in kaist:
        lines.append(f"    \\item {c['term']}: [{c['role']}] {c['course']}")
    lines.append(r"\end{itemize}")

    lines.append("")
    lines.append(r"\section{\sc Mentoring}")
    uw_m    = [m for m in data['teaching']['mentoring'] if m['institution'] == 'UW\u2013Madison']
    kaist_m = [m for m in data['teaching']['mentoring'] if m['institution'] == 'KAIST']

    if uw_m:
        lines.append(r"\textbf{UW--Madison}")
        lines.append(r"\begin{itemize}")
        for m in uw_m:
            lines.append(f"    \\item {m['period']}: {m['name']}, {m['description']}\\\\")
            if m.get('note'):
                lines.append(f"    {m['note']}")
        lines.append(r"\end{itemize}")
        lines.append(r"\vspacesection")

    if kaist_m:
        lines.append(r"\textbf{KAIST}")
        lines.append(r"\begin{itemize}")
        for m in kaist_m:
            lines.append(f"    \\item {m['period']}: {m['name']}, {m['description']}\\\\")
            if m.get('note'):
                lines.append(f"    {m['note']}")
        lines.append(r"\end{itemize}")

    return '\n'.join(lines)


def sec_awards(data):
    lines = []
    lines.append(r"\vspacesection")
    lines.append(r"\section{\sc Honors and Awards}")
    lines.append(r"\begin{itemize}[leftmargin=-1pt, label={}]")
    for a in data['awards']:
        if not a.get('cv', True):
            continue
        lines.append(f"    \\item {a['year']} {a['title']}, {a['org']}")
    lines.append(r"\end{itemize}")
    return '\n'.join(lines)


def sec_grants(data):
    lines = []
    lines.append(r"\section{\sc Research Grants}")
    for g in data['grants']:
        lines.append(f"{g['period']} {g['funder']}, {g['grant_number']}, "
                     f"\\textbf{{{g['role']}}} ({g['amount']})\\\\")
        lines.append(f"Title: \\textit{{{g['title']}}}")
        lines.append("")
    return '\n'.join(lines)


def sec_service(data):
    lines = []
    lines.append(r"\vspacesection")
    lines.append(r"\section{\sc Academic \\ Service}")
    for s in data['service']['service']:
        lines.append(f"\\textbf{{{s['date']}: {tex_escape(s['title'])}}} \\\\")
        if s.get('note'):
            lines.append(tex_escape(s['note']))
        lines.append(r"\vspace{-5pt}")
        lines.append("")

    lines.append(r"\section{\sc Peer Review}")
    lines.append(', '.join(data['service']['peer_review']))
    lines.append(r"\vspace{-8pt}")
    lines.append("")

    lines.append(r"\section{\sc Outreach}")
    lines.append(r"\begin{itemize}[leftmargin=0pt, label={}]")
    for o in data['service']['outreach']:
        url = o.get('url', '')
        event_title = tex_escape(o.get('title', ''))
        date = o.get('date', '')
        title_str = f"\\href{{{url}}}{{\\textbf{{{date}: {event_title}}}}}" if url \
                    else f"\\textbf{{{date}: {event_title}}}"
        venue = tex_escape(o.get('venue', ''))
        item_line = f"    \\item {title_str}, {venue}"
        if o.get('talk_title'):
            item_line += f" \\\\\n    \\textit{{{tex_escape(o['talk_title'])}}}"
        if o.get('note'):
            item_line += f" \\\\\n    {tex_escape(o['note'])}"
        lines.append(item_line)
    lines.append(r"\end{itemize}")
    return '\n'.join(lines)


# ── CV 조립 ──────────────────────────────────────────────────

PREAMBLE = r"""\documentclass[margin,line]{res}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage{soul}
\usepackage{kotex}
\usepackage{multicol}
\usepackage{comment}
\usepackage{fancyhdr}
\newcommand{\shorttoday}{%
  \ifcase\month
  \or Jan.\or Feb.\or Mar.\or Apr.\or May\or Jun.\or Jul.\or Aug.\or Sep.\or Oct.\or Nov.\or Dec.\fi
  \space\number\day, \number\year}

\hypersetup{
    colorlinks=false,
    linkcolor=blue,
    linkbordercolor=black,
    filecolor=magenta,
    urlcolor=blue,
    pdfborderstyle={/S/U/W 1}
}

\oddsidemargin -.5in
\evensidemargin -.5in
\textwidth=6.0in
\textheight=9.1in
\itemsep=0in
\parsep=0in
\setlength{\pdfpagewidth}{\paperwidth}
\setlength{\pdfpageheight}{\paperheight}

\newenvironment{list1}{
  \begin{list}{\ding{113}}{%
      \setlength{\itemsep}{0in}
      \setlength{\parsep}{0in} \setlength{\parskip}{0in}
      \setlength{\topsep}{0in} \setlength{\partopsep}{0in}
      \setlength{\leftmargin}{0.17in}}}{\end{list}}
\newenvironment{list2}{
  \begin{list}{$\bullet$}{%
      \setlength{\itemsep}{0in}
      \setlength{\parsep}{0in} \setlength{\parskip}{0in}
      \setlength{\topsep}{0in} \setlength{\partopsep}{0in}
      \setlength{\leftmargin}{0.2in}}}{\end{list}}

\newcommand{\vspaceaward}{\vspace*{-3.0mm}}
\newcommand{\vspacesection}{\vspace*{-1.5mm}}

\begin{document}
\name{Hyukpyo Hong \vspace*{.1in} \hspace{10.5cm} \small{Last updated: \shorttoday}}

\begin{resume}
"""

CONTACT = r"""
\section{\sc Contact Information}
\vspace{.05in}
\begin{tabular}{@{}p{2.7in}p{4in}}
\href{https://ibs.re.kr/bimag}{Biomedical Mathematics Group} & {\it E-mail:} hyukpyo.hong13@gmail.com \\
Institute for Basic Science (IBS) & {\it Web:} \url{https://hyukpyohong.github.io}\\
55 Expo-ro Yuseong-gu & \\
Daejeon 34126, South Korea & \\
\end{tabular}
\vspacesection
"""

APPOINTMENT = r"""
\section{\sc Appointments}
{\bf Institute for Basic Science (IBS)}, Daejeon, South Korea\\
\vspace*{-.1in}
\begin{list1}
\item[] Visiting Research Fellow, Biomedical Mathematics Group \hfill May 2026--present
\end{list1}
{\bf University of Wisconsin--Madison}, Madison, Wisconsin, USA\\
\vspace*{-.1in}
\begin{list1}
\item[] Van Vleck Assistant Professor, Department of Mathematics \hfill Aug. 2023--May 2026
\end{list1}
\vspacesection
"""

EDUCATION = r"""
\section{\sc Education}
{\bf KAIST}, Daejeon, South Korea\\
\vspace*{-.1in}
\begin{list1}
\item[] Ph.D.\ in Mathematical Sciences \hfill Feb.\ 2018--Aug.\ 2023 \\
Advisor: \href{https://mathsci.kaist.ac.kr/~jaekkim}{Jae Kyoung Kim} \\
Thesis: Development of stochastic model reduction framework for \\
\phantom{HHHHi} analysis and inference of biochemical reaction networks
\vspace*{.05in}
\item[] B.S.\ in Mathematical Sciences \hfill Mar.\ 2013--Feb.\ 2018
\end{list1}
\vspacesection
"""

RESEARCH_INTERESTS = r"""
\section{\sc Research Interests}
\textbf{Fields}: Mathematical biology, ODEs, Stochastic processes, Bayesian statistics, Digital medicine

\vspace{-10pt}
\textbf{Topics}: Steady states of ODEs, stationary distributions of CTMCs, Koopman operator theory,
MCMC methods, parameter estimation for non-Markovian stochastic models,
metabolic control analysis, homeostasis and adaptation in biological systems,
neurodegenerative disease-related alteration of human motor activity
\vspacesection
"""

POSTAMBLE = r"""
\vspace{-8pt}
\end{resume}
\end{document}
"""


def build_cv(short=False):
    data = {
        'papers':   load('papers'),
        'talks':    load('talks'),
        'teaching': load('teaching'),
        'awards':   load('awards'),
        'grants':   load('grants'),
        'service':  load('service'),
    }

    sections = [
        PREAMBLE,
        CONTACT,
        APPOINTMENT,
        EDUCATION,
        RESEARCH_INTERESTS,
        sec_papers(data, short=short),
        sec_grants(data),
        sec_awards(data),
        sec_teaching(data),
        sec_talks(data, short=short),
        sec_service(data),
        POSTAMBLE,
    ]

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sections))
    print(f"✅  Generated: {OUTPUT}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--short', action='store_true')
    args = parser.parse_args()
    build_cv(short=args.short)
