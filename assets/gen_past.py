# -*- coding: utf-8 -*-
# Generator for ALTS past-event sum-up pages (new design)
import json, html

CDN = "https://cdn.prod.website-files.com/6899b009eafbcc44466f60d3/"

EVENTS = [
  dict(
    slug="alts-past-cee-spring-2026",
    title='ALTS CEE <em>Spring Edition</em>',
    date="April 21–23, 2026", place="Budapest, Hungary",
    hero=CDN+"69f89cfcc32852a7af7c66a6_Budapest%202026.jpg",
    wave="wave-a",
    recap="ALTS CEE in Budapest marked a key step in our expansion across Central and Eastern Europe, gathering a carefully curated community of travel designers from Hungary, Poland, the Czech Republic, Romania, Bulgaria, Slovakia, Slovenia, Moldova, the Baltics and Serbia. Set in one of the region's most captivating capitals, the event combined focused business meetings with the energy of a fast-evolving market, opening the door to new partnerships and fresh opportunities.",
    stats=[("1048","match-made pre-scheduled 1:1 meetings"),("2.5","days of outstanding networking"),("50","hand-picked luxury buyers from across Central & Eastern Europe"),("40","selected international exhibitors from around the world")],
    partners=[("Destination Partner","69f8aff11df88ae0aebd58eb_budapest%201.png"),("Host Venue","68f75ff363cb077f13c5e5d7_w-budapest.svg")],
    gallery=["69f8bd3eeeae6d31c76ad8cf_10.jpg","69f8bd3c6db20c3f186f61ba_8.jpg","69f8bd3d7beec6f37e6d62b5_3.jpg","69f8bd3d5765452dab9c5c64_7.jpg","69f8bd3ba7b4b33eaf7040e5_4.jpg","69f8bd3b97f759f783847d9f_12.jpg","69f8bd3bd32ec5f15a680376_2.jpg","69f8bd3b9dc0c6279b896715_1.jpg","69f8bd3c19489b2944c27092_15.jpg","69f8bd3ce8c8a03e3326f4f5_14.jpg","69f8bd3d416747abc80d6a5c_9.jpg","69f8bd3dc83b9145a0646dd6_5.jpg","69f9d080985493346172cbd6_210A9289%201.jpg","69f9d07f4d2487d5ffa48476_DSC02471-Enhanced-NR%201.jpg","69f9d07fcbfc87a95abe2ba6_23.04.26_AltsBp_GalaDinner_144%201.jpg","69f9d07c3f1357c3a20565fe_budapest-164%201.jpg"],
    next=[("April 20, 2026","ALTS Prague Workshop & Dinner","alts-past-prague-2026.html","69f89b985e73d9a0dd080fe4_Prague%202026.jpg"),
          ("February 22–24, 2026","ALTS UK & Europe","alts-past-uk-europe-2026.html","69f89aad9ddecf6ef5acacb8_madeira%202026.jpg")],
  ),
  dict(
    slug="alts-past-prague-2026",
    title='ALTS Prague <em>Workshop &amp; Dinner</em>',
    date="April 20, 2026", place="Prague, Czech Republic",
    hero=CDN+"69f89b985e73d9a0dd080fe4_Prague%202026.jpg",
    wave="wave-b",
    recap="We were pleased to welcome our guests to a refined evening of networking and conversation in the heart of Prague. The event brought together a curated selection of top-tier luxury travel agencies from the Czech Republic and international travel suppliers from around the world. Set in an elegant and intimate atmosphere, the business dinner offered a valuable platform to connect with key decision-makers, strengthen relationships, and explore new opportunities in the luxury travel space.",
    stats=[("228","curated 1:1 meetings with luxury leisure travel leaders"),("1","exclusive evening combining a focused workshop and a stylish dinner"),("26","hand-picked luxury buyers from the Czech Republic"),("17","premium travel suppliers from around the world")],
    partners=[("Host Venue","69f8c4260fdc5e3d25f8042d_augustine%20hotel.png")],
    gallery=["69f8cbd7162681a1636bd8fb_6.jpg","69f8cbd74535dcf316904c05_12.jpg","69f8cbd72d5fa43d3ba9e2d7_4.jpg","69f8cbd7b5e1a3317375b43e_3.jpg","69f8cbd81cb7f1abc182df95_10.jpg","69f8cbd80a1566ed97b65b96_1.jpg","69f8cbd8097ca8f8468a0e62_8.jpg","69f8cbd85f9ff9213e742292_2.jpg","69f8cbd806460d0d1fdbc274_14.jpg","69f8cbd9bd211e1175fd90ba_15.jpg","69f8cbd930c69168321b9956_11.jpg","69f8cbd92a3e8870028807ed_7.jpg"],
    next=[("April 21–23, 2026","ALTS CEE Spring Edition","alts-past-cee-spring-2026.html","69f89cfcc32852a7af7c66a6_Budapest%202026.jpg"),
          ("February 22–24, 2026","ALTS UK & Europe","alts-past-uk-europe-2026.html","69f89aad9ddecf6ef5acacb8_madeira%202026.jpg")],
  ),
  dict(
    slug="alts-past-uk-europe-2026",
    title='ALTS UK <em>&amp; Europe</em>',
    date="February 22–24, 2026", place="Madeira, Portugal",
    hero=CDN+"69f89aad9ddecf6ef5acacb8_madeira%202026.jpg",
    wave="wave-c",
    recap="ALTS UK & Europe in Madeira delivered a vibrant mix of curated business connections, inspiring encounters and authentic island experiences. Framed by panoramic Atlantic views, this edition proved that great business happens even better in extraordinary places.",
    stats=[("1196","1:1 meetings"),("3","days of business and fun"),("50","hand-picked buyers from UK & Europe"),("40","luxury worldwide travel suppliers")],
    partners=[("Destination Partner","69f8d6e55cabc28a4e61f4da_madeira%20logo%202026.png"),("Host Venue","69f8d73d96c85d52f4770eea_savoy%20color%20logo.png"),("Event Partner","69f8d88397cf274209c74f2f_insider%20logo.png")],
    gallery=["69f8e0180a807326e17c0de5_ALTS_MADEIRA_03_1272%201.jpg","69f8e01ff74e8b9a85bf259a_ALTS_MADEIRA_02_0595%201.jpg","69f8e01f8e6015304b0ff50a_DSC_0942%201.jpg","69f8e020dd58b09bea98aaf4_DSC_3825%201.jpg","69f8e020d51089c067c6ebb9_E-Bike%20Photo%20Reportage-19%20(1)%201.jpg","69f8e01e2986c45fba6bc649_A7303025%201.jpg","69f8e01e2986c45fba6bc646_DSC_4194%201.jpg","69f8e01ed4a0eb3796bfeea4_A7400371%20(1)%201.jpg","69f8e01e887200bc13c34238_A7400018%201.jpg","69f8e01d81a4214a857668f3_DSC_4055%201.jpg","69f8e01d2f486a09ecde297e_A7400021%201.jpg","69f8e01d826dde394ac32b21_A7400448%201.jpg","69f8e01c7eff06d414665fab_A7302472%201.jpg","69f8e01befa34e354ed6530b_y-28%201.jpg","69f8e01a9c78f04d81569f8e_SA105408%201.jpg","69f8e01af69600e4225b14cc_ALTS_MADEIRA_01_0103%201.jpg"],
    next=[("April 20, 2026","ALTS Prague Workshop & Dinner","alts-past-prague-2026.html","69f89b985e73d9a0dd080fe4_Prague%202026.jpg"),
          ("November 13–14, 2025","ALTS CEE in Warsaw","alts-past-warsaw-2025.html","693994a5738e27c73ef6abe7_Nobu%20Hotel%20Warsaw5.jpg")],
  ),
  dict(
    slug="alts-past-warsaw-2025",
    title='ALTS CEE <em>in Warsaw</em>',
    date="November 13–14, 2025", place="NOBU Hotel Warsaw, Poland",
    hero=CDN+"693994a5738e27c73ef6abe7_Nobu%20Hotel%20Warsaw5.jpg",
    wave="wave-a",
    recap="ALTS CEE in Warsaw brought together over 100 luxury travel professionals, including exhibitors from around the globe and carefully selected buyers from across Central and Eastern Europe: Poland, Romania, Bulgaria, Slovakia, Czech Republic, Hungary, Serbia and Slovenia. We enjoyed an incredible time in Poland's vibrant capital, forging lasting connections and creating wonderful memories together.",
    stats=[("1.5","days of high-end networking"),("40","1:1 meetings"),("100","luxury travel professionals")],
    partners=[("Destination Partner","693988a222595821462a889e_madeira_logo.svg"),("Host Hotel","6932cea75187d244b4ca3ad9_nobu%20hotel.svg")],
    gallery=["693999faa81ce380db3c5f4a_1E7A2041.jpg","693999f9f9a69dc90228e5b7_1E7A0823.jpg","693999f8658b6693cb3160c0_1E7A0255.jpg","693999f8be9e67c9358b4096_1E7A0229.jpg","693999fa07d69e09d08a5c6a_1E7A1124.jpg","693999fa668ab7a2689835f6_1E7A3377.jpg","693999f7e8468af38afdc729_1E7A1924.jpg","693999f8dedd609aaeb94b7e_1E7A2457.jpg","693999f771d5534e94a8a0a6_1E7A1264.jpg","693999fa385b8fd4349608be_1E7A3424.jpg","693999f8a428ddbbab54661b_1E7A0706.jpg","69399bf9a34bda0d6d255590_1E7A2852.jpg"],
    next=[("February 22–24, 2026","ALTS UK & Europe","alts-past-uk-europe-2026.html","69f89aad9ddecf6ef5acacb8_madeira%202026.jpg"),
          ("October 7–9, 2025","ALTS UK | EU Douro Valley","alts-past-douro-2025.html","6909f5521cc007e29bf4fb62_Douro.png")],
  ),
]

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_plain} | Access Luxury Travel Show</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300&family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/alts.css">
</head>
<body>

