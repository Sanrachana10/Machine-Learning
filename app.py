import streamlit as st

# 1. PAGE SETUP
st.set_page_config(
    page_title="SGSITS — Lab Exhibition 2026",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. THEME & ANIMATION CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=JetBrains+Mono&display=swap');

    :root {
        --primary: #10b981;
        --bg-deep: #0f172a;
        --card-bg: rgba(30, 41, 59, 0.6);
        --border: rgba(16, 185, 129, 0.2);
    }

    .stApp {
        background-color: var(--bg-deep);
        background-image: 
            radial-gradient(at 0% 0%, rgba(16, 185, 129, 0.08) 0, transparent 50%), 
            radial-gradient(at 100% 100%, rgba(59, 130, 246, 0.08) 0, transparent 50%);
        font-family: 'Syne', sans-serif;
    }

    .block-container { padding: 60px !important; }
    header, footer { visibility: hidden; }

    /* Centered Header Section */
    .showcase-header {
        text-align: center;
        margin-bottom: 80px;
    }
    
    .college-name {
        font-size: 1.2rem;
        font-weight: 400;
        color: #94a3b8;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-bottom: 10px;
    }
    
    .dept-name {
        font-size: 3.8rem;
        font-weight: 800;
        color: white;
        letter-spacing: -0.04em;
        line-height: 1.1;
        margin-bottom: 25px;
    }

    .exhibit-badge {
        background: rgba(16, 185, 129, 0.1);
        color: var(--primary);
        padding: 8px 24px;
        border-radius: 30px;
        font-size: 0.85rem;
        font-weight: 700;
        border: 1px solid var(--border);
        display: inline-block;
    }

    /* Cards Layout */
    .cards-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 30px;
        max-width: 1200px;
        margin: 0 auto;
    }

    .pcard {
        background: var(--card-bg);
        backdrop-filter: blur(10px);
        border: 1px solid var(--border);
        border-radius: 24px;
        padding: 40px;
        text-decoration: none !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        display: flex;
        flex-direction: column;
        height: 100%;
    }

    .pcard:hover {
        transform: translateY(-12px);
        border-color: var(--primary);
        background: rgba(30, 41, 59, 0.9);
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    }

    .card-icon { font-size: 2.5rem; margin-bottom: 20px; }
    
    .card-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: white;
        margin-bottom: 15px;
        line-height: 1.3;
    }

    .card-desc {
        color: #94a3b8;
        font-size: 0.9rem;
        line-height: 1.6;
        margin-bottom: 30px;
        flex-grow: 1;
    }

    .card-link {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        color: var(--primary);
        text-transform: uppercase;
        letter-spacing: 0.15em;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* Accessibility and functional clean-up */
    a { text-decoration: none !important; }

</style>
""", unsafe_allow_html=True)

# 3. CENTERED HEADER SECTION
st.markdown("""
<div class="showcase-header">
    <div class="college-name">Shri Govindram Seksaria Institute of Technology and Science</div>
    <h1 class="dept-name">Department of<br>Information Technology</h1>
    <div class="exhibit-badge">LAB EXHIBITION 2026</div>
</div>
""", unsafe_allow_html=True)

# 4. UPDATED PROJECT CARDS
# Note: Using standard <a> tags to avoid Streamlit JS blocks.
st.markdown("""
<div class="cards-grid">

    <a href="https://machine-failure-predictor-h28hyojxcxoxon5fybywcd.streamlit.app/" target="_blank">
        <div class="pcard">
            <div class="card-icon">⚙️</div>
            <div class="card-title">Machine Failure Prediction</div>
            <div class="card-desc">Industrial IoT monitoring using the AI4I 2020 dataset to predict CNC sensor anomalies and tool wear.</div>
            <div class="card-link">Launch Analysis →</div>
        </div>
    </a>

    <a href="https://kth-action-recognition-sclujdd3svncxzmjgcduaj.streamlit.app/" target="_blank">
        <div class="pcard">
            <div class="card-icon">⚡</div>
            <div class="card-title">KTH Action Recognition</div>
            <div class="card-desc">Spatiotemporal deep learning model for real-time human action classification (Boxing, Walking, Running).</div>
            <div class="card-link">Launch Neural System →</div>
        </div>
    </a>

    <a href="https://predictor-8c5xjsvmo49exmvyml53fk.streamlit.app/" target="_blank">
        <div class="pcard">
            <div class="card-icon">🎓</div>
            <div class="card-title">Placement Predictor</div>
            <div class="card-desc">Analyzing engineering student records including CGPA and internships to forecast career outcomes.</div>
            <div class="card-link">Launch Predictor →</div>
        </div>
    </a>

    <a href="#" target="_blank">
        <div class="pcard">
            <div class="card-icon">😊</div>
            <div class="card-title">Smile Detector Model</div>
            <div class="card-desc">Computer Vision application for facial expression analysis and real-time happiness index tracking.</div>
            <div class="card-link">Deploy Vision →</div>
        </div>
    </a>

    <a href="#" target="_blank">
        <div class="pcard">
            <div class="card-icon">🎙️</div>
            <div class="card-title">Sanskrit Transcription</div>
            <div class="card-desc">Automated Speech Recognition (ASR) tailored for low-resource Sanskrit audio datasets.</div>
            <div class="card-link">Launch Transcription →</div>
        </div>
    </a>

</div>
""", unsafe_allow_html=True)
