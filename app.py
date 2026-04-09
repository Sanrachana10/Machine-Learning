import streamlit as st

st.set_page_config(
    page_title="SGSITS — Department of IT",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>

:root {
    --navy:   #0b1f3a;
    --gold:   #c9a84c;
    --gold2:  #e8c96a;
    --cream:  #f5f0e8;
    --muted:  #8a9bb5;
    --border: rgba(201,168,76,0.25);
    --card:   rgba(255,255,255,0.04);
}

#MainMenu, footer, header { visibility: hidden; }
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"],
[data-testid="stVerticalBlock"] {
    background: var(--navy) !important;
}
.block-container, [data-testid="stMainBlockContainer"] {
    padding: 0 !important;
    max-width: 100% !important;
}

.page {
    min-height: 100vh;
    background:
        radial-gradient(ellipse at 20% 0%, rgba(201,168,76,0.08) 0%, transparent 55%),
        radial-gradient(ellipse at 80% 100%, rgba(201,168,76,0.05) 0%, transparent 50%),
        linear-gradient(160deg, #0b1f3a 0%, #091729 60%, #0d2040 100%);
    padding: 0 0 80px;
}
.top-stripe {
    height: 4px;
    background: linear-gradient(90deg, transparent, var(--gold), var(--gold2), var(--gold), transparent);
}
.site-header {
    text-align: center;
    padding: 56px 40px 48px;
}
.site-header::after {
    content: '';
    display: block;
    margin: 36px auto 0;
    width: 80px;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
}
.institute-badge {
    display: inline-block;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.35em;
    text-transform: uppercase;
    color: var(--gold);
    border: 1px solid var(--border);
    padding: 6px 20px;
    border-radius: 2px;
    margin-bottom: 28px;
    background: rgba(201,168,76,0.06);
}
.institute-name {
    font-family: 'Playfair Display', serif;
    font-size: clamp(26px, 4vw, 52px);
    font-weight: 900;
    color: #f0e9d6;
    line-height: 1.15;
    letter-spacing: -0.01em;
    margin-bottom: 14px;
    text-shadow: 0 2px 40px rgba(201,168,76,0.15);
}
.dept-name {
    font-family: 'DM Sans', sans-serif;
    font-size: clamp(14px, 2vw, 20px);
    font-weight: 300;
    color: var(--muted);
    letter-spacing: 0.06em;
}
.dept-name span { color: var(--gold); font-weight: 500; }

.section-label {
    text-align: center;
    margin: 8px 0 40px;
}
.section-label p {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: var(--muted);
    position: relative;
    display: inline-block;
}
.section-label p::before,
.section-label p::after {
    content: '';
    position: absolute;
    top: 50%;
    width: 60px;
    height: 1px;
    background: var(--border);
}
.section-label p::before { right: calc(100% + 16px); }
.section-label p::after  { left:  calc(100% + 16px); }

.cards-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 22px;
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 40px;
}
@media (max-width: 860px) { .cards-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 560px) { .cards-grid { grid-template-columns: 1fr; } }
.cards-grid .app-card:nth-child(4) { grid-column: 1; }
.cards-grid .app-card:nth-child(5) { grid-column: 2; }

.app-card {
    background: var(--card);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 32px 28px 28px;
    position: relative;
    overflow: hidden;
    transition: transform 0.28s ease, border-color 0.28s ease, box-shadow 0.28s ease;
    animation: fadeUp 0.5s ease both;
    text-decoration: none !important;
    display: block;
    cursor: pointer;
}
.app-card:nth-child(1) { animation-delay: 0.05s; }
.app-card:nth-child(2) { animation-delay: 0.12s; }
.app-card:nth-child(3) { animation-delay: 0.19s; }
.app-card:nth-child(4) { animation-delay: 0.26s; }
.app-card:nth-child(5) { animation-delay: 0.33s; }

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(24px); }
    to   { opacity: 1; transform: translateY(0); }
}