<header id="hdr">
  <div class="wrap nav">
    <a href="alts-redesign-home.html" class="brand">
      <img class="logo" src="{cdn}6899bc2f414ba1d0943f1657_Logo%20Black.svg" alt="ALTS">
      <span class="brand-txt">Access Luxury<br>Travel Show</span>
    </a>
    <nav class="links">
      <a href="alts-events.html">Events</a>
      <a href="alts-buyer-registration.html">For Buyers</a>
      <a href="alts-exhibitor-registration.html">For Exhibitors</a>
      <a href="alts-about.html">About ALTS</a>
      <a href="alts-contact.html">Contacts</a>
      <a href="alts-exhibitor-registration.html" class="btn btn-grad">Request an Invitation</a>
    </nav>
  </div>
</header>
"""

FOOTER = """
<footer id="contacts">
  <div class="wrap">
    <div class="f-nav">
      <div class="f-links">
        <a href="alts-events.html">Events</a><i>•</i>
        <a href="alts-buyer-registration.html">For Buyers</a><i>•</i>
        <a href="alts-exhibitor-registration.html">For Exhibitors</a><i>•</i>
        <a href="alts-about.html">About ALTS</a><i>•</i>
        <a href="alts-contact.html">Contacts</a>
      </div>
      <div class="f-social">
        <a href="https://www.facebook.com/accessluxurytravelshow" aria-label="Facebook"><svg viewBox="0 0 24 24"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.4v7A10 10 0 0 0 22 12Z"/></svg></a>
        <a href="https://www.linkedin.com/company/access-luxury-travel-show/" aria-label="LinkedIn"><svg viewBox="0 0 24 24"><path d="M20.4 3H3.6A.6.6 0 0 0 3 3.6v16.8c0 .3.3.6.6.6h16.8c.3 0 .6-.3.6-.6V3.6a.6.6 0 0 0-.6-.6ZM8.3 18.4H5.7V9.9h2.6v8.5ZM7 8.7a1.5 1.5 0 1 1 0-3.1 1.5 1.5 0 0 1 0 3ZM18.4 18.4h-2.6v-4.1c0-1 0-2.3-1.4-2.3s-1.6 1.1-1.6 2.2v4.2h-2.7V9.9h2.5v1.2h.1a2.8 2.8 0 0 1 2.5-1.4c2.7 0 3.2 1.8 3.2 4v4.7Z"/></svg></a>
        <a href="https://www.instagram.com/alts.events/" aria-label="Instagram"><svg viewBox="0 0 24 24"><path d="M12 2.2c3.2 0 3.6 0 4.8.1 1.2 0 1.8.2 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.2.1 1.6.1 4.8s0 3.6-.1 4.8c0 1.2-.2 1.8-.4 2.2a3.9 3.9 0 0 1-2.3 2.3c-.4.2-1 .4-2.2.4-1.2.1-1.6.1-4.8.1s-3.6 0-4.8-.1c-1.2 0-1.8-.2-2.2-.4a3.9 3.9 0 0 1-2.3-2.3c-.2-.4-.4-1-.4-2.2-.1-1.2-.1-1.6-.1-4.8s0-3.6.1-4.8c0-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4 1.2-.1 1.6-.1 4.8-.1Zm0 2A61 61 0 0 0 7.3 4.3c-1.1 0-1.7.2-2 .4-.6.2-.9.5-1.1 1.1-.2.3-.4.9-.4 2-.1 1.2-.1 1.5-.1 4.7s0 3.5.1 4.7c0 1.1.2 1.7.4 2 .2.6.5.9 1.1 1.1.3.2.9.4 2 .4 1.2.1 1.5.1 4.7.1s3.5 0 4.7-.1c1.1 0 1.7-.2 2-.4.6-.2.9-.5 1.1-1.1.2-.3.4-.9.4-2 .1-1.2.1-1.5.1-4.7s0-3.5-.1-4.7c0-1.1-.2-1.7-.4-2a1.9 1.9 0 0 0-1.1-1.1c-.3-.2-.9-.4-2-.4-1.2-.1-1.5-.1-4.7-.1Zm0 3.3a5 5 0 1 1 0 10 5 5 0 0 1 0-10Zm0 2a3 3 0 1 0 0 6 3 3 0 0 0 0-6Zm5.2-3.5a1.2 1.2 0 1 1 0 2.4 1.2 1.2 0 0 1 0-2.4Z"/></svg></a>
      </div>
    </div>
    <hr>
    <div class="f-brand">
      <div class="logos">
        <span style="display:flex;flex-direction:column;gap:6px">
          <img src="assets/wordmark-white.png" alt="ACCESS" style="height:26px;width:auto">
          <img src="assets/tagline-white.png" alt="Explore | Connect | Travel" style="height:9px;width:auto">
        </span>
        <span class="x">×</span>
        <img src="{cdn}6899bc2f414ba1d0943f1657_Logo%20Black.svg" alt="ALTS" style="height:44px;filter:brightness(0) invert(1)">
      </div>
      <p>ALTS is affiliated with Access.Marketing – an international premium travel representation company with 15+ years of exceptional experience in providing custom services of sales, marketing and PR across the markets of CEE, DACH, CIS, Central Asia, and Turkey.</p>
    </div>
    <hr>
    <div class="f-bottom">
      <p class="copy">© 2026 ALTS EVENTS LIMITED 6 St David Square,<br>London, E14 3WA, United Kingdom</p>
      <p class="f-motto">we meet <em>differently.</em></p>
    </div>
  </div>
