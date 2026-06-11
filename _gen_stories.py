# -*- coding: utf-8 -*-
from _build_page import build

MAIN = r'''
<main id="top">
<!-- ===== HERO ===== -->
<section class="relative bg-paper overflow-hidden pt-[74px]">
  <div class="mx-auto max-w-[86rem] px-5 lg:px-10 py-20 lg:py-28">
    <a href="index.html" class="reveal nudge inline-flex items-center gap-2 text-[13px] font-600 text-inkt/60 hover:text-pine">
      <svg class="h-4 w-4 text-brass-deep rotate-180" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 12h14m-6-6 6 6-6 6"/></svg>
      Back to home
    </a>
    <div class="mt-9 grid lg:grid-cols-12 gap-10 lg:gap-16 items-end">
      <div class="lg:col-span-7">
        <div class="reveal flex items-center gap-3 text-brass-deep"><span class="diamond"></span><span class="eyebrow">Success stories</span></div>
        <h1 class="lines mt-6 display leading-[1.05] text-[2.3rem] sm:text-[3rem] lg:text-[3.5rem] text-pine-900">
          <span class="line"><span>Real families.</span></span>
          <span class="line"><span>Real results.</span></span>
          <span class="line"><span>Real <em class="quote text-brass-deep font-500">hope.</em></span></span>
        </h1>
      </div>
      <div class="lg:col-span-5 lg:pb-2">
        <p class="reveal text-[17px] leading-relaxed text-inkt/75" data-d="1">
          Every immigration journey is unique. These stories &mdash; shared with client consent and with confidentiality
          protected &mdash; show what is possible when people have access to trusted legal help.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- ===== INTRO ===== -->
<section class="bg-ivory border-y border-pine/10">
  <div class="mx-auto max-w-[60rem] px-5 lg:px-10 py-20 lg:py-24 text-center">
    <p class="reveal display text-[1.6rem] sm:text-[2rem] lg:text-[2.3rem] leading-[1.2] text-pine-900" data-d="1">
      Behind every case is a family with its own story &mdash; a mother separated from her child, a worker facing
      removal after decades of contribution, a young person who has known no other home.
    </p>
    <p class="reveal mt-7 text-[16px] leading-relaxed text-inkt/65 max-w-2xl mx-auto" data-d="2">
      Liberty Immigration Council was built for these families &mdash; to stand beside them when the system feels
      insurmountable, explain their rights in plain language, and help them find the best path forward.
    </p>
  </div>
</section>

<!-- ===== STORIES ===== -->
<section class="bg-paper">
  <div class="mx-auto max-w-[86rem] px-5 lg:px-10 py-24 lg:py-32">
    <div class="grid md:grid-cols-3 gap-7 lg:gap-9">

      <article class="reveal lift rounded-2xl bg-ivory border border-pine/10 p-8 lg:p-9 flex flex-col" data-d="1">
        <svg class="h-9 w-9 text-brass/40" fill="currentColor" viewBox="0 0 24 24"><path d="M7.5 6C5 6 3 8 3 10.5S5 15 7.5 15c.3 0 .6 0 .8-.1C7.7 16.7 6 18 4 18.3v2.2c4-.4 7-3.6 7-8.2V10.5C11 8 9 6 7.5 6zm9 0C14 6 12 8 12 10.5S14 15 16.5 15c.3 0 .6 0 .8-.1-.6 1.8-2.3 3.1-4.3 3.4v2.2c4-.4 7-3.6 7-8.2V10.5C20 8 18 6 16.5 6z"/></svg>
        <div class="eyebrow text-brass-deep mt-6">Family reunification</div>
        <h2 class="display text-[1.45rem] text-pine-900 mt-2 leading-tight">A long-awaited reunion</h2>
        <p class="mt-3.5 text-[15px] leading-relaxed text-inkt/70 flex-1">
          &ldquo;Maria&rdquo; came to us after years apart from her adult daughter. Through family petitioning, we helped
          her understand her eligibility, prepare her documents, and reach a reunion she had waited years for.
        </p>
      </article>

      <article class="reveal lift rounded-2xl bg-pine-900 text-paper p-8 lg:p-9 flex flex-col relative overflow-hidden grain" data-d="2">
        <div class="absolute -top-16 -right-12 h-56 w-56 rounded-full opacity-25 pointer-events-none" style="background:radial-gradient(circle,rgba(174,138,67,.6) 0%,transparent 62%)"></div>
        <svg class="relative h-9 w-9 text-brass-soft/50" fill="currentColor" viewBox="0 0 24 24"><path d="M7.5 6C5 6 3 8 3 10.5S5 15 7.5 15c.3 0 .6 0 .8-.1C7.7 16.7 6 18 4 18.3v2.2c4-.4 7-3.6 7-8.2V10.5C11 8 9 6 7.5 6zm9 0C14 6 12 8 12 10.5S14 15 16.5 15c.3 0 .6 0 .8-.1-.6 1.8-2.3 3.1-4.3 3.4v2.2c4-.4 7-3.6 7-8.2V10.5C20 8 18 6 16.5 6z"/></svg>
        <div class="relative eyebrow text-brass-soft mt-6">Citizenship preparation</div>
        <h2 class="relative display text-[1.45rem] mt-2 leading-tight">The most important day</h2>
        <p class="relative mt-3.5 text-[15px] leading-relaxed text-paper/80 flex-1">
          &ldquo;Carlos&rdquo; had been a lawful permanent resident for over 12 years without realizing he was eligible
          for citizenship. After a consultation, he prepared for the civics interview and took the oath &mdash; a moment
          he calls &ldquo;the most important day of my life.&rdquo;
        </p>
      </article>

      <article class="reveal lift rounded-2xl bg-ivory border border-pine/10 p-8 lg:p-9 flex flex-col" data-d="3">
        <svg class="h-9 w-9 text-brass/40" fill="currentColor" viewBox="0 0 24 24"><path d="M7.5 6C5 6 3 8 3 10.5S5 15 7.5 15c.3 0 .6 0 .8-.1C7.7 16.7 6 18 4 18.3v2.2c4-.4 7-3.6 7-8.2V10.5C11 8 9 6 7.5 6zm9 0C14 6 12 8 12 10.5S14 15 16.5 15c.3 0 .6 0 .8-.1-.6 1.8-2.3 3.1-4.3 3.4v2.2c4-.4 7-3.6 7-8.2V10.5C20 8 18 6 16.5 6z"/></svg>
        <div class="eyebrow text-brass-deep mt-6">Deportation defense</div>
        <h2 class="display text-[1.45rem] text-pine-900 mt-2 leading-tight">A path through fear</h2>
        <p class="mt-3.5 text-[15px] leading-relaxed text-inkt/70 flex-1">
          &ldquo;Sofia&rdquo; received a notice to appear in immigration court and did not know what to do. Our team
          reviewed her situation, identified potential grounds for defense, and connected her with a qualified attorney.
        </p>
      </article>

    </div>
    <p class="reveal mt-12 text-xs text-inkt/45 max-w-2xl" data-d="1">
      Names and identifying details in all stories are changed or removed to protect client confidentiality. Stories are
      published only with explicit written consent.
    </p>
  </div>
</section>

<!-- ===== CTA BAND ===== -->
<section class="relative bg-pine-900 text-paper grain overflow-hidden">
  <div class="absolute -top-32 -right-28 h-[34rem] w-[34rem] rounded-full opacity-20 pointer-events-none" style="background:radial-gradient(circle,rgba(174,138,67,.55) 0%,transparent 62%)"></div>
  <div class="relative mx-auto max-w-[86rem] px-5 lg:px-10 py-20 lg:py-24 flex flex-col lg:flex-row lg:items-center lg:justify-between gap-8">
    <h2 class="reveal display text-[2rem] lg:text-[2.7rem] leading-[1.1] max-w-2xl">Your story could be<br>the next one.</h2>
    <div class="reveal flex flex-wrap gap-4" data-d="2">
      <a href="index.html#help" class="btn btn-brass inline-flex items-center gap-2 rounded-full px-7 py-4 font-600">Get legal help</a>
      <a href="index.html#donate" class="btn inline-flex items-center gap-2 rounded-full border border-paper/30 px-7 py-4 font-600 hover:bg-paper hover:text-pine-900">Support the mission</a>
    </div>
  </div>
</section>
</main>
'''

build("success-stories.html",
      "Immigrant Family Stories | Liberty Immigration Council",
      "See how Liberty Immigration Council helps families obtain legal status, citizenship, and reunite with loved ones. Real outcomes from trusted, professional legal help.",
      MAIN, nav_active="stories")