.app-card::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
    opacity: 0;
    transition: opacity 0.28s;
}
.app-card:hover {
    transform: translateY(-6px);
    border-color: var(--border);
    box-shadow: 0 20px 60px rgba(0,0,0,0.4), 0 0 0 1px rgba(201,168,76,0.1);
}
.app-card:hover::before { opacity: 1; }

.card-number {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    font-weight: 900;
    color: rgba(201,168,76,0.12);
    line-height: 1;
    margin-bottom: 16px;
    transition: color 0.28s;
}
.app-card:hover .card-number { color: rgba(201,168,76,0.22); }
.card-icon { font-size: 2rem; margin-bottom: 14px; display: block; }
.card-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.15rem;
    font-weight: 700;
    color: #e8e0d0;
    margin-bottom: 8px;
    line-height: 1.3;
}
.card-desc {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.82rem;
    font-weight: 300;
    color: var(--muted);
    line-height: 1.6;
    margin-bottom: 22px;
}
.card-link {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--gold);
    text-decoration: none;
    transition: gap 0.22s;
}
.card-arrow { display: inline-block; transition: transform 0.22s; }
.app-card:hover .card-arrow { transform: translateX(4px); }

.site-footer {
    text-align: center;
    margin-top: 64px;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.65rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: rgba(138,155,181,0.45);
}
</style>
""", unsafe_allow_html=True)

APPS = [
    {
        "number": "01",
        "icon": "🔬",
        "title": "MotionIQ",
        "desc": "AI-powered human action recognition for rehabilitation monitoring and sports biomechanics analysis.",
        "url": "https://your-app-1.streamlit.app",
    },
    {
        "number": "02",
        "icon": "🧠",
        "title": "MindMap AI",
        "desc": "Natural language processing tool for extracting key concepts and generating visual knowledge graphs.",
        "url": "https://your-app-2.streamlit.app",
    },
    {
        "number": "03",
        "icon": "📊",
        "title": "DataViz Studio",
        "desc": "Interactive data visualization dashboard for exploring and presenting complex datasets with ease.",
        "url": "https://your-app-3.streamlit.app",
    },
    {
        "number": "04",
        "icon": "🌐",
        "title": "NetGuard",
        "desc": "Real-time network intrusion detection system powered by machine learning anomaly detection.",
        "url": "https://your-app-4.streamlit.app",
    },
    {
        "number": "05",
        "icon": "💬",
        "title": "SentiScope",
        "desc": "Sentiment analysis engine for social media streams with live emotion tracking and reporting.",
        "url": "https://your-app-5.streamlit.app",
    },
]

st.markdown('<div class="page">', unsafe_allow_html=True)
st.markdown('<div class="top-stripe"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="site-header">
  <div class="institute-badge">Est. 1952 &nbsp;·&nbsp; Indore, India</div>
  <div class="institute-name">Shri Govindram Seksaria<br>Institute of Technology &amp; Science</div>
  <div class="dept-name">Department of <span>Information Technology</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-label"><p>Student Project Showcase</p></div>', unsafe_allow_html=True)

cards_html = '<div class="cards-grid">'
for app in APPS:
    cards_html += f"""
    <a class="app-card" href="{app['url']}" target="_blank" rel="noopener noreferrer">
      <div class="card-number">{app['number']}</div>
      <span class="card-icon">{app['icon']}</span>
      <div class="card-title">{app['title']}</div>
      <div class="card-desc">{app['desc']}</div>
      <span class="card-link">Launch App <span class="card-arrow">&#8594;</span></span>
    </a>
    """
cards_html += '</div>'
st.markdown(cards_html, unsafe_allow_html=True)

st.markdown("""
<div class="site-footer">
  &copy; 2026 &nbsp;·&nbsp; SGSITS &nbsp;·&nbsp; Department of Information Technology
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
