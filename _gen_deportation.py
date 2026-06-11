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
    <div class="mt-9 grid lg:grid-cols-12 gap-12 lg:gap-16 items-end">
      <div class="lg:col-span-7">
        <div class="reveal flex items-center gap-3 text-brass-deep"><span class="diamond"></span><span class="eyebrow">Immigration services &middot; Deportation defense</span></div>
        <h1 class="lines mt-6 display leading-[1.06] text-[2.3rem] sm:text-[3rem] lg:text-[3.5rem] text-pine-900">
          <span class="line"><span>Received a deportation</span></span>
          <span class="line"><span>notice? <em class="quote text-brass-deep font-500">You have rights.</em></span></span>
        </h1>
      </div>
      <div class="lg:col-span-5 lg:pb-2">
        <p class="reveal text-[17px] leading-relaxed text-inkt/75" data-d="1">
          A notice to appear in immigration court is frightening &mdash; but it is not the end. Liberty Immigration
          Council helps you understand your options and connect with qualified legal defense.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- ===== INTRO + WHAT IT INCLUDES ===== -->
<section class="bg-ivory border-y border-pine/10">
  <div class="mx-auto max-w-[86rem] px-5 lg:px-10 py-24 lg:py-32 grid lg:grid-cols-12 gap-12 lg:gap-16">
    <div class="lg:col-span-5 self-start">
      <div class="mask-img duo arch relative overflow-hidden shadow-card aspect-[4/5] max-w-[26rem]">
        <img src="https://images.unsplash.com/photo-1589216532372-1c2a367900d9?auto=format&fit=crop&w=1000&q=80"
             alt="A person consulting with a legal advisor" class="h-full w-full object-cover">
      </div>
    </div>
    <div class="lg:col-span-7">
      <p class="reveal text-[17px] leading-relaxed text-inkt/80" data-d="1">
        If you or a family member has received a <span class="font-600 text-pine-900">Notice to Appear (NTA)</span>
        in immigration court, been detained by ICE, or has a final order of removal &mdash; immediate legal help is critical.
      </p>
      <div class="reveal flex items-center gap-3 text-brass-deep mt-12" data-d="1"><span class="diamond"></span><span class="eyebrow">What deportation defense includes</span></div>
      <p class="reveal text-[15.5px] leading-relaxed text-inkt/65 mt-5" data-d="2">Deportation defense means representing a person in immigration court. A qualified attorney can:</p>
      <ul class="mt-7 space-y-0">
        <li class="reveal flex items-start gap-5 border-t border-pine/15 py-5" data-d="1"><span class="num-index display text-brass-deep text-xl leading-none mt-0.5">01</span><p class="text-inkt/75 leading-relaxed">Review the grounds for removal and identify available legal defenses.</p></li>
        <li class="reveal flex items-start gap-5 border-t border-pine/15 py-5" data-d="1"><span class="num-index display text-brass-deep text-xl leading-none mt-0.5">02</span><p class="text-inkt/75 leading-relaxed">File motions to continue, reopen, or terminate proceedings.</p></li>
        <li class="reveal flex items-start gap-5 border-t border-pine/15 py-5" data-d="2"><span class="num-index display text-brass-deep text-xl leading-none mt-0.5">03</span><p class="text-inkt/75 leading-relaxed">Apply for forms of relief &mdash; cancellation of removal, asylum, and protection under the Convention Against Torture.</p></li>
        <li class="reveal flex items-start gap-5 border-t border-pine/15 py-5" data-d="2"><span class="num-index display text-brass-deep text-xl leading-none mt-0.5">04</span><p class="text-inkt/75 leading-relaxed">Seek a bond reduction for detained individuals.</p></li>
        <li class="reveal flex items-start gap-5 border-y border-pine/15 py-5" data-d="3"><span class="num-index display text-brass-deep text-xl leading-none mt-0.5">05</span><p class="text-inkt/75 leading-relaxed">Prepare and present evidence and testimony at hearings.</p></li>
      </ul>
    </div>
  </div>
</section>

<!-- ===== WHO WE HELP + URGENT ===== -->
<section class="bg-paper">
  <div class="mx-auto max-w-[86rem] px-5 lg:px-10 py-24 lg:py-32 grid lg:grid-cols-2 gap-12 lg:gap-16">
    <div>
      <div class="reveal flex items-center gap-3 text-brass-deep"><span class="diamond"></span><span class="eyebrow">Who we help</span></div>
      <p class="reveal display text-[1.7rem] lg:text-[2.1rem] leading-[1.18] text-pine-900 mt-6" data-d="1">
        We stand beside people who have received an NTA, are in removal proceedings, or fear for their status and possible detention.
      </p>
    </div>
    <div class="reveal" data-d="2">
      <div class="rounded-2xl bg-pine-900 text-paper p-8 lg:p-10 shadow-lift relative overflow-hidden grain">
        <div class="absolute -top-20 -right-16 h-72 w-72 rounded-full opacity-25 pointer-events-none" style="background:radial-gradient(circle,rgba(174,138,67,.6) 0%,transparent 62%)"></div>
        <div class="relative">
          <div class="eyebrow text-brass-soft">Urgent cases</div>
          <p class="mt-4 text-[16.5px] leading-relaxed text-paper/85">
            If you or a relative is currently detained, note it in the intake form &mdash; our team prioritizes detained cases.
          </p>
          <a href="index.html#help" class="nudge btn btn-brass inline-flex items-center gap-2 mt-7 rounded-full px-7 py-4 font-600">
            Submit an urgent intake form
            <svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 12h14m-6-6 6 6-6 6"/></svg>
          </a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ===== DISCLAIMER + CTA ===== -->
<section class="bg-ivory border-t border-pine/10">
  <div class="mx-auto max-w-[86rem] px-5 lg:px-10 py-20 lg:py-24">
    <div class="reveal rounded-2xl border border-brass/30 bg-paper p-7 lg:p-9 max-w-3xl" data-d="1">
      <div class="flex items-start gap-4">
        <svg class="h-6 w-6 text-brass-deep shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 9v4m0 4h.01M10.3 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.7 3.86a2 2 0 0 0-3.42 0z"/></svg>
        <p class="text-[15px] leading-relaxed text-inkt/75">
          <span class="font-600 text-pine-900">Important.</span> Deportation defense requires representation by a licensed
          attorney or an accredited representative. Our team reviews your situation and helps you find the right specialist.
          The information on this page is general and not legal advice.
        </p>
      </div>
    </div>
    <div class="reveal flex flex-wrap items-center gap-x-7 gap-y-3 mt-10" data-d="2">
      <a href="index.html#help" class="nudge btn btn-pine inline-flex items-center gap-2 rounded-full px-7 py-4 font-600">Submit an urgent intake form</a>
      <a href="index.html#programs" class="nudge inline-flex items-center gap-2 font-600 text-pine ulink">
        Explore other immigration services
        <svg class="h-4 w-4 text-brass-deep" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 12h14m-6-6 6 6-6 6"/></svg>
      </a>
    </div>
  </div>
</section>
</main>
'''

build("services-deportation-defense.html",
      "Deportation Defense | Liberty Immigration Council",
      "Received a notice to appear in immigration court? Liberty Immigration Council helps assess your case and connect you with qualified deportation-defense attorneys.",
      MAIN)
