import streamlit as st

st.set_page_config(
    page_title="SGSITS — Department of IT",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── CSS AND GLOBAL STYLING ──
st.markdown("""
<div class="project-grid">

  <a href="https://your-app-1.streamlit.app" target="_blank" style="text-decoration:none;">
    <div class="project-card">
      <div class="card-number">01</div>
      <div style="font-size:2rem; margin-bottom:12px;">🔬</div>
      <div class="card-title">MotionIQ</div>
      <div class="card-desc">AI-powered human action recognition for rehabilitation monitoring and sports biomechanics analysis.</div>
      <div class="launch-btn">Launch App →</div>
    </div>
  </a>

  <a href="https://your-app-2.streamlit.app" target="_blank" style="text-decoration:none;">
    <div class="project-card">
      <div class="card-number">02</div>
      <div style="font-size:2rem; margin-bottom:12px;">🧠</div>
      <div class="card-title">MindMap AI</div>
      <div class="card-desc">Natural language processing tool for extracting key concepts and generating visual knowledge graphs.</div>
      <div class="launch-btn">Launch App →</div>
    </div>
  </a>

  <a href="https://your-app-3.streamlit.app" target="_blank" style="text-decoration:none;">
    <div class="project-card">
      <div class="card-number">03</div>
      <div style="font-size:2rem; margin-bottom:12px;">📊</div>
      <div class="card-title">DataViz Studio</div>
      <div class="card-desc">Interactive data visualization dashboard for exploring and presenting complex datasets with ease.</div>
      <div class="launch-btn">Launch App →</div>
    </div>
  </a>

  <a href="https://your-app-4.streamlit.app" target="_blank" style="text-decoration:none;">
    <div class="project-card">
      <div class="card-number">04</div>
      <div style="font-size:2rem; margin-bottom:12px;">🌐</div>
      <div class="card-title">NetGuard</div>
      <div class="card-desc">Real-time network intrusion detection system powered by machine learning anomaly detection.</div>
      <div class="launch-btn">Launch App →</div>
    </div>
  </a>

  <a href="https://your-app-5.streamlit.app" target="_blank" style="text-decoration:none;">
    <div class="project-card">
      <div class="card-number">05</div>
      <div style="font-size:2rem; margin-bottom:12px;">💬</div>
      <div class="card-title">SentiScope</div>
      <div class="card-desc">Sentiment analysis engine for social media streams with live emotion tracking and reporting.</div>
      <div class="launch-btn">Launch App →</div>
    </div>
  </a>

</div>
""", unsafe_allow_html=True)
