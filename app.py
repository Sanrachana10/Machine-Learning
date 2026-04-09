import streamlit as st

st.set_page_config(
    page_title="SGSITS — Department of IT",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<div class="cards-grid">

  <a href="https://your-app-1.streamlit.app" target="_blank" style="text-decoration:none; color:inherit;">
    <div class="pcard">
      <div class="card-bg-num">01</div>
      <span class="card-icon">🔬</span>
      <div class="card-title-text">MotionIQ</div>
      <div class="card-desc-text">AI-powered human action recognition for rehabilitation monitoring and sports biomechanics analysis.</div>
      <div class="card-launch">Launch App →</div>
    </div>
  </a>

  <a href="https://your-app-2.streamlit.app" target="_blank" style="text-decoration:none; color:inherit;">
    <div class="pcard">
      <div class="card-bg-num">02</div>
      <span class="card-icon">🧠</span>
      <div class="card-title-text">MindMap AI</div>
      <div class="card-desc-text">Natural language processing tool for extracting key concepts and generating visual knowledge graphs.</div>
      <div class="card-launch">Launch App →</div>
    </div>
  </a>

  <a href="https://your-app-3.streamlit.app" target="_blank" style="text-decoration:none; color:inherit;">
    <div class="pcard">
      <div class="card-bg-num">03</div>
      <span class="card-icon">📊</span>
      <div class="card-title-text">DataViz Studio</div>
      <div class="card-desc-text">Interactive data visualization dashboard for exploring and presenting complex datasets with ease.</div>
      <div class="card-launch">Launch App →</div>
    </div>
  </a>

  <a href="https://your-app-4.streamlit.app" target="_blank" style="text-decoration:none; color:inherit;">
    <div class="pcard">
      <div class="card-bg-num">04</div>
      <span class="card-icon">🌐</span>
      <div class="card-title-text">NetGuard</div>
      <div class="card-desc-text">Real-time network intrusion detection system powered by machine learning anomaly detection.</div>
      <div class="card-launch">Launch App →</div>
    </div>
  </a>

  <a href="https://your-app-5.streamlit.app" target="_blank" style="text-decoration:none; color:inherit;">
    <div class="pcard">
      <div class="card-bg-num">05</div>
      <span class="card-icon">💬</span>
      <div class="card-title-text">SentiScope</div>
      <div class="card-desc-text">Sentiment analysis engine for social media streams with live emotion tracking and reporting.</div>
      <div class="card-launch">Launch App →</div>
    </div>
  </a>

</div>
""", unsafe_allow_html=True)