</footer>

<div class="lightbox" id="lb">
  <span class="close" onclick="lbClose()">×</span>
  <span class="arr prev" onclick="lbNav(-1)">‹</span>
  <img id="lb-img" src="" alt="">
  <span class="arr next" onclick="lbNav(1)">›</span>
</div>

<script>
  const hdr=document.getElementById('hdr');
  addEventListener('scroll',()=>hdr.classList.toggle('scrolled',scrollY>60),{passive:true});
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}}),{threshold:.12});
  document.querySelectorAll('.reveal').forEach(el=>io.observe(el));

  // lightbox
  const shots=[...document.querySelectorAll('.gallery a')].map(a=>a.href);
  let cur=0;
  document.querySelectorAll('.gallery a').forEach((a,i)=>a.addEventListener('click',e=>{e.preventDefault();cur=i;lbShow()}));
  function lbShow(){document.getElementById('lb-img').src=shots[cur];document.getElementById('lb').classList.add('open')}
  function lbClose(){document.getElementById('lb').classList.remove('open')}
  function lbNav(d){cur=(cur+d+shots.length)%shots.length;lbShow()}
  document.getElementById('lb').addEventListener('click',e=>{if(e.target.id==='lb')lbClose()});
  addEventListener('keydown',e=>{if(!document.getElementById('lb').classList.contains('open'))return;if(e.key==='Escape')lbClose();if(e.key==='ArrowRight')lbNav(1);if(e.key==='ArrowLeft')lbNav(-1)});
