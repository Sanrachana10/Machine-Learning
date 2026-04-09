import streamlit as st

st.set_page_config(
    page_title="SGSITS — Department of IT",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600;700&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">

<style>
  #MainMenu, footer, header { visibility: hidden !important; }
  .stApp,
  [data-testid="stAppViewContainer"],
  [data-testid="stAppViewBlockContainer"],
  [data-testid="stMain"],
  [data-testid="stMainBlockContainer"],
  [data-testid="stVerticalBlock"],
  [data-testid="stHorizontalBlock"] {
    background: #f5f2eb !important;
  }
  .block-container { padding: 0 !important; max-width: 100% !important; }
  [data-testid="stMainBlockContainer"] { padding: 0 !important; }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(28px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  @keyframes lineExpand {
    from { width: 0; }
    to   { width: 120px; }
  }
  @keyframes float {
    0%,100% { transform: translateY(0px); }
    50%      { transform: translateY(-6px); }
  }

  .main-wrapper {
    min-height: 100vh;
    background: #f5f2eb;
    background-image:
      radial-gradient(circle at 8% 12%, rgba(139,109,56,0.07) 0%, transparent 40%),
      radial-gradient(circle at 92% 80%, rgba(139,109,56,0.05) 0%, transparent 35%),
      url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%238b6d38' fill-opacity='0.03'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
    font-family: 'Outfit', sans-serif;
    padding-bottom: 80px;
  }

  /* ── TOP STRIPE ── */
  .top-stripe {
    height: 3px;
    background: linear-gradient(90deg, transparent 0%, #8b6d38 20%, #c9a55a 50%, #8b6d38 80%, transparent 100%);
  }

  /* ── HEADER ── */
  .header-wrap {
    text-align: center;
    padding: 64px 40px 32px;
    animation: fadeUp 0.9s ease both;
  }
  .college-badge {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    font-family: 'Outfit', sans-serif;
    font-size: 0.6rem;
    font-weight: 600;
    letter-spacing: 0.38em;
    text-transform: uppercase;
    color: #8b6d38;
    border: 1px solid rgba(139,109,56,0.3);
    padding: 7px 22px;
    border-radius: 2px;
    margin-bottom: 32px;
    background: rgba(139,109,56,0.05);
  }
  .college-name {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(32px, 5vw, 64px);
    font-weight: 700;
    color: #1a1410;
    line-height: 1.12;
    margin-bottom: 14px;
    letter-spacing: -0.01em;
  }
  .dept-name {
    font-size: clamp(13px, 1.8vw, 18px);
    font-weight: 300;
    color: #6b5e4e;
    letter-spacing: 0.12em;
    text-transform: uppercase;
  }
  .dept-name span {
    color: #8b6d38;
    font-weight: 500;
  }
  .divider-line {
    height: 1px;
    width: 120px;
    background: linear-gradient(90deg, transparent, #8b6d38, transparent);
    margin: 32px auto 0;
    animation: lineExpand 1.2s ease 0.4s both;
  }

  /* ── SECTION LABEL ── */
  .section-label {
    text-align: center;
    margin: 48px 0 40px;
    animation: fadeUp 0.9s ease 0.2s both;
  }
  .section-label span {
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.38em;
    text-transform: uppercase;
    color: #9b8b79;
    position: relative;
  }
  .section-label span::before,
  .section-label span::after {
    content: '';
    display: inline-block;
    width: 40px;
    height: 1px;
    background: #c9a55a;
    vertical-align: middle;
    margin: 0 16px;
  }

  /* ── GRID ── */
  .cards-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 40px;
  }

  /* ── CARD ── */
  .pcard {
    background: #fffef9;
    border: 1px solid rgba(139,109,56,0.15);
    border-radius: 4px;
    padding: 36px 30px 30px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    transition: transform 0.32s cubic-bezier(.22,.68,0,1.2), box-shadow 0.32s ease, border-color 0.32s ease;
    animation: fadeUp 0.8s ease both;
  }
  .pcard::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #8b6d38, #c9a55a);
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.38s ease;
  }
  .pcard:hover { transform: translateY(-7px); box-shadow: 0 24px 64px rgba(26,20,16,0.12); border-color: rgba(139,109,56,0.35); }
  .pcard:hover::before { transform: scaleX(1); }

  .pcard:nth-child(1) { animation-delay: 0.1s; }
  .pcard:nth-child(2) { animation-delay: 0.2s; }
  .pcard:nth-child(3) { animation-delay: 0.3s; }
  .pcard:nth-child(4) { animation-delay: 0.4s; }
  .pcard:nth-child(5) { animation-delay: 0.5s; }

  .card-bg-num {
    font-family: 'Cormorant Garamond', serif;
    font-size: 5rem;
    font-weight: 700;
    color: rgba(139,109,56,0.07);
    line-height: 1;
    margin-bottom: 8px;
    letter-spacing: -0.04em;
  }
  .card-icon { font-size: 1.9rem; margin-bottom: 14px; display: block; }
  .card-title-text {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.35rem;
    font-weight: 600;
    color: #1a1410;
    margin-bottom: 10px;
    letter-spacing: 0.01em;
  }
  .card-desc-text {
    font-size: 0.82rem;
    font-weight: 300;
    color: #7a6e64;
    line-height: 1.7;
    margin-bottom: 26px;
  }
  .card-launch {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #8b6d38;
    border-bottom: 1px solid rgba(139,109,56,0.3);
    padding-bottom: 2px;
    transition: gap 0.2s ease, border-color 0.2s ease;
  }
  .pcard:hover .card-launch { gap: 14px; border-color: #8b6d38; }

  /* ── FOOTER ── */
  .footer {
    text-align: center;
    margin-top: 72px;
    font-size: 0.6rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: rgba(107,94,78,0.45);
  }
</style>

<div class="main-wrapper">
  <div class="top-stripe"></div>

  <div class="header-wrap">
    <div class="college-badge">Est. 1952 &nbsp;·&nbsp; Indore, Madhya Pradesh</div>
    <div class="college-name">Shri G.S. Institute of Technology &amp; Science</div>
    <div class="dept-name">Department of <span>Information Technology</span></div>
    <div class="divider-line"></div>
  </div>

  <div class="section-label">
    <span>Student Project Showcase</span>
  </div>

  <div class="cards-grid">

    <div class="pcard" onclick="window.open('https://your-app-1.streamlit.app','_blank')">
      <div class="card-bg-num">01</div>
      <span class="card-icon">🔬</span>
      <div class="card-title-text">MotionIQ</div>
      <div class="card-desc-text">AI-powered human action recognition for rehabilitation monitoring and sports biomechanics analysis.</div>
      <div class="card-launch">Launch App &nbsp;→</div>
    </div>

    <div class="pcard" onclick="window.open('https://your-app-2.streamlit.app','_blank')">
      <div class="card-bg-num">02</div>
      <span class="card-icon">🧠</span>
      <div class="card-title-text">MindMap AI</div>
      <div class="card-desc-text">Natural language processing tool for extracting key concepts and generating visual knowledge graphs.</div>
      <div class="card-launch">Launch App &nbsp;→</div>
    </div>

    <div class="pcard" onclick="window.open('https://your-app-3.streamlit.app','_blank')">
      <div class="card-bg-num">03</div>
      <span class="card-icon">📊</span>
      <div class="card-title-text">DataViz Studio</div>
      <div class="card-desc-text">Interactive data visualization dashboard for exploring and presenting complex datasets with ease.</div>
      <div class="card-launch">Launch App &nbsp;→</div>
    </div>

    <div class="pcard" onclick="window.open('https://your-app-4.streamlit.app','_blank')">
      <div class="card-bg-num">04</div>
      <span class="card-icon">🌐</span>
      <div class="card-title-text">NetGuard</div>
      <div class="card-desc-text">Real-time network intrusion detection system powered by machine learning anomaly detection.</div>
      <div class="card-launch">Launch App &nbsp;→</div>
    </div>

    <div class="pcard" onclick="window.open('https://your-app-5.streamlit.app','_blank')">
      <div class="card-bg-num">05</div>
      <span class="card-icon">💬</span>
      <div class="card-title-text">SentiScope</div>
      <div class="card-desc-text">Sentiment analysis engine for social media streams with live emotion tracking and reporting.</div>
      <div class="card-launch">Launch App &nbsp;→</div>
    </div>

  </div>

  <div class="footer">&copy; 2026 &nbsp;·&nbsp; SGSITS &nbsp;·&nbsp; Department of Information Technology</div>
</div>
""", unsafe_allow_html=True)
