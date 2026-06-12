# -*- coding: utf-8 -*-
"""Reusable builder: clones index.html shell (head/nav/footer/scripts) and injects page MAIN."""
import re, sys

src = open("index.html", encoding="utf-8").read()
HEAD = src[:src.index('<header id="nav"')]
NAV = src[src.index('<header id="nav"'):src.index('</header>') + len('</header>')]
FOOTER = src[src.index('<!-- ===== FOOTER'):src.index('</footer>') + len('</footer>')]
SCRIPTS = src[src.index('<script>', src.index('</footer>')):]


def to_home(block):
    block = block.replace('href="#top"', 'href="index.html"')
    return re.sub(r'href="#([a-zA-Z0-9_-]+)"', r'href="index.html#\1"', block)


def build(out, title, meta, main, nav_active=None):
    head = re.sub(r'<title>.*?</title>', '<title>' + title + '</title>', HEAD, flags=re.S)
    head = re.sub(r'(<meta name="description" content=")[^"]*(")', r'\1' + meta + r'\2', head)
    nav = to_home(NAV)
    if nav_active:
        nav = nav.replace('href="index.html#%s" class="ulink">' % nav_active,
                          'href="index.html#%s" class="ulink text-brass-deep" aria-current="page">' % nav_active)
    footer = to_home(FOOTER)
    page = head + nav + "\n" + main + "\n" + footer + "\n" + SCRIPTS
    open(out, "w", encoding="utf-8").write(page)
    print(out, "written:", len(page), "bytes")