</script>
</body>
</html>
"""

def build(ev):
    import re
    title_plain = re.sub(r'<[^>]+>','',ev['title']).replace('&amp;','&')
    out = HEAD.format(title_plain=title_plain, cdn=CDN)
    # hero
    out += f"""
<section class="hero">
  <img class="hero-bg" src="{ev['hero']}" alt="{title_plain}">
  <img class="hero-waves right" src="assets/{ev['wave']}.svg" alt="">
  <div class="hero-inner wrap">
    <span class="date-pill">{ev['date']}</span>
    <h1>{ev['title']}</h1>
    <p class="place">{ev['place']}</p>
  </div>
</section>

<section class="overview">
  <div class="wrap ov-grid">
    <h2 class="sec-h big reveal">Event <em>recap</em></h2>
    <div class="ov-text reveal"><p>{ev['recap']}</p></div>
  </div>
</section>

<section class="numbers">
  <img class="bg-wave" src="assets/{ev['wave']}.svg" alt="">
  <div class="wrap">
    <div class="num-head reveal"><h2 class="sec-h">Event <em>in numbers</em></h2></div>
    <div class="num-grid"{' style="grid-template-columns:repeat(3,1fr)"' if len(ev['stats'])==3 else ''}>
"""
    for n,label in ev['stats']:
        out += f'      <div class="num-card reveal"><b>{n}</b><span>{label}</span></div>\n'
    out += "    </div>\n  </div>\n</section>\n"
    # partners
    if ev['partners']:
        out += """
