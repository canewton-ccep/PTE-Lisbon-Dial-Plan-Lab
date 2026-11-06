"""Number lab-guide headings (0.1, 1.2.3, 2.2.2a, B.4 ...) and pin each heading's original link id.

Usage (from the repo root):
    python scripts/number_headings.py docs            # preview the numbering
    python scripts/number_headings.py docs --apply    # write it to the .md files

Safe to re-run after adding or moving headings: existing numbers are recalculated.
Edit PAGES below if pages are added, removed or reordered.
"""
import re, sys, unicodedata, os
APPLY = '--apply' in sys.argv
D = sys.argv[1]
# page -> (top label, number the H1?)
PAGES = [
 ('lab-learning-objectives.md', '0.1', True),
 ('lab-access-2-minutes.md', '0.2', True),
 ('lab-site-1-san-jose-20-30-minutes.md', '1', False),
 ('lab-site-2-new-york-1-hour-15-minutes.md', '2', False),
 ('lab-site-3-dallas-20-30-minutes.md', '3', False),
 ('lab-site-4-london-30-minutes.md', '4', False),
 ('lab-debug-calls-through-local-gateway.md', 'B', False),
]
UNNUMBERED_H1 = {'Finish Line!'}
def slug(v):
    v = unicodedata.normalize('NFKD', v).encode('ascii', 'ignore').decode()
    v = re.sub(r'[^\w\s-]', '', v).strip().lower()
    return re.sub(r'[-\s]+', '-', v)
for fn, top, num_h1 in PAGES:
    p = os.path.join(D, fn)
    lines = open(p, encoding='utf-8').read().split('\n')
    infence = False; seen = {}; h2 = h3 = h4 = 0; stop = False
    print(f'\n=== {fn}')
    for i, l in enumerate(lines):
        if re.match(r'^\s*(```|~~~)', l): infence = not infence; continue
        if infence: continue
        m = re.match(r'^(#{1,4}) (.+?)\s*$', l)
        if not m: continue
        lvl, text = len(m.group(1)), m.group(2)
        # re-run safe: strip a previous number and pinned id
        pinned = re.search(r'\s*\{#([\w-]+)\}$', text)
        if pinned: text = text[:pinned.start()]
        text = re.sub(r'^(?:0\.\d+|[1-9B])(?:\.\d+){0,2}[a-z]?\s+(?=\S)', '', text) if pinned else text
        # mkdocs default id (with duplicate suffixes)
        s = slug(text); n = seen.get(s, 0); seen[s] = n + 1
        hid = s if n == 0 else f'{s}_{n}'
        if pinned: hid = pinned.group(1)
        if lvl == 1:
            if text in UNNUMBERED_H1: stop = True; label = None
            else: label = top if num_h1 else None
            h2 = h3 = h4 = 0
        elif stop: label = None
        elif lvl == 2: h2 += 1; h3 = h4 = 0; label = f'{top}.{h2}'
        elif lvl == 3: h3 += 1; h4 = 0; label = f'{top}.{h2}.{h3}'
        else: h4 += 1; label = f'{top}.{h2}.{h3}{chr(96+h4)}'
        if label is None:
            print(f'{"  "*(lvl-1)}(unnumbered) {text}')
            if pinned: lines[i] = f'{m.group(1)} {text} {{#{hid}}}'
            continue
        new = f'{m.group(1)} {label} {text} {{#{hid}}}'
        print(f'{"  "*(lvl-1)}{label} {text}')
        lines[i] = new
    if APPLY: open(p, 'w', encoding='utf-8').write('\n'.join(lines))
