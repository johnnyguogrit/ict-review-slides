import streamlit as st
from pathlib import Path

# Page config
st.set_page_config(
    page_title="信息技术复习提纲",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Enhanced styling
st.markdown("""
<style>
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}

    /* Main container */
    .stApp {
        background: linear-gradient(135deg, #0a0f1c 0%, #1a1f2e 50%, #0a1a0f 100%);
    }

    /* Hero section */
    .hero-title {
        font-size: clamp(2rem, 6vw, 4rem);
        font-weight: 800;
        background: linear-gradient(135deg, #00ffcc 0%, #00ff88 50%, #00d4ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 0 0 60px rgba(0, 255, 204, 0.3);
    }

    .hero-subtitle {
        font-size: clamp(1rem, 2.5vw, 1.5rem);
        color: rgba(255, 255, 255, 0.7);
        text-align: center;
        margin-bottom: 2rem;
    }

    /* Stats section */
    .stats-section {
        display: flex;
        justify-content: center;
        gap: 3rem;
        padding: 2rem;
        flex-wrap: wrap;
    }

    .stat-item {
        text-align: center;
    }

    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #00ffcc, #00ff88);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .stat-label {
        color: rgba(255, 255, 255, 0.6);
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }

    /* Grade cards container */
    .cards-wrapper {
        display: flex;
        gap: 2rem;
        justify-content: center;
        flex-wrap: wrap;
        padding: 1rem;
    }

    /* Grade cards */
    .grade-card {
        min-width: 320px;
        max-width: 450px;
        padding: 3rem 2rem;
        border-radius: 24px;
        text-align: center;
        position: relative;
        overflow: hidden;
    }

    .grade-card-7 {
        background: linear-gradient(135deg, rgba(0, 255, 204, 0.1) 0%, rgba(0, 255, 204, 0.05) 100%);
        border: 2px solid rgba(0, 255, 204, 0.3);
        box-shadow: 0 10px 40px rgba(0, 255, 204, 0.1);
    }

    .grade-card-8 {
        background: linear-gradient(135deg, rgba(0, 255, 136, 0.1) 0%, rgba(0, 255, 136, 0.05) 100%);
        border: 2px solid rgba(0, 255, 136, 0.3);
        box-shadow: 0 10px 40px rgba(0, 255, 136, 0.1);
    }

    .grade-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
    }

    .grade-title {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    .grade-card-7 .grade-title {
        color: #00ffcc;
        text-shadow: 0 0 30px rgba(0, 255, 204, 0.5);
    }

    .grade-card-8 .grade-title {
        color: #00ff88;
        text-shadow: 0 0 30px rgba(0, 255, 136, 0.5);
    }

    .grade-subtitle {
        font-size: 1rem;
        color: rgba(255, 255, 255, 0.6);
        margin-bottom: 1.5rem;
    }

    .grade-features {
        list-style: none;
        padding: 0;
        margin: 1.5rem 0;
        text-align: left;
    }

    .grade-features li {
        padding: 0.5rem 0;
        color: rgba(255, 255, 255, 0.8);
        font-size: 0.95rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }

    .grade-features li:last-child {
        border-bottom: none;
    }

    .grade-features li::before {
        content: "▸";
        color: #00ffcc;
        margin-right: 0.5rem;
    }

    .grade-card-8 .grade-features li::before {
        color: #00ff88;
    }

    /* Streamlit button styling override */
    .stButton > button {
        width: 100%;
        padding: 1rem 3rem;
        border-radius: 50px;
        font-size: 1.1rem;
        font-weight: 600;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        margin-top: 1rem;
    }

    .grade-card-7 .stButton > button {
        background: linear-gradient(135deg, #00ffcc, #00d4ff);
        color: #0a0f1c;
        box-shadow: 0 5px 20px rgba(0, 255, 204, 0.3);
    }

    .grade-card-7 .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 30px rgba(0, 255, 204, 0.5);
    }

    .grade-card-8 .stButton > button {
        background: linear-gradient(135deg, #00ff88, #00d4ff);
        color: #0a1a0f;
        box-shadow: 0 5px 20px rgba(0, 255, 136, 0.3);
    }

    .grade-card-8 .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 30px rgba(0, 255, 136, 0.5);
    }

    /* Features section */
    .features-section {
        max-width: 1000px;
        margin: 0 auto;
        padding: 2rem;
    }

    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin-top: 2rem;
    }

    .feature-item {
        padding: 1.5rem;
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        text-align: center;
    }

    .feature-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }

    .feature-text {
        color: rgba(255, 255, 255, 0.8);
        font-size: 0.9rem;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: rgba(255, 255, 255, 0.4);
        font-size: 0.85rem;
    }

    /* Full height for presentation */
    .fullscreen-html {
        height: calc(100vh - 200px);
    }

    .fullscreen-html iframe {
        height: calc(100vh - 200px) !important;
    }
</style>
""", unsafe_allow_html=True)

# Session state for navigation
if 'current_view' not in st.session_state:
    st.session_state.current_view = 'landing'

# Navigation function
def go_to_landing():
    st.session_state.current_view = 'landing'
    st.rerun()

def go_to_grade7():
    st.session_state.current_view = 'grade7'
    st.rerun()

def go_to_grade8():
    st.session_state.current_view = 'grade8'
    st.rerun()

# Landing Page
if st.session_state.current_view == 'landing':
    # Hero section
    st.markdown("""
    <div class="hero-title">📚 信息技术复习提纲</div>
    <div class="hero-subtitle">八年级期末考试 · 互动式学习平台</div>
    """, unsafe_allow_html=True)

    # Stats
    st.markdown("""
    <div class="stats-section">
        <div class="stat-item">
            <div class="stat-number">13</div>
            <div class="stat-label">单元内容</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">80+</div>
            <div class="stat-label">知识点</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">∞</div>
            <div class="stat-label">练习题</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Grade cards
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="grade-card grade-card-7">
            <div class="grade-icon">📘</div>
            <div class="grade-title">七年级</div>
            <div class="grade-subtitle">互联网与信息处理</div>
            <ul class="grade-features">
                <li>互联网起源与发展趋势</li>
                <li>搜索引擎与信息检索</li>
                <li>网站制作与HTML基础</li>
                <li>网络原理与协议</li>
                <li>互联网创新应用</li>
                <li>网络安全与防范</li>
                <li>人工智能初识</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.button("📘 开始复习", key="btn7", on_click=go_to_grade7)

    with col2:
        st.markdown("""
        <div class="grade-card grade-card-8">
            <div class="grade-icon">📗</div>
            <div class="grade-title">八年级</div>
            <div class="grade-subtitle">物联网技术</div>
            <ul class="grade-features">
                <li>物联网定义与三层架构</li>
                <li>感知层技术 (二维码、RFID)</li>
                <li>网络层 (蓝牙、Wi-Fi、MQTT)</li>
                <li>物联网系统实践</li>
                <li>物联网创新应用</li>
                <li>物联网安全与发展</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.button("📗 开始复习", key="btn8", on_click=go_to_grade8)

    # Features section
    st.markdown("""
    <div class="features-section">
        <h3 style="text-align: center; color: rgba(255,255,255,0.8); margin-bottom: 1rem;">✨ 学习特点</h3>
        <div class="features-grid">
            <div class="feature-item">
                <div class="feature-icon">🎯</div>
                <div class="feature-text">互动测验<br>即时反馈</div>
            </div>
            <div class="feature-item">
                <div class="feature-icon">⌨️</div>
                <div class="feature-text">键盘导航<br>操作便捷</div>
            </div>
            <div class="feature-item">
                <div class="feature-icon">📱</div>
                <div class="feature-text">响应式设计<br>支持移动端</div>
            </div>
            <div class="feature-item">
                <div class="feature-icon">✏️</div>
                <div class="feature-text">编辑模式<br>可自定义内容</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer">
        <p>💡 使用键盘 ↑↓ 箭头键或鼠标滚轮导航 | 按 E 键进入编辑模式</p>
        <p style="margin-top: 0.5rem;">信息技术复习提纲 · 期末备考专用</p>
    </div>
    """, unsafe_allow_html=True)

# Grade 7 Presentation
elif st.session_state.current_view == 'grade7':
    st.button("← 返回选择", on_click=go_to_landing)

    html_file = "七年级信息技术复习提纲_增强版.html"
    html_path = Path(html_file)

    if html_path.exists():
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        st.markdown('<div class="fullscreen-html">', unsafe_allow_html=True)
        st.components.v1.html(html_content, height=1000, scrolling=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error(f"文件未找到: {html_file}")

# Grade 8 Presentation
elif st.session_state.current_view == 'grade8':
    st.button("← 返回选择", on_click=go_to_landing)

    html_file = "八年级信息技术复习提纲_增强版.html"
    html_path = Path(html_file)

    if html_path.exists():
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        st.markdown('<div class="fullscreen-html">', unsafe_allow_html=True)
        st.components.v1.html(html_content, height=1000, scrolling=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error(f"文件未找到: {html_file}")
