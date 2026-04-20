from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT_A = ROOT / 'version-a'
OUT_B = ROOT / 'version-b'
ASSET = 'source-assets/wp-content/uploads'

PAGES = {
    'index': {
        'title': 'Stellina Connections',
        'slug': '',
        'hero_kicker': 'Your insider for global site selection',
        'hero_title': 'Premier hotel and resort sourcing for meetings, incentives, and executive retreats.',
        'hero_text': 'We source, compare, and negotiate premier hotels and resorts for corporate events worldwide. Stellina Connections brings 25+ years of hospitality experience to secure stronger contracts, save time, and reduce stress.',
        'hero_cta': ('Explore Services', 'services/'),
        'sections': [
            {
                'heading': 'Who we serve',
                'items': [
                    'Corporate teams planning strategic meetings, incentives, and executive retreats.',
                    'Executives who need seamless venue sourcing and strong contract advocacy.',
                    'Groups seeking premier all-inclusive properties or distinctive destinations worldwide.',
                    'Planners who want a trusted partner to simplify the search and protect the outcome.',
                ],
            },
            {
                'heading': 'Why Stellina',
                'text': 'After decades representing hotels, Raffy built Stellina Connections to be firmly on the client side of the table. The advantage is insider knowledge, trusted relationships, and a boutique level of care from the first shortlist to final contract signature.',
                'items': [
                    'Hands-on support from Raffy directly, not a junior handoff.',
                    'Hotel-side experience that sharpens sourcing strategy and negotiation leverage.',
                    'Clear proposal comparisons and fewer inbox-flooding hotel email chains.',
                    'Support that flexes to your style, from highly collaborative to mostly hands-off.',
                ],
            },
        ],
    },
    'about': {
        'title': 'About',
        'slug': 'about/',
        'hero_kicker': 'About Stellina',
        'hero_title': 'Meet your insider.',
        'hero_text': 'After 25 years on the hotel side of the business, Raffy launched Stellina Connections to give clients big-agency capability with the focus and loyalty of a true partner.',
        'sections': [
            {
                'heading': 'Raffy’s story',
                'paragraphs': [
                    'Born in Italy and raised across New Jersey, Tokyo, Frankfurt, Rio de Janeiro, and Bangkok, Raffy learned early how to connect across cultures and navigate international relationships with ease.',
                    'Her career began in New York, where a hotel sponsored her visa after recognizing her drive. She went on to help lead sales strategies across hundreds of hotels and DMCs, gaining a rare inside view into pricing, positioning, and negotiation dynamics.',
                    'Today she uses that experience to advocate for clients — protecting budgets, spotting leverage points, and helping teams move through site selection with confidence.',
                    'When you hire Stellina Connections, you work directly with Raffy. The process can be high-touch or low-maintenance depending on your preference, but the commitment stays the same: relentless advocacy and personal accountability.',
                ],
            }
        ],
    },
    'services': {
        'title': 'Services',
        'slug': 'services/',
        'hero_kicker': 'Services',
        'hero_title': 'Site selection that puts you first.',
        'hero_text': 'From sourcing strategy to contract terms, Stellina helps clients move through hotel selection with a clear process and stronger negotiating leverage.',
        'sections': [
            {
                'heading': 'Scope of services',
                'items': [
                    'RFP development and strategic hotel sourcing',
                    'Detailed proposal comparison in one clean decision-making format',
                    'Client-side advocacy and negotiation support',
                    'Site inspection planning and coordination',
                    'Contract review and concession negotiation',
                    'White-glove communication and follow-through from shortlist to signature',
                ],
            },
            {
                'heading': 'Where Stellina adds value',
                'items': [
                    'Meeting and incentive programs of all sizes',
                    'Executive retreats and leadership gatherings',
                    'All-inclusive resort sourcing and broader global hotel selection',
                    'Attrition, cancellation, and contract-risk conversations where experience matters',
                ],
            },
        ],
    },
    'process': {
        'title': 'Process',
        'slug': 'process/',
        'hero_kicker': 'How it works',
        'hero_title': 'Six strategic steps. Less chaos. Better outcomes.',
        'hero_text': 'A structured process that turns site selection from a messy scramble into a guided, high-confidence decision.',
        'sections': [
            {
                'heading': 'The process',
                'steps': [
                    ('01', 'Discovery Call', 'Understand program goals, budget, destinations, timing, and decision drivers before any outreach begins.'),
                    ('02', 'Hotel Sourcing', 'Distribute the RFP strategically, manage hotel communications, and organize responses into one clear comparison format.'),
                    ('03', 'First-Round Review', 'Compare pricing, availability, meeting space, and fit to identify the strongest initial contenders.'),
                    ('04', 'Shortlist & Negotiation', 'Negotiate rates, concessions, and terms with your preferred options while matching your desired level of involvement.'),
                    ('05', 'Site Inspection', 'Coordinate productive property visits with thoughtful agendas, logistics, and optional accompaniment.'),
                    ('06', 'Contract Finalization', 'Review final terms carefully and push for the strongest possible agreement before signature.'),
                ],
            }
        ],
    },
    'faq': {
        'title': 'FAQ',
        'slug': 'faq/',
        'hero_kicker': 'Frequently asked questions',
        'hero_title': 'We’ve got you.',
        'hero_text': 'Straight answers on how Stellina works and why clients bring Raffy in early.',
        'sections': [
            {
                'heading': 'FAQ',
                'faqs': [
                    ('Do your services cost me extra?', 'No. Hotels pay a commission for site selection services, so there is no added cost to the client. In many cases, Stellina saves clients more through stronger negotiation than they would secure on their own.'),
                    ('Will hotel rates be higher if I use Stellina Connections?', 'No. Rates are not inflated. In practice, the combination of industry relationships and hotel-side expertise often improves concessions, terms, and total value.'),
                    ('What types of events do you handle?', 'Everything from executive retreats to larger incentive trips and conferences, with the same level of detail and advocacy regardless of size.'),
                    ('Do you only work with all-inclusive resorts?', 'No. All-inclusives are a strength, but Stellina sources hotels and resorts globally across brands, destinations, and budgets.'),
                    ('When should I bring you in?', 'Ideally at the beginning. Early involvement creates more leverage, more options, and better protection before contracts start hardening.'),
                    ('Why not just contact hotels directly?', 'You can, but it usually means hours of outreach, follow-up, and negotiation. Stellina takes on that work while protecting your leverage and acting as your advocate.'),
                    ('What makes Stellina different from bigger agencies?', 'You work directly with Raffy, not a junior coordinator. It is boutique by design: more personal attention, more accountability, and deeper hotel-side knowledge in the room.'),
                ],
            }
        ],
    },
    'contact': {
        'title': 'Contact',
        'slug': 'contact/',
        'hero_kicker': 'Contact',
        'hero_title': 'Let’s find the right property.',
        'hero_text': 'Your trusted partner for meetings, incentives, and events worldwide.',
        'sections': [
            {
                'heading': 'Get in touch',
                'contact': [
                    ('Email', 'raffy@stellinaconnections.com', 'mailto:raffy@stellinaconnections.com'),
                    ('LinkedIn', 'linkedin.com/in/raffaellatasca', 'https://www.linkedin.com/in/raffaellatasca/'),
                ],
                'paragraphs': [
                    'If you already have destinations in mind, a shortlist started, or a contract that needs another set of experienced eyes, Stellina can jump in and help.'
                ],
            }
        ],
    },
}

