# -*- coding: utf-8 -*-
"""Blog generator: content/blog/*.md -> blog.html (index) + blog-<slug>.html (articles).
Runs locally AND in CI (GitHub Action). Uses the shared shell from index.html via _build_page."""
import os, glob, re, html as _html
import markdown as md
import yaml
from _build_page import build

CONTENT = "content/blog"

def parse(path):
    raw = open(path, encoding="utf-8").read()
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', raw, re.S)
    if not m:
        return None
    meta = yaml.safe_load(m.group(1)) or {}
    body_md = m.group(2).strip()
    slug = os.path.splitext(os.path.basename(path))[0]
    meta['slug'] = slug
    meta['body_html'] = md.markdown(body_md, extensions=['extra', 'sane_lists'])
    return meta

def fmt_date(d):
    s = str(d)
    try:
        from datetime import datetime
        return datetime.strptime(s[:10], "%Y-%m-%d").strftime("%B %-d, %Y")
    except Exception:
        try:
            from datetime import datetime
            return datetime.strptime(s[:10], "%Y-%m-%d").strftime("%B %d, %Y").replace(" 0", " ")
        except Exception:
            return s

def esc(t):
    return _html.escape(str(t), quote=True)

posts = sorted(filter(None, (parse(p) for p in glob.glob(CONTENT + "/*.md"))),
               key=lambda x: str(x.get('date', '')), reverse=True)

# ---- article pages ----
for po in posts:
    title = esc(po.get('title', 'Untitled'))
    date_h = esc(fmt_date(po.get('date', '')))
    author = esc(po.get('author', 'Liberty Immigration Council'))
    excerpt = esc(po.get('excerpt', ''))
    main = f'''
<main id="top">
<section class="relative bg-paper overflow-hidden pt-[74px]">
  <div class="mx-auto max-w-[48rem] px-5 lg:px-10 pt-9 pb-10 lg:pt-10">
    <a href="blog.html" class="reveal nudge inline-flex items-center gap-2 text-[13px] font-600 text-inkt/60 hover:text-pine">
      <svg class="h-4 w-4 text-brass-deep rotate-180" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 12h14m-6-6 6 6-6 6"/></svg>
      All articles
    </a>
    <div class="reveal flex items-center gap-3 text-brass-deep mt-9"><span class="diamond"></span><span class="eyebrow">{date_h} &middot; {author}</span></div>
    <h1 class="reveal display text-[2rem] sm:text-[2.6rem] lg:text-[3rem] leading-[1.1] text-pine-900 mt-5">{title}</h1>
  </div>
</section>
<section class="bg-paper">
  <div class="mx-auto max-w-[48rem] px-5 lg:px-10 pb-24">
    <div class="reveal prose">{po['body_html']}</div>
  </div>
</section>
<section class="relative bg-pine-900 text-paper grain overflow-hidden">
  <div class="absolute -top-32 -right-28 h-[34rem] w-[34rem] rounded-full opacity-20 pointer-events-none" style="background:radial-gradient(circle,rgba(174,138,67,.55) 0%,transparent 62%)"></div>
  <div class="relative mx-auto max-w-[86rem] px-5 lg:px-10 py-14 lg:py-16 flex flex-col lg:flex-row lg:items-center lg:justify-between gap-8">
    <h2 class="reveal display text-[1.9rem] lg:text-[2.5rem] leading-[1.1] max-w-2xl">Have a question about<br>your situation?</h2>
    <div class="reveal flex flex-wrap gap-4" data-d="2">
      <a href="index.html#help" class="btn btn-brass inline-flex items-center gap-2 rounded-full px-7 py-4 font-600">Get help</a>
      <a href="blog.html" class="btn inline-flex items-center gap-2 rounded-full border border-paper/30 px-7 py-4 font-600 hover:bg-paper hover:text-pine-900">More articles</a>
    </div>
  </div>
</section>
</main>'''
    build(f"blog-{po['slug']}.html",
          title + " | Liberty Immigration Council",
          excerpt or (title + " — Liberty Immigration Council"),
          main, nav_active="blog")

# ---- index page ----
cards = ""
for i, po in enumerate(posts):
    cards += f'''
      <a href="blog-{esc(po['slug'])}.html" class="reveal lift block rounded-2xl bg-ivory border border-pine/10 p-7 lg:p-8" data-d="{(i%3)+1}">
        <div class="eyebrow text-brass-deep">{esc(fmt_date(po.get('date','')))}</div>
        <h2 class="display text-[1.4rem] lg:text-[1.55rem] text-pine-900 mt-3 leading-tight">{esc(po.get('title','Untitled'))}</h2>
        <p class="mt-3 text-[15px] leading-relaxed text-inkt/65">{esc(po.get('excerpt',''))}</p>
        <span class="nudge inline-flex items-center gap-2 mt-5 font-600 text-pine text-[14px]">Read article
          <svg class="h-4 w-4 text-brass-deep" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 12h14m-6-6 6 6-6 6"/></svg></span>
      </a>'''

empty = '<p class="reveal text-inkt/60">New articles are coming soon.</p>' if not posts else ''
index_main = f'''
<main id="top">
<section class="relative bg-paper overflow-hidden pt-[74px]">
  <div class="mx-auto max-w-[86rem] px-5 lg:px-10 pt-9 pb-14 lg:pt-10 lg:pb-16">
    <a href="index.html" class="reveal nudge inline-flex items-center gap-2 text-[13px] font-600 text-inkt/60 hover:text-pine">
      <svg class="h-4 w-4 text-brass-deep rotate-180" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 12h14m-6-6 6 6-6 6"/></svg>
      Back to home
    </a>
    <div class="mt-7 grid lg:grid-cols-12 gap-8 lg:gap-16 items-end">
      <div class="lg:col-span-7">
        <div class="reveal flex items-center gap-3 text-brass-deep"><span class="diamond"></span><span class="eyebrow">Resources &amp; updates</span></div>
        <h1 class="lines mt-6 display leading-[1.06] text-[2.3rem] sm:text-[3rem] lg:text-[3.5rem] text-pine-900">
          <span class="line"><span>Know Your Rights.</span></span>
          <span class="line"><span>Stay <em class="quote text-brass-deep font-500">informed.</em></span></span>
        </h1>
      </div>
      <div class="lg:col-span-5 lg:pb-2">
        <p class="reveal text-[17px] leading-relaxed text-inkt/75" data-d="1">
          Plain-language articles on immigration, your rights, and the resources available to you and your family.
        </p>
      </div>
    </div>
  </div>
</section>
<section class="bg-ivory border-y border-pine/10">
  <div class="mx-auto max-w-[86rem] px-5 lg:px-10 py-16 lg:py-20">
    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-7">{cards}{empty}
    </div>
  </div>
</section>
</main>'''
build("blog.html", "Blog &amp; Resources | Liberty Immigration Council",
      "Plain-language articles on immigration, your rights, and resources for families from Liberty Immigration Council.",
      index_main, nav_active="blog")

print("blog generated:", len(posts), "articles + index")
