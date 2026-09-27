#!/usr/bin/env python3
"""
generate_cv.py  —  YAML _data/ → CV.tex Auto-Generation
Usage:
    python generate_cv.py
    python generate_cv.py --short   # Show recent N items only
"""

import yaml, re, argparse
from pathlib import Path

DATA_DIR = Path("../_data")
OUTPUT   = Path("Hong_CV_latest.tex")

# ── Helpers ─────────────────────────────────────────────────────

def load(name):
    with open(DATA_DIR / f"{name}.yml", encoding="utf-8") as f:
        return yaml.safe_load(f)

def tex_escape(s):
    if not isinstance(s, str):
        return str(s)
    replacements = {
        "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%",
        "#": r"\#", "$": r"\$", "_": r"\_",
        "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
        "{": r"\{", "}": r"\}",
    }
    return ''.join(replacements.get(char, char) for char in s)

def format_authors(authors):
    if not authors:
        return ""
    s = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', str(authors))
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

def is_cv_enabled(item):
    """Safely check if the item is enabled for CV using string parsing."""
    val = item.get('cv')
    if val is None:
        return True
    return str(val).strip().upper() != 'FALSE'

# ── Sections ─────────────────────────────────────────────────────

def sec_papers(data, short=False):
    lines = []
    lines.append(r"\section{\sc Papers}")
    lines.append(r"$\dagger$: (co-)1st author, ${}^*$: (co-)corresponding author. \\")
    lines.append(r"Note: Where no author is designated as the first author ($\dagger$), "
                 r"names are listed in alphabetical order by last name, as is standard practice in mathematical journals.")
    lines.append("")

    # Filter enabled preprints and published papers
    preprints = [p for p in data['papers']['preprints'] if is_cv_enabled(p)]
    published = [p for p in data['papers']['published'] if is_cv_enabled(p)]
    if short:
        published = published[:5]

    # Calculate the unified total count for sequential reverse numbering across both sections
    total_papers_count = len(preprints) + len(published)

    # 1. Preprints (Top section - starts with the absolute highest number)
    lines.append(r"\vspace{-5pt}")
    lines.append(r"In preparation or preprint: \vspace{7pt}")
    lines.append(r"\begin{itemize}[leftmargin=*]")
    
    current_num = total_papers_count  # Start with the maximum total number
    for p in preprints:
        authors = format_authors(p['authors'])
        ptype   = str(p.get('type', 'prep')).strip()
        status  = {'prep': r'\textit{in preparation}',
                   'submitted': r'\textit{Submitted}',
                   'review': r'\textit{Under review}'}.get(ptype, r'\textit{in preparation}')
        links   = format_links(p)
        
        entry   = f"    \\item[{current_num}.] {authors}, {p['title']}, {status}"
        if links:
            entry += f"; {links}"
        lines.append(entry)
        lines.append("")
        current_num -= 1  # Decrement the global paper number
        
    lines.append(r"\end{itemize}")
    lines.append("")

    # 2. Published (Bottom section - continues counting down to 1)
    lines.append(r"\vspace{-5pt}")
    lines.append(r"Published or accepted: \vspace{7pt}")
    lines.append(r"\begin{itemize}[leftmargin=*]")
    
    for p in published:
        links = format_links(p)
        escaped_year = tex_escape(p.get('year', ''))
        
        entry = f"    \\item[{current_num}.] {format_authors(p['authors'])}, {p['title']}, \\textit{{{p['venue']}}}, {escaped_year}"
        if links:
            entry += f"; {links}"
        lines.append(entry)
        lines.append("")
        current_num -= 1  # Decrement the global paper number
        
    lines.append(r"\end{itemize}")

    # 3. Book Chapters (Kept independent from regular journal/preprint numbering)
    if data['papers'].get('book_chapters'):
        book_chapters = [p for p in data['papers']['book_chapters'] if is_cv_enabled(p)]
        book_count = len(book_chapters)
        
        lines.append(r"\vspacesection")
        lines.append(r"\section{\sc Book Chapters}")
        lines.append(r"\begin{itemize}[leftmargin=*]")
        for i, p in enumerate(book_chapters):
            current_book_num = book_count - i
            links = format_links(p)
            entry = f"    \\item[{current_book_num}.] {format_authors(p['authors'])}, {p['title']}, {p['venue']}"
            if links:
                entry += f"; {links}"
            lines.append(entry)
        lines.append(r"\end{itemize}")

    return '\n'.join(lines)


