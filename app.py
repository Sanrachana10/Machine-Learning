import streamlit as st

# 1. PAGE SETUP
st.set_page_config(
    page_title="SGSITS — Department of IT Showcase",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. HIGH-IMPACT CSS (Glassmorphism + Hover Effects)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=JetBrains+Mono&display=swap');

    :root {
        --primary: #10b981;
        --bg: #0f172a;
        --card-bg: rgba(30, 41, 59, 0.7);
        --border: rgba(255, 255, 255, 0.1);
    }

    .stApp {
        background-color: var(--bg);
        background-image: 
            radial-gradient(at 0% 0%, rgba(16, 185, 129, 0.1) 0, transparent 50%), 
            radial-gradient(at 100% 100%, rgba(59, 130, 246, 0.1) 0, transparent 50%);
        font-family: 'Inter', sans-serif;
    }

    /* Remove Streamlit whitespace */
    .block-container { padding: 40px 60px !important; }
    header, footer { visibility: hidden; }

    .showcase-header {
        text-align: center;
        margin-bottom: 60px;
    }
    
    .showcase-title {
        font-size: 3.5rem;
        font-weight: 800;
        color: white;
        letter-spacing: -0.03em;
        margin-bottom: 10px;
    }
    
    .showcase-subtitle {
        color: #94a3b8;
        font-size: 1.1rem;
        max-width: 600px;
        margin: 0 auto;
    }

    /* THE CARDS GRID */
    .cards-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 25px;
        perspective: 1000px;
    }

    .pcard {
        background: var(--card-bg);
        backdrop-filter: blur(12px);
        border: 1px solid var(--border);
        border-radius: 20px;
        padding: 35px;
        position: relative;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        height: 100%;
        display: flex;
        flex-direction: column;
        overflow: hidden;
    }

    .pcard:hover {
        transform: translateY(-10px) rotateX(5deg);
        border-color: var(--primary);
        box-shadow: 0 20px 40px rgba(0,0,0,0.4), 0 0 20px rgba(16, 185, 129, 0.2);
    }

    .card-bg-num {
        position: absolute;
        top: -10px;
        right: 10px;
        font-size: 6rem;
        font-weight: 900;
        color: rgba(255,255,255,0.03);
        z-index: 0;
        user-select: none;
    }

    .card-icon {
        font-size: 2.5rem;
        margin-bottom: 20px;
        display: block;
        z-index: 1;
    }

    .card-title-text {
        font-size: 1.5rem;
        font-weight: 700;
        color: white;
        margin-bottom: 12px;
        z-index: 1;
    }

    .card-desc-text {
        color: #94a3b8;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 25px;
        flex-grow: 1;
        z-index: 1;
    }

    .card-launch {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.8rem;
        font-weight: 600;
        color: var(--primary);
        text-transform: uppercase;
        letter-spacing: 0.1em;
        display: flex;
        align-items: center;
        gap: 8px;
        transition: gap 0.3s;
    }

    .pcard:hover .card-launch {
        gap: 15px;
    }

    /* Glowing spot effect on hover */
    .pcard::after {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: radial-gradient(circle at var(--x) var(--y), rgba(16, 185, 129, 0.15), transparent 70%);
        opacity: 0;
        transition: opacity 0.3s;
        pointer-events: none;
    }
    .pcard:hover::after { opacity: 1; }

</style>
""", unsafe_allow_html=True)

# 3. HEADER SECTION
st.markdown("""
<div class="showcase-header">
    <h1 class="showcase-title">Department of IT</h1>
    <p class="showcase-subtitle">Shri Govindram Seksaria Institute of Technology and Science</p>
    <div style="margin-top: 20px;">
        <span style="background: rgba(16,185,129,0.1); color: #10b981; padding: 5px 15px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; border: 1px solid rgba(16,185,129,0.3);">LAB EXHIBITION 2026</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 4. THE CARDS (Natively compatible with Streamlit)
st.markdown("""
<div class="cards-grid">

  <a href="https://your-app-1.streamlit.app" target="_blank" style="text-decoration:none;">
    <div class="pcard">
      <div class="card-bg-num">01</div>
      <span class="card-icon">🔬</span>
      <div class="card-title-text">MotionIQ</div>
      <div class="card-desc-text">AI-powered human action recognition built with ConvLSTM for physical rehabilitation and elder care.</div>
      <div class="card-launch">Explore System →</div>
    </div>
  </a>

  <a href="https://your-app-2.streamlit.app" target="_blank" style="text-decoration:none;">
    <div class="pcard">
      <div class="card-bg-num">02</div>
      <span class="card-icon">🧠</span>
      <div class="card-title-text">MindMap AI</div>
      <div class="card-desc-text">Extracting hierarchical knowledge from dense academic PDFs using Transformer-based NLP.</div>
      <div class="card-launch">Visualize Knowledge →</div>
    </div>
  </a>

  <a href="https://your-app-3.streamlit.app" target="_blank" style="text-decoration:none;">
    <div class="pcard">
      <div class="card-bg-num">03</div>
      <span class="card-icon">📊</span>
      <div class="card-title-text">DataViz Studio</div>
      <div class="card-desc-text">Transforming complex institute datasets into interactive decision-making dashboards.</div>
      <div class="card-launch">View Dashboard →</div>
    </div>
  </a>

  <a href="https://your-app-4.streamlit.app" target="_blank" style="text-decoration:none;">
    <div class="pcard">
      <div class="card-bg-num">04</div>
      <span class="card-icon">🌐</span>
      <div class="card-title-text">NetGuard</div>
      <div class="card-desc-text">Anomaly-based intrusion detection using unsupervised machine learning for campus networks.</div>
      <div class="card-launch">Secure Network →</div>
    </div>
  </a>

  <a href="https://your-app-5.streamlit.app" target="_blank" style="text-decoration:none;">
    <div class="pcard">
      <div class="card-bg-num">05</div>
      <span class="card-icon">💬</span>
      <div class="card-title-text">SentiScope</div>
      <div class="card-desc-text">Multi-language sentiment analysis for social streams with real-time emotion mapping.</div>
      <div class="card-launch">Analyze Sentiments →</div>
    </div>
  </a>

</div>
""", unsafe_allow_html=True)
