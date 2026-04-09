import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SGSITS Lab Exhibition 2026",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit chrome
st.markdown("""
<style>
#MainMenu, footer, header { visibility: hidden !important; }
.stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"],
[data-testid="stMainBlockContainer"], [data-testid="stVerticalBlock"] {
  background: #080c14 !important;
}
.block-container { padding: 0 !important; max-width: 100% !important; }
[data-testid="stMainBlockContainer"] { padding: 0 !important; }
</style>
""", unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Instrument+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { background: #080c14; }

@keyframes fadeUp {
  from { opacity:0; transform:translateY(32px); }
  to   { opacity:1; transform:translateY(0); }
}
@keyframes drift {
  0%,100% { transform: translateY(0) rotate(0deg); }
  33%      { transform: translateY(-18px) rotate(1.5deg); }
  66%      { transform: translateY(8px) rotate(-1deg); }
}
@keyframes shimmer {
  0%   { background-position: -200% center; }
  100% { background-position: 200% center; }
}
@keyframes pulse-ring {
  0%   { transform: scale(0.92); opacity: 0.6; }
  100% { transform: scale(1.12); opacity: 0; }
}
@keyframes scanline {
  0%   { transform: translateY(-100%); }
  100% { transform: translateY(400%); }
}

.page-shell {
  min-height: 100vh;
  background:
    radial-gradient(ellipse 80% 50% at 50% -10%, rgba(56,189,248,0.08) 0%, transparent 60%),
    radial-gradient(ellipse 60% 40% at 90% 90%, rgba(99,102,241,0.06) 0%, transparent 55%),
    radial-gradient(ellipse 50% 60% at 5% 70%, rgba(20,184,166,0.05) 0%, transparent 50%),
    #080c14;
  font-family: 'Instrument Sans', sans-serif;
  overflow-x: hidden;
  padding-bottom: 80px;
}

.grid-bg {
  position: fixed;
  inset: 0;
  background-image:
    linear-gradient(rgba(56,189,248,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(56,189,248,0.03) 1px, transparent 1px);
  background-size: 48px 48px;
  pointer-events: none;
  z-index: 0;
}

.top-bar {
  height: 2px;
  background: linear-gradient(90deg,
    transparent 0%, #0ea5e9 20%, #38bdf8 40%, #67e8f9 50%,
    #38bdf8 60%, #0ea5e9 80%, transparent 100%);
  position: relative;
  z-index: 10;
}

.orb {
  position: fixed;
  border-radius: 50%;
  filter: blur(80px);
  pointer-events: none;
  z-index: 0;
}
.orb-1 {
  width: 500px; height: 500px;
  background: radial-gradient(circle, rgba(14,165,233,0.06) 0%, transparent 70%);
  top: -150px; left: -150px;
  animation: drift 14s ease-in-out infinite;
}
.orb-2 {
  width: 400px; height: 400px;
  background: radial-gradient(circle, rgba(99,102,241,0.05) 0%, transparent 70%);
  bottom: -100px; right: -100px;
  animation: drift 18s ease-in-out infinite reverse;
}

.header-section {
  text-align: center;
  padding: 72px 40px 48px;
  position: relative;
  z-index: 10;
  animation: fadeUp 1s ease both;
}

.institute-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.6rem;
  font-weight: 500;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: #38bdf8;
  border: 1px solid rgba(56,189,248,0.2);
  padding: 6px 20px;
  border-radius: 100px;
  margin-bottom: 28px;
  background: rgba(56,189,248,0.04);
}
.eyebrow-dot {
  width: 5px; height: 5px;
  border-radius: 50%;
  background: #38bdf8;
  animation: pulse-ring 1.8s ease-out infinite;
  box-shadow: 0 0 0 0 rgba(56,189,248,0.4);
}

.college-heading {
  font-family: 'Playfair Display', serif;
  font-size: clamp(28px, 4.5vw, 58px);
  font-weight: 900;
  line-height: 1.1;
  margin-bottom: 12px;
  background: linear-gradient(135deg, #f0f9ff 0%, #bae6fd 40%, #7dd3fc 70%, #f0f9ff 100%);
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: shimmer 4s linear infinite;
  letter-spacing: -0.02em;
}

.dept-subtitle {
  font-size: clamp(13px, 1.6vw, 17px);
  font-weight: 300;
  color: #64748b;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  margin-bottom: 8px;
}
.dept-subtitle strong { color: #94a3b8; font-weight: 500; }

.event-tag {
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.65rem;
  font-weight: 500;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: #0ea5e9;
  margin-top: 18px;
  padding: 5px 16px;
  border: 1px solid rgba(14,165,233,0.25);
  border-radius: 3px;
  background: rgba(14,165,233,0.05);
  position: relative;
  overflow: hidden;
}
.event-tag::after {
  content: '';
  position: absolute;
  top: 0; left: -100%; width: 60%; height: 100%;
  background: linear-gradient(90deg, transparent, rgba(56,189,248,0.15), transparent);
  animation: scanline 2.5s ease-in-out infinite;
}



.section-label {
  text-align: center;
  margin: 0 0 44px;
  position: relative;
  z-index: 10;
  animation: fadeUp 0.8s ease 0.2s both;
}
.section-label-inner {
  display: inline-flex;
  align-items: center;
  gap: 16px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.6rem;
  font-weight: 500;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: #475569;
}
.section-label-inner::before,
.section-label-inner::after {
  content: '';
  width: 60px; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(56,189,248,0.3));
}
.section-label-inner::after {
  background: linear-gradient(90deg, rgba(56,189,248,0.3), transparent);
}

.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
justify-items: center; 
  gap: 20px;
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 40px;
  position: relative;
  z-index: 10;
}

.cards-grid a {
  text-decoration: none !important;
  display: block;
  animation: fadeUp 0.7s ease both;
}
.cards-grid a:nth-child(1) { animation-delay: 0.05s; }
.cards-grid a:nth-child(2) { animation-delay: 0.12s; }
.cards-grid a:nth-child(3) { animation-delay: 0.19s; }
.cards-grid a:nth-child(4) { animation-delay: 0.26s; }
.cards-grid a:nth-child(5) { animation-delay: 0.33s; }

.card-inner {
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid rgba(56,189,248,0.1);
  border-radius: 12px;
  padding: 32px 28px 26px;
  height: 100%;
  position: relative;
  overflow: hidden;
  transition: transform 0.35s cubic-bezier(.22,.68,0,1.2),
              box-shadow 0.35s ease,
              border-color 0.35s ease,
              background 0.35s ease;
  backdrop-filter: blur(12px);
}
.card-inner::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(56,189,248,0.5), transparent);
  transform: scaleX(0);
  transition: transform 0.4s ease;
}
.card-inner::after {
  content: '';
  position: absolute;
  bottom: -60px; right: -60px;
  width: 120px; height: 120px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(56,189,248,0.06) 0%, transparent 70%);
  transition: all 0.4s ease;
}

