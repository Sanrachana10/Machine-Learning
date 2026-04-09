import streamlit as st

st.set_page_config(
    page_title="SGSITS Lab Exhibition 2026",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 1. CLEANED CSS (Removed comments and extra whitespace)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=JetBrains+Mono&display=swap');
    :root {
        --primary: #10b981;
        --bg: #0f172a;
        --card-bg: rgba(30, 41, 59, 0.6);
        --border: rgba(16, 185, 129, 0.2);
    }
    .stApp { background-color: var(--bg); font-family: 'Syne', sans-serif; }
    .block-container { padding: 40px 60px !important; }
    header, footer { visibility: hidden; }
    .showcase-header { text-align: center; margin-bottom: 60px; }
    .dept-name { font-size: 3rem; font-weight: 800; color: white; margin-bottom: 10px; }
    .cards-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; }
    .pcard {
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-radius: 20px;
        padding: 30px;
        transition: 0.3s;
        height: 100%;
        display: flex;
        flex-direction: column;
        text-decoration: none !important;
    }
    .pcard:hover { transform: translateY(-8px); border-color: var(--primary); background: rgba(30, 41, 59, 0.9); }
    .card-icon { font-size: 2rem; margin-bottom: 15px; }
    .card-title { font-size: 1.3rem; font-weight: 700; color: white; margin-bottom: 10px; }
    .card-desc { color: #94a3b8; font-size: 0.85rem; line-height: 1.5; margin-bottom: 20px; flex-grow: 1; }
    .card-link { font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: var(--primary); text-transform: uppercase; }
</style>
""", unsafe_allow_html=True)

# 2. HEADER
st.markdown("""
<div class="showcase-header">
    <div class="dept-name">Department of Information Technology</div>
    <div style="color:#10b981; font-weight:700; letter-spacing:0.1em;">SGSITS LAB EXHIBITION 2026</div>
</div>
""", unsafe_allow_html=True)

# 3. CONSOLIDATED CARDS (Crucial: Keep the string "tight" to avoid text-bleeding)
st.markdown("""
<div class="cards-grid">
    <a href="https://machine-failure-predictor-h28hyojxcxoxon5fybywcd.streamlit.app/" target="_blank" style="text-decoration:none;">
        <div class="pcard">
            <div class="card-icon">⚙️</div>
            <div class="card-title">Machine Failure Prediction</div>
            <div class="card-desc">Industrial IoT monitoring using the AI4I 2020 dataset to predict CNC sensor anomalies and tool wear.</div>
            <div class="card-link">Launch Analysis →</div>
        </div>
    </a>
    <a href="https://kth-action-recognition-sclujdd3svncxzmjgcduaj.streamlit.app/" target="_blank" style="text-decoration:none;">
        <div class="pcard">
            <div class="card-icon">⚡</div>
            <div class="card-title">KTH Action Recognition</div>
            <div class="card-desc">Spatiotemporal deep learning model for real-time human action classification (Boxing, Walking, Running).</div>
            <div class="card-link">Launch Neural System →</div>
        </div>
    </a>
    <a href="https://predictor-8c5xjsvmo49exmvyml53fk.streamlit.app/" target="_blank" style="text-decoration:none;">
        <div class="pcard">
            <div class="card-icon">🎓</div>
            <div class="card-title">Placement Predictor</div>
            <div class="card-desc">Analyzing engineering student records including CGPA and internships to forecast career outcomes.</div>
            <div class="card-link">Launch Predictor →</div>
        </div>
    </a>
    <a href="#" style="text-decoration:none;">
        <div class="pcard">
            <div class="card-icon">😊</div>
            <div class="card-title">Smile Detector Model</div>
            <div class="card-desc">Computer Vision application for facial expression analysis and real-time happiness tracking.</div>
            <div class="card-link">Deploy Vision →</div>
        </div>
    </a>
    <a href="#" style="text-decoration:none;">
        <div class="pcard">
            <div class="card-icon">🎙️</div>
            <div class="card-title">Sanskrit Transcription</div>
            <div class="card-desc">Automated Speech Recognition (ASR) tailored for low-resource Sanskrit audio datasets.</div>
            <div class="card-link">Launch Transcription →</div>
        </div>
    </a>
</div>
""", unsafe_allow_html=True)
