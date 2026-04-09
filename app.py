import streamlit as st

st.set_page_config(
    page_title="SGSITS — Department of IT",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── CSS AND GLOBAL STYLING ──
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">

<style>
/* Hide default Streamlit elements */
#MainMenu, footer, header { visibility: hidden !important; }
.stApp { background: #0b1f3a !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* Main Wrapper */
.showcase-wrapper {
    min-height: 100vh; 
    background: radial-gradient(ellipse at 20% 0%, rgba(201,168,76,0.08) 0%, transparent 55%), 
                radial-gradient(ellipse at 80% 100%, rgba(201,168,76,0.05) 0%, transparent 50%), 
                linear-gradient(160deg,#0b1f3a 0%,#091729 60%,#0d2040 100%); 
    padding-bottom: 80px; 
    font-family: 'DM Sans', sans-serif;
}

/* Card Grid Layout */
.project-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 22px;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 40px;
}

/* Card Styling */
.project-card {
    cursor: pointer;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.09);
    border-radius: 14px;
    padding: 32px 28px 28px;
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
}

.project-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 60px rgba(0,0,0,0.4);
    border-color: rgba(201,168,76,0.35);
}

.card-number {
    font-family: 'Playfair Display', serif;
    font-size: 2.8rem;
    font-weight: 900;
    color: rgba(201,168,76,0.13);
    line-height: 1;
    margin-bottom: 14px;
}

.card-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.25rem;
    font-weight: 700;
    color: #e8e0d0;
    margin-bottom: 8px;
}

.card-desc {
    font-size: 0.85rem;
    font-weight: 300;
    color: #8a9bb5;
    line-height: 1.6;
    margin-bottom: 22px;
    flex-grow: 1;
}

.launch-btn {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #c9a84c;
}
</style>

<div class="showcase-wrapper">
  <div style="height:4px; background:linear-gradient(90deg,transparent,#c9a84c,#e8c96a,#c9a84c,transparent);"></div>

  <div style="text-align:center; padding:56px 40px 48px;">
    <div style="display:inline-block; font-size:0.65rem; font-weight:600; letter-spacing:0.35em; text-transform:uppercase; color:#c9a84c; border:1px solid rgba(201,168,76,0.25); padding:6px 20px; border-radius:2px; margin-bottom:28px; background:rgba(201,168,76,0.06);">
      Est. 1952 &nbsp;·&nbsp; Indore, India
    </div>
    <div style="font-family:'Playfair Display',serif; font-size:clamp(28px, 5vw, 52px); font-weight:900; color:#f0e9d6; line-height:1.15; margin-bottom:14px;">
      Shri Govindram Seksaria<br>Institute of Technology & Science
    </div>
    <div style="font-size:clamp(16px, 2.5vw, 20px); font-weight:300; color:#8a9bb5; letter-spacing:0.06em;">
      Department of <span style="color:#c9a84c; font-weight:500;">Information Technology</span>
    </div>
    <div style="width:80px; height:1px; background:linear-gradient(90deg,transparent,#c9a84c,transparent); margin:36px auto 0;"></div>
  </div>

  <div style="text-align:center; margin:0 0 50px;">
    <span style="font-size:0.75rem; font-weight:500; letter-spacing:0.35em; text-transform:uppercase; color:#8a9bb5;">
      ── &nbsp; Student Project Showcase &nbsp; ──
    </span>
  </div>

  <div class="project-grid">

    <div class="project-card" onclick="window.open('https://your-app-1.streamlit.app','_blank')">
      <div class="card-number">01</div>
      <div style="font-size:2rem; margin-bottom:12px;">🔬</div>
      <div class="card-title">MotionIQ</div>
      <div class="card-desc">AI-powered human action recognition for rehabilitation monitoring and sports biomechanics analysis.</div>
      <div class="launch-btn">Launch App &nbsp;→</div>
    </div>

    <div class="project-card" onclick="window.open('https://your-app-2.streamlit.app','_blank')">
      <div class="card-number">02</div>
      <div style="font-size:2rem; margin-bottom:12px;">🧠</div>
      <div class="card-title">MindMap AI</div>
      <div class="card-desc">Natural language processing tool for extracting key concepts and generating visual knowledge graphs.</div>
      <div class="launch-btn">Launch App &nbsp;→</div>
    </div>

    <div class="project-card" onclick="window.open('https://your-app-3.streamlit.app','_blank')">
      <div class="card-number">03</div>
      <div style="font-size:2rem; margin-bottom:12px;">📊</div>
      <div class="card-title">DataViz Studio</div>
      <div class="card-desc">Interactive data visualization dashboard for exploring and presenting complex datasets with ease.</div>
      <div class="launch-btn">Launch App &nbsp;→</div>
    </div>

    <div class="project-card" onclick="window.open('https://your-app-4.streamlit.app','_blank')">
      <div class="card-number">04</div>
      <div style="font-size:2rem; margin-bottom:12px;">🌐</div>
      <div class="card-title">NetGuard</div>
      <div class="card-desc">Real-time network intrusion detection system powered by machine learning anomaly detection.</div>
      <div class="launch-btn">Launch App &nbsp;→</div>
    </div>

    <div class="project-card" onclick="window.open('https://your-app-5.streamlit.app','_blank')">
      <div class="card-number">05</div>
      <div style="font-size:2rem; margin-bottom:12px;">💬</div>
      <div class="card-title">SentiScope</div>
      <div class="card-desc">Sentiment analysis engine for social media streams with live emotion tracking and reporting.</div>
      <div class="launch-btn">Launch App &nbsp;→</div>
    </div>

  </div>

  <div style="text-align:center; margin-top:80px; font-size:0.65rem; letter-spacing:0.2em; text-transform:uppercase; color:rgba(138,155,181,0.4);">
    &copy; 2026 &nbsp;·&nbsp; SGSITS &nbsp;·&nbsp; Department of Information Technology
  </div>

</div>
""", unsafe_allow_html=True)