.cards-grid a:hover .card-inner {
  transform: translateY(-8px);
  box-shadow: 0 24px 60px rgba(0,0,0,0.5), 0 0 0 1px rgba(56,189,248,0.15), inset 0 1px 0 rgba(56,189,248,0.1);
  border-color: rgba(56,189,248,0.25);
  background: rgba(15, 23, 42, 0.9);
}
.cards-grid a:hover .card-inner::before { transform: scaleX(1); }
.cards-grid a:hover .card-inner::after {
  bottom: -30px; right: -30px;
  width: 160px; height: 160px;
}

.card-number {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.65rem;
  font-weight: 500;
  color: rgba(56,189,248,0.35);
  letter-spacing: 0.15em;
  margin-bottom: 16px;
}
.card-icon-wrap {
  font-size: 2rem;
  margin-bottom: 14px;
  display: block;
  filter: drop-shadow(0 0 8px rgba(56,189,248,0.2));
}
.card-title {
  font-family: 'Playfair Display', serif;
  font-size: 1.2rem;
  font-weight: 700;
  color: #e2e8f0;
  margin-bottom: 10px;
  letter-spacing: -0.01em;
  transition: color 0.3s;
}
.cards-grid a:hover .card-title { color: #bae6fd; }
.card-desc {
  font-size: 0.8rem;
  font-weight: 300;
  color: #475569;
  line-height: 1.7;
  margin-bottom: 24px;
}
.card-cta {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.62rem;
  font-weight: 500;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #0ea5e9;
  transition: gap 0.25s ease, color 0.25s;
}
.cards-grid a:hover .card-cta { gap: 14px; color: #38bdf8; }
.card-cta-arrow { transition: transform 0.25s ease; }
.cards-grid a:hover .card-cta-arrow { transform: translateX(4px); }

.corner-tl, .corner-br {
  position: absolute;
  width: 14px; height: 14px;
  transition: all 0.3s ease;
}
.corner-tl {
  top: 10px; left: 10px;
  border-top: 1px solid rgba(56,189,248,0.2);
  border-left: 1px solid rgba(56,189,248,0.2);
}
.corner-br {
  bottom: 10px; right: 10px;
  border-bottom: 1px solid rgba(56,189,248,0.2);
  border-right: 1px solid rgba(56,189,248,0.2);
}
.cards-grid a:hover .corner-tl,
.cards-grid a:hover .corner-br {
  width: 20px; height: 20px;
  border-color: rgba(56,189,248,0.5);
}

.stats-row {
  display: flex;
  justify-content: center;
  gap: 60px;
  margin: 60px auto 0;
  max-width: 600px;
  padding: 32px 40px;
  border-top: 1px solid rgba(56,189,248,0.08);
  border-bottom: 1px solid rgba(56,189,248,0.08);
  position: relative;
  z-index: 10;
  animation: fadeUp 0.8s ease 0.5s both;
}
.stat-item { text-align: center; }
.stat-num {
  font-family: 'Playfair Display', serif;
  font-size: 2rem;
  font-weight: 900;
  color: #38bdf8;
  line-height: 1;
  margin-bottom: 4px;
}
.stat-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.55rem;
  font-weight: 500;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #334155;
}

.page-footer {
  text-align: center;
  margin-top: 52px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.55rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: rgba(71,85,105,0.5);
  position: relative;
  z-index: 10;
}
</style>
</head>
<body>
<div class="page-shell">
  <div class="grid-bg"></div>
  <div class="orb orb-1"></div>
  <div class="orb orb-2"></div>
  <div class="top-bar"></div>

  <div class="header-section">
    <div class="institute-eyebrow">
      <div class="eyebrow-dot"></div>
      Est. 1952 &nbsp;·&nbsp; Indore, Madhya Pradesh
    </div>
    <div class="college-heading">Shri G.S. Institute of Technology &amp; Science</div>
    <div class="dept-subtitle">Department of <strong>Information Technology</strong></div>
    <div class="event-tag">&#9632; Lab Exhibition 2026 &nbsp;·&nbsp; Live</div>
  
   <img src="https://raw.githubusercontent.com/Sanrachana10/Machine-Learning/main/logo.webp"
     style="
       display:block;
       margin:22px auto 0;
       width:140px;
       border-radius:50%;
       background:#080c14;
       padding:6px;
       box-shadow: 0 0 20px rgba(56,189,248,0.35);
     " />
  
  <div class="section-label">
    <div class="section-label-inner">Student Project Showcase</div>
  </div>

  <div class="cards-grid">

    <a href="https://machine-failure-predictor-h28hyojxcxoxon5fybywcd.streamlit.app/" target="_blank">
      <div class="card-inner">
        <div class="corner-tl"></div>
        <div class="corner-br"></div>
        <div class="card-number">// 01</div>
        <span class="card-icon-wrap">⚙️</span>
        <div class="card-title">Machine Failure Prediction</div>
        <div class="card-desc">Industrial IoT monitoring using the AI4I 2020 dataset to predict CNC sensor anomalies and tool wear.</div>
        <div class="card-cta">Launch Analysis <span class="card-cta-arrow">→</span></div>
      </div>
    </a>

    <a href="https://kth-action-recognition-sclujdd3svncxzmjgcduaj.streamlit.app/" target="_blank">
      <div class="card-inner">
        <div class="corner-tl"></div>
        <div class="corner-br"></div>
        <div class="card-number">// 02</div>
        <span class="card-icon-wrap">⚡</span>
        <div class="card-title">KTH Action Recognition</div>
        <div class="card-desc">Spatiotemporal deep learning model for real-time human action classification (Boxing, Walking, Running).</div>
        <div class="card-cta">Launch Neural System <span class="card-cta-arrow">→</span></div>
      </div>
    </a>

    <a href="https://predictor-8c5xjsvmo49exmvyml53fk.streamlit.app/" target="_blank">
      <div class="card-inner">
        <div class="corner-tl"></div>
        <div class="corner-br"></div>
        <div class="card-number">// 03</div>
        <span class="card-icon-wrap">🎓</span>
        <div class="card-title">Placement Predictor</div>
        <div class="card-desc">Analyzing engineering student records including CGPA and internships to forecast career outcomes.</div>
        <div class="card-cta">Launch Predictor <span class="card-cta-arrow">→</span></div>
      </div>
    </a>

    <a href="#" target="_blank">
      <div class="card-inner">
        <div class="corner-tl"></div>
        <div class="corner-br"></div>
        <div class="card-number">// 04</div>
        <span class="card-icon-wrap">😊</span>
        <div class="card-title">Smile Detector Model</div>
        <div class="card-desc">Computer Vision application for facial expression analysis and real-time happiness tracking.</div>
        <div class="card-cta">Deploy Vision <span class="card-cta-arrow">→</span></div>
      </div>
    </a>

    <a href="#" target="_blank">
      <div class="card-inner">
        <div class="corner-tl"></div>
        <div class="corner-br"></div>
        <div class="card-number">// 05</div>
        <span class="card-icon-wrap">🎙️</span>
        <div class="card-title">Sanskrit Transcription</div>
        <div class="card-desc">Automated Speech Recognition (ASR) tailored for low-resource Sanskrit audio datasets.</div>
        <div class="card-cta">Launch Transcription <span class="card-cta-arrow">→</span></div>
      </div>
    </a>

  </div>

  <div class="stats-row">
    <div class="stat-item">
      <div class="stat-num">5</div>
      <div class="stat-label">Projects</div>
    </div>
    <div class="stat-item">
      <div class="stat-num">2026</div>
      <div class="stat-label">Cohort</div>
    </div>
    <div class="stat-item">
      <div class="stat-num">IT</div>
      <div class="stat-label">Department</div>
    </div>
  </div>

  <div class="page-footer">&copy; 2026 &nbsp;·&nbsp; SGSITS &nbsp;·&nbsp; Department of Information Technology</div>
</div>
</body>
</html>
""", height=1200, scrolling=True)