def sec_talks(data, short=False):
    lines = []
    lines.append(r"\vspacesection")
    lines.append(r"\section{\sc Invited talks}")
    invited = [t for t in data['talks']['invited'] if is_cv_enabled(t)]
    if short:
        invited = invited[:10]

    lines.append(r"\begin{itemize}[leftmargin=0pt, label={}]")
    for t in invited:
        date        = tex_escape(t['date'])
        event       = tex_escape(t['event'])
        location    = tex_escape(t.get('location', ''))
        title       = t.get('title', '')
        url         = t.get('url', '')
        extra_url   = t.get('extra_url', '')
        extra_label = t.get('extra_label', '')
        slides_url  = t.get('slides_url', '')

        loc_part   = f", {location}" if location else ""
        event_part = f"\\href{{{url}}}{{\\textbf{{{event}}}}}" if url else f"\\textbf{{{event}}}"
        
        # Main item line: Date, Location, Event (No slide link here)
        item_line  = f"    \\item {date}{loc_part}, {event_part}"
        
        if title:
            title_line = tex_escape(title)
            
            # 💡 Append [slides] right next to the talk title if slides_url exists
            if slides_url:
                title_line += f" [\\href{{{slides_url}}}{{\\ul{{slides}}}}]"
                
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
        lines.append(f"    \\item {tex_escape(c['term'])}: [{tex_escape(c['role'])}] {tex_escape(c['course'])}")
    lines.append(r"\end{itemize}")
    lines.append(r"\vspacesection")
    lines.append("")
    lines.append(r"\textbf{KAIST}")
    lines.append(r"\begin{itemize}")
    for c in kaist:
        lines.append(f"    \\item {tex_escape(c['term'])}: [{tex_escape(c['role'])}] {tex_escape(c['course'])}")
    lines.append(r"\end{itemize}")

    lines.append("")
    lines.append(r"\section{\sc Mentoring}")
    uw_m    = [m for m in data['teaching']['mentoring'] if m['institution'] == 'UW\u2013Madison']
    kaist_m = [m for m in data['teaching']['mentoring'] if m['institution'] == 'KAIST']

    if uw_m:
        lines.append(r"\textbf{UW--Madison}")
        lines.append(r"\begin{itemize}")
        for m in uw_m:
            lines.append(f"    \\item {tex_escape(m['period'])}: {tex_escape(m['name'])}, {tex_escape(m['description'])}\\\\")
            if m.get('note'):
                lines.append(f"    {m['note']}")
        lines.append(r"\end{itemize}")
        lines.append(r"\vspacesection")

    if kaist_m:
        lines.append(r"\textbf{KAIST}")
        lines.append(r"\begin{itemize}")
        for m in kaist_m:
            lines.append(f"    \\item {tex_escape(m['period'])}: {tex_escape(m['name'])}, {tex_escape(m['description'])}\\\\")
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
        if not is_cv_enabled(a):
            continue
        year  = tex_escape(a.get('year', ''))
        title = tex_escape(a.get('title', ''))
        org   = tex_escape(a.get('org', ''))
        lines.append(f"    \\item {year} {title}, {org}")
    lines.append(r"\end{itemize}")
    return '\n'.join(lines)


def sec_grants(data):
    lines = []
    lines.append(r"\section{\sc Research Grants}")
    for g in data['grants']:
        period = tex_escape(g.get('period', ''))
        funder = tex_escape(g.get('funder', ''))
        g_num  = tex_escape(g.get('grant_number', ''))
        role   = tex_escape(g.get('role', ''))
        amount = tex_escape(g.get('amount', ''))
        title  = tex_escape(g.get('title', ''))
        
        lines.append(f"{period} {funder}, {g_num}, \\textbf{{{role}}} ({amount})\\\\")
        lines.append(f"Title: \\textit{{{title}}}")
        lines.append("")
    return '\n'.join(lines)