PRIMARY_LOGO_DARK = f'{ASSET}/2025/10/Stellina-Connections-Logo-Dark.svg'
PRIMARY_LOGO_LIGHT = f'{ASSET}/2025/10/Stellina-Connections-Logo-White.svg'
HERO_A = f'{ASSET}/2025/10/Stellina-site-selection-company-12.jpg'
HERO_B = f'{ASSET}/2025/11/IMG_6051-scaled.jpg'
PORTRAIT = f'{ASSET}/2025/09/unnamed.png'
GALLERY = [
    f'{ASSET}/2025/10/Stellina-site-selection-company-11-1.jpg',
    f'{ASSET}/2025/10/Stellina-site-selection-company-13-1.jpg',
    f'{ASSET}/2025/10/patrick-robert-doyle-AH8zKXqFITA-unsplash-1.jpg',
]


def nav(current: str):
    items = [('Home', ''), ('About', 'about/'), ('Services', 'services/'), ('Process', 'process/'), ('FAQ', 'faq/'), ('Contact', 'contact/')]
    out = []
    for label, href in items:
        cls = 'active' if href == current else ''
        out.append(f'<a class="{cls}" href="/{href}">{label}</a>')
    return ''.join(out)


def footer():
    return '''<footer class="site-footer"><div class="container footer-grid"><div><img class="footer-logo" src="/%s" alt="Stellina Connections logo" /><p>Your trusted partner for meetings, incentives, and events worldwide.</p></div><div><h4>Connect</h4><p><a href="mailto:raffy@stellinaconnections.com">raffy@stellinaconnections.com</a><br><a href="https://www.linkedin.com/in/raffaellatasca/" target="_blank" rel="noreferrer">LinkedIn</a></p></div></div></footer>''' % PRIMARY_LOGO_LIGHT