<section class="partners">
  <div class="wrap">
    <h2 class="sec-h center reveal">Event <em>partners</em></h2>
    <div class="pt-grid">
"""
        for role, img in ev['partners']:
            out += f'      <div class="pt-card reveal"><span>{role}</span><img src="{CDN}{img}" alt="{role}"></div>\n'
        out += "    </div>\n  </div>\n</section>\n"
    # gallery
    out += """
<section class="gallery-sec">
  <div class="wrap">
    <h2 class="sec-h center reveal">Highlights <em>from the event</em></h2>
    <div class="gallery">
"""
    for img in ev['gallery']:
        out += f'      <a href="{CDN}{img}"><img loading="lazy" src="{CDN}{img}" alt=""></a>\n'
    out += "    </div>\n  </div>\n</section>\n"
    # next events
    out += """
<section class="next" style="padding-top:20px;padding-bottom:110px">
  <div class="wrap">
    <div class="next-head reveal"><h2 class="sec-h">More <em>events</em></h2></div>
    <div class="next-grid">
"""
    for date,name,href,img in ev['next']:
        out += f"""      <a class="next-card reveal" href="{href}">
        <img class="bg" src="{CDN}{img}" alt="">
        <div class="txt"><h3>{name}</h3><p class="date">{date}</p></div>
        <span class="ev-arrow"><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
      </a>
"""
    out += "    </div>\n  </div>\n</section>\n"
    out += FOOTER.replace('{cdn}', CDN)
    return out

import os
outdir = os.path.dirname(os.path.abspath(__file__)) + '/..'
for ev in EVENTS:
    p = os.path.join(outdir, ev['slug'] + '.html')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(build(ev))
    print('written', p)