def sec_service(data):
    lines = []
    lines.append(r"\vspacesection")
    lines.append(r"\section{\sc Academic \\ Service}")
    for s in data['service']['service']:
        lines.append(f"\\textbf{{{tex_escape(s['date'])}: {tex_escape(s['title'])}}} \\\\")
        if s.get('note'):
            lines.append(s['note'])
        lines.append(r"\vspace{-5pt}")
        lines.append("")

    lines.append(r"\section{\sc Peer Review}")
    escaped_pr = [tex_escape(p) for p in data['service']['peer_review']]
    lines.append(', '.join(escaped_pr))
    lines.append(r"\vspace{-8pt}")
    lines.append("")

    lines.append(r"\section{\sc Outreach}")
    lines.append(r"\begin{itemize}[leftmargin=0pt, label={}]")
    for o in data['service']['outreach']:
        url         = o.get('url', '')
        event_title = tex_escape(o.get('title', ''))
        date        = o.get('date', '')
        venue       = tex_escape(o.get('venue', ''))
        talk_title  = o.get('talk_title', '')
        slides_url  = o.get('slides_url', '')

        # Use explicit string formatting to handle possible non-string dates safely
        formatted_date = tex_escape(str(date))
        title_str = f"\\href{{{url}}}{{\\textbf{{{formatted_date}: {event_title}}}}}" if url \
                    else f"\\textbf{{{formatted_date}: {event_title}}}"
        
        # Main item line (No slide link here)
        item_line = f"    \\item {title_str}, {venue}"
        
        if talk_title:
            talk_title_str = tex_escape(talk_title)
            
            # 💡 Append [slides] right next to the outreach talk title if slides_url exists
            if slides_url:
                talk_title_str += f" [\\href{{{slides_url}}}{{\\ul{{slides}}}}]"
                
            item_line += f" \\\\\n    \\textit{{{talk_title_str}}}"
            
        if o.get('note'):
            item_line += f" \\\\\n    {o['note']}"
        lines.append(item_line)
    lines.append(r"\end{itemize}")
    return '\n'.join(lines)


# ── Assemble CV ──────────────────────────────────────────────────

PREAMBLE = r"""\documentclass[margin,line]{res}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage{soul}
\usepackage{kotex}
\usepackage{multicol}
\usepackage{comment}
\usepackage{fancyhdr}
\usepackage{array}
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
\raggedright
"""

CONTACT = r"""
\section{\sc Contact Information}
\vspace{.05in}  
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.53\linewidth}>{\raggedright\arraybackslash}p{\dimexpr0.47\linewidth-2\tabcolsep\relax}@{}}
\href{https://www.kias.re.kr/kias/cp/centrsPgmsMng/people.do?centrspgmsCd=AI&menuNo=403021}{Center for AI and Natural Sciences (CAINS)} & {\it E-mail:} hhong78@kias.re.kr \\
\href{https://www.kias.re.kr/}{Korea Institute for Advanced Study (KIAS)} & {\it Web:} \url{https://hyukpyohong.github.io}\\
85 Hoegiro, Dongdaemun-gu & \\
Seoul 02455, South Korea & \\
\end{tabular}
\vspacesection
"""

# CONTACT = r"""
# \section{\sc Contact Information}
# \vspace{.05in}
# \begin{tabular}{@{}p{2.7in}p{4in}}
# \href{https://math.wisc.edu}{Department of Mathematics} & {\it E-mail:} hhong78@wisc.edu \\
# University of Wisconsin--Madison & {\it Web:} \url{https://hyukpyohong.github.io}\\
# 480 Lincoln Drive & \\
# Madison, WI 53706, USA & \\
# \end{tabular}
# \vspacesection
# """

APPOINTMENT = r"""
\section{\sc Appointments}
{\bf Korea Institute for Advanced Study}, Seoul, South Korea\\
\begin{list1}
\item[] AI Fellow (AI Assistant Professor), Center for AI and Natural Sciences \hfill Aug. 2026--Present
\end{list1}
{\bf Institute for Basic Science}, Daejeon, South Korea\\
\begin{list1}
\item[] Visiting Research Fellow, Biomedical Mathematics Group \hfill May 2026--Aug. 2026
\end{list1}
{\bf University of Wisconsin--Madison}, Madison, Wisconsin, USA\\
\begin{list1}
\item[] Van Vleck Assistant Professor, Department of Mathematics \hfill Aug. 2023--May 2026
\end{list1}
\vspacesection
"""

EDUCATION = r"""
\section{\sc Education}
{\bf KAIST}, Daejeon, South Korea\\
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
\textbf{Fields}: Scientific machine learning (SciML), Mathematical biology, ODEs, Stochastic processes, Bayesian statistics, Computational neuroscience

\vspace{-10pt}
\textbf{Topics}: Koopman operator theory, System identification, Steady states of ODEs, stationary distributions of CTMCs, 
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

    for key in ('awards', 'grants'):
        data[key] = [item for item in data[key] if is_cv_enabled(item)]
    for group, keys in {
        'teaching': ('courses', 'mentoring'),
        'service': ('service', 'outreach'),
    }.items():
        for key in keys:
            data[group][key] = [item for item in data[group][key] if is_cv_enabled(item)]

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
        manuscript = '\n'.join(sections)
        # Filtering may leave a section with no items; LaTeX rejects empty lists.
        manuscript = re.sub(r'\\begin\{itemize\}(?:\[[^\]]*\])?\s*\\end\{itemize\}', '', manuscript)
        f.write(manuscript)
    print(f"✅  Generated: {OUTPUT}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--short', action='store_true')
    args = parser.parse_args()
    build_cv(short=args.short)