def page_shell(version_name: str, page_key: str, page: dict, inner: str, css_name: str, logo: str, theme_class: str):
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{page['title']} | Stellina Connections</title>
  <meta name="description" content="Stellina Connections helps clients source, compare, and negotiate premier hotels and resorts for meetings, incentives, and executive retreats." />
  <link rel="icon" href="/{ASSET}/2025/11/cropped-favicon-32x32.jpg" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Cormorant+Garamond:wght@500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/{css_name}" />
</head>
<body class="{theme_class}">
  <header class="site-header">
    <div class="container nav-wrap">
      <a href="/" class="brand"><img src="/{logo}" alt="Stellina Connections" /></a>
      <nav>{nav(page['slug'])}</nav>
    </div>
  </header>
  {inner}
  {footer()}
</body>
</html>'''


def render_sections(page_key: str, page: dict, variant: str):
    blocks = []
    for section in page.get('sections', []):
        body = [f'<section class="section"><div class="container"><div class="section-head"><p class="eyebrow">{page["hero_kicker"]}</p><h2>{section["heading"]}</h2></div>']
        if 'text' in section:
            body.append(f'<p class="lede">{section["text"]}</p>')
        if 'paragraphs' in section:
            body.extend(f'<p class="lede narrow">{p}</p>' for p in section['paragraphs'])
        if 'items' in section:
            body.append('<div class="card-grid">')
            for item in section['items']:
                body.append(f'<article class="card"><p>{item}</p></article>')
            body.append('</div>')
        if 'steps' in section:
            body.append('<div class="steps">')
            for num, title, text in section['steps']:
                body.append(f'<article class="step"><span>{num}</span><h3>{title}</h3><p>{text}</p></article>')
            body.append('</div>')
        if 'faqs' in section:
            body.append('<div class="faq-list">')
            for q, a in section['faqs']:
                body.append(f'<details><summary>{q}</summary><p>{a}</p></details>')
            body.append('</div>')
        if 'contact' in section:
            body.append('<div class="contact-grid">')
            for label, text, href in section['contact']:
                body.append(f'<article class="contact-card"><h3>{label}</h3><p><a href="{href}">{text}</a></p></article>')
            body.append('</div>')
        body.append('</div></section>')
        blocks.append(''.join(body))
    if page_key == 'index':
        blocks.append('<section class="section alt"><div class="container"><div class="section-head"><p class="eyebrow">Partners & destinations</p><h2>Built for the moments that matter.</h2></div><div class="image-row">' + ''.join(f'<img src="/{img}" alt="Hotel destination photography" />' for img in GALLERY) + '</div></div></section>')
    return ''.join(blocks)


def hero(page_key: str, page: dict, variant: str):
    image = HERO_A if variant == 'a' else HERO_B
    if page_key == 'about':
        image = PORTRAIT
    cta = page.get('hero_cta', ('Contact', 'contact/'))
    return f'''<main>
    <section class="hero">
      <div class="container hero-grid">
        <div class="hero-copy">
          <p class="eyebrow">{page['hero_kicker']}</p>
          <h1>{page['hero_title']}</h1>
          <p class="lede">{page['hero_text']}</p>
          <div class="hero-actions"><a class="button primary" href="/{cta[1]}">{cta[0]}</a><a class="button secondary" href="/contact/">Contact Raffy</a></div>
        </div>
        <div class="hero-media"><img src="/{image}" alt="Stellina Connections visual" /></div>
      </div>
    </section>
    {render_sections(page_key, page, variant)}
  </main>'''


CSS_A = '''
:root{--bg:#f7f4ee;--bg-alt:#fff;--text:#1f2430;--muted:#5d6675;--line:#ddd3c7;--accent:#8f6b3b;--accent-deep:#4f3723;--card:#fffaf4;--footer:#1f2025}
*{box-sizing:border-box}html,body{margin:0;padding:0}body{font-family:Inter,system-ui,sans-serif;background:var(--bg);color:var(--text);line-height:1.6}a{color:inherit;text-decoration:none}img{max-width:100%;display:block}.container{width:min(1120px,calc(100% - 2rem));margin:0 auto}.site-header{position:sticky;top:0;background:rgba(247,244,238,.94);backdrop-filter:blur(12px);border-bottom:1px solid var(--line);z-index:10}.nav-wrap{display:flex;align-items:center;justify-content:space-between;padding:1rem 0}.brand img{height:52px}.site-header nav{display:flex;gap:1rem;flex-wrap:wrap}.site-header nav a{padding:.5rem .8rem;border-radius:999px;color:var(--muted);font-weight:600}.site-header nav a.active,.site-header nav a:hover{background:#ece2d4;color:var(--accent-deep)}.hero{padding:4rem 0 3rem}.hero-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:2rem;align-items:center}.eyebrow{text-transform:uppercase;letter-spacing:.14em;font-size:.78rem;color:var(--accent);font-weight:700;margin:0 0 1rem}.hero h1,.section h2{font-family:"Cormorant Garamond",serif;line-height:.98;letter-spacing:-.02em}.hero h1{font-size:clamp(3rem,6vw,5.5rem);margin:.2rem 0 1rem}.lede{font-size:1.1rem;color:var(--muted);max-width:64ch}.hero-actions{display:flex;gap:1rem;flex-wrap:wrap;margin-top:1.75rem}.button{padding:.95rem 1.3rem;border-radius:999px;font-weight:700}.button.primary{background:var(--accent-deep);color:#fff}.button.secondary{border:1px solid var(--line);background:#fff}.hero-media img{border-radius:28px;min-height:540px;object-fit:cover;box-shadow:0 30px 80px rgba(61,42,21,.18)}.section{padding:1.5rem 0 4rem}.section.alt{background:#efe7dc}.section-head{max-width:760px;margin-bottom:1.5rem}.section h2{font-size:clamp(2.3rem,4vw,4rem);margin:0}.narrow{max-width:72ch}.card-grid,.contact-grid,.steps,.image-row{display:grid;gap:1rem}.card-grid{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}.card,.contact-card,.step,details{background:var(--card);border:1px solid var(--line);border-radius:22px;padding:1.25rem 1.25rem 1.1rem;box-shadow:0 10px 30px rgba(80,56,26,.06)}.steps{grid-template-columns:repeat(auto-fit,minmax(250px,1fr))}.step span{display:inline-flex;width:3rem;height:3rem;align-items:center;justify-content:center;border-radius:50%;background:#efe2d1;color:var(--accent-deep);font-weight:800;margin-bottom:1rem}.step h3,.contact-card h3{margin:.2rem 0 .4rem;font-size:1.1rem}.faq-list{display:grid;gap:.85rem}details summary{cursor:pointer;font-weight:700;list-style:none}details summary::-webkit-details-marker{display:none}details p{color:var(--muted);margin:1rem 0 .2rem}.contact-grid{grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}.image-row{grid-template-columns:repeat(3,1fr)}.image-row img{border-radius:24px;height:280px;width:100%;object-fit:cover}.site-footer{background:var(--footer);color:#f4ede3;padding:3rem 0;margin-top:3rem}.footer-grid{display:grid;grid-template-columns:2fr 1fr;gap:2rem}.footer-logo{height:44px;margin-bottom:1rem}.site-footer a{color:#fff;text-decoration:underline}@media (max-width: 860px){.hero-grid,.footer-grid{grid-template-columns:1fr}.site-header nav{display:none}.hero-media img{min-height:320px}.image-row{grid-template-columns:1fr}}
'''

CSS_B = '''
:root{--bg:#0f1722;--surface:#16202f;--surface-2:#1d2938;--text:#eef3f7;--muted:#b9c4cf;--accent:#d6a45f;--accent-2:#7fd3cb;--line:rgba(255,255,255,.1)}*{box-sizing:border-box}html,body{margin:0;padding:0}body{font-family:Inter,system-ui,sans-serif;background:radial-gradient(circle at top left,#1b2737 0,#0f1722 45%,#0c1320 100%);color:var(--text);line-height:1.6}a{color:inherit;text-decoration:none}img{max-width:100%;display:block}.container{width:min(1160px,calc(100% - 2rem));margin:0 auto}.site-header{position:sticky;top:0;background:rgba(9,14,22,.75);backdrop-filter:blur(16px);border-bottom:1px solid var(--line);z-index:20}.nav-wrap{display:flex;justify-content:space-between;align-items:center;padding:1rem 0}.brand img{height:54px;filter:brightness(0) invert(1)}.site-header nav{display:flex;gap:.5rem;flex-wrap:wrap}.site-header nav a{padding:.55rem .9rem;border-radius:999px;color:var(--muted);font-weight:600}.site-header nav a.active,.site-header nav a:hover{background:rgba(214,164,95,.16);color:#fff}.hero{padding:4.5rem 0 3rem}.hero-grid{display:grid;grid-template-columns:1fr 1fr;gap:2rem;align-items:center}.eyebrow{text-transform:uppercase;letter-spacing:.18em;font-size:.78rem;color:var(--accent-2);font-weight:800;margin:0 0 1rem}.hero h1,.section h2{font-family:"Cormorant Garamond",serif;line-height:.98;letter-spacing:-.03em}.hero h1{font-size:clamp(3.1rem,6vw,6rem);margin:0 0 1rem}.lede{font-size:1.08rem;color:var(--muted);max-width:64ch}.hero-actions{display:flex;gap:1rem;flex-wrap:wrap;margin-top:1.7rem}.button{padding:1rem 1.35rem;border-radius:999px;font-weight:700}.button.primary{background:linear-gradient(135deg,var(--accent),#f2c181);color:#1b1611}.button.secondary{border:1px solid var(--line);background:rgba(255,255,255,.03)}.hero-media{position:relative}.hero-media::after{content:"";position:absolute;inset:auto -20px -20px auto;width:140px;height:140px;background:radial-gradient(circle,#7fd3cb 0,rgba(127,211,203,0) 70%);filter:blur(6px)}.hero-media img{border-radius:30px;height:600px;width:100%;object-fit:cover;border:1px solid var(--line);box-shadow:0 25px 70px rgba(0,0,0,.35)}.section{padding:1.5rem 0 4rem}.section.alt{background:linear-gradient(180deg,rgba(255,255,255,.03),rgba(255,255,255,0))}.section-head{max-width:760px;margin-bottom:1.5rem}.section h2{font-size:clamp(2.4rem,4vw,4.3rem);margin:0}.narrow{max-width:74ch}.card-grid,.contact-grid,.steps,.image-row{display:grid;gap:1rem}.card-grid{grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}.card,.contact-card,.step,details{background:linear-gradient(180deg,rgba(255,255,255,.06),rgba(255,255,255,.03));border:1px solid var(--line);border-radius:24px;padding:1.35rem;box-shadow:0 18px 50px rgba(0,0,0,.18)}.steps{grid-template-columns:repeat(auto-fit,minmax(250px,1fr))}.step span{display:inline-flex;align-items:center;justify-content:center;width:3rem;height:3rem;border-radius:16px;background:rgba(214,164,95,.14);color:#ffd59e;font-weight:800;margin-bottom:1rem}.step h3,.contact-card h3{margin:.2rem 0 .45rem;font-size:1.1rem}.faq-list{display:grid;gap:.85rem}details summary{cursor:pointer;font-weight:700;list-style:none}details summary::-webkit-details-marker{display:none}details p{color:var(--muted);margin:1rem 0 .15rem}.contact-grid{grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}.image-row{grid-template-columns:repeat(3,1fr)}.image-row img{border-radius:24px;height:300px;width:100%;object-fit:cover;border:1px solid var(--line)}.site-footer{border-top:1px solid var(--line);padding:3rem 0;background:rgba(255,255,255,.02);margin-top:3rem}.footer-grid{display:grid;grid-template-columns:2fr 1fr;gap:2rem}.footer-logo{height:46px;filter:brightness(0) invert(1);margin-bottom:1rem}.site-footer a{color:#fff;text-decoration:underline}@media (max-width:860px){.hero-grid,.footer-grid{grid-template-columns:1fr}.site-header nav{display:none}.hero-media img{height:340px}.image-row{grid-template-columns:1fr}}
'''


def build_version(out_dir: Path, css: str, css_name: str, logo: str, theme: str, variant: str):
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / css_name).write_text(css)
    for key, page in PAGES.items():
        inner = hero(key, page, variant)
        html = page_shell('A' if variant == 'a' else 'B', key, page, inner, css_name, logo, theme)
        dest_dir = out_dir / page['slug']
        if page['slug']:
            dest_dir.mkdir(parents=True, exist_ok=True)
            (dest_dir / 'index.html').write_text(html)
        else:
            (out_dir / 'index.html').write_text(html)

    for name in ['source-assets']:
        target = out_dir / name
        if target.exists() or target.is_symlink():
            target.unlink()
        target.symlink_to(ROOT / name, target_is_directory=True)


build_version(OUT_A, CSS_A, 'styles.css', PRIMARY_LOGO_DARK, 'theme-a', 'a')
build_version(OUT_B, CSS_B, 'styles.css', PRIMARY_LOGO_LIGHT, 'theme-b', 'b')
print('Built version-a and version-b')
