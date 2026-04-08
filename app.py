import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

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
        min-height: 100vh;
    }

    /* Hero section */
    .hero-section {
        text-align: center;
        padding: 3rem 1rem 2rem;
        animation: fadeInUp 1s ease-out;
    }

    .hero-title {
        font-size: clamp(2rem, 6vw, 4rem);
        font-weight: 800;
        background: linear-gradient(135deg, #00ffcc 0%, #00ff88 50%, #00d4ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        text-shadow: 0 0 60px rgba(0, 255, 204, 0.3);
    }

    .hero-subtitle {
        font-size: clamp(1rem, 2.5vw, 1.5rem);
        color: rgba(255, 255, 255, 0.7);
        margin-bottom: 2rem;
    }

    /* Cards container */
    .cards-container {
        display: flex;
        gap: 2rem;
        justify-content: center;
        flex-wrap: wrap;
        padding: 1rem 2rem 3rem;
        max-width: 1400px;
        margin: 0 auto;
    }

    /* Grade cards */
    .grade-card {
        flex: 1;
        min-width: 320px;
        max-width: 500px;
        padding: 3rem 2rem;
        border-radius: 24px;
        text-align: center;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }

    .grade-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        opacity: 0;
        transition: opacity 0.4s ease;
        z-index: 0;
    }

    .grade-card-7 {
        background: linear-gradient(135deg, rgba(0, 255, 204, 0.1) 0%, rgba(0, 255, 204, 0.05) 100%);
        border: 2px solid rgba(0, 255, 204, 0.3);
        box-shadow: 0 10px 40px rgba(0, 255, 204, 0.1);
    }

    .grade-card-7::before {
        background: linear-gradient(135deg, rgba(0, 255, 204, 0.2) 0%, rgba(0, 212, 255, 0.2) 100%);
    }

    .grade-card-7:hover {
        transform: translateY(-8px) scale(1.02);
        border-color: rgba(0, 255, 204, 0.6);
        box-shadow: 0 20px 60px rgba(0, 255, 204, 0.25);
    }

    .grade-card-8 {
        background: linear-gradient(135deg, rgba(0, 255, 136, 0.1) 0%, rgba(0, 255, 136, 0.05) 100%);
        border: 2px solid rgba(0, 255, 136, 0.3);
        box-shadow: 0 10px 40px rgba(0, 255, 136, 0.1);
    }

    .grade-card-8::before {
        background: linear-gradient(135deg, rgba(0, 255, 136, 0.2) 0%, rgba(0, 212, 255, 0.2) 100%);
    }

    .grade-card-8:hover {
        transform: translateY(-8px) scale(1.02);
        border-color: rgba(0, 255, 136, 0.6);
        box-shadow: 0 20px 60px rgba(0, 255, 136, 0.25);
    }

    .grade-card:hover::before {
        opacity: 1;
    }

    .grade-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        position: relative;
        z-index: 1;
        animation: float 3s ease-in-out infinite;
    }

    .grade-card-8 .grade-icon {
        animation-delay: 0.5s;
    }

    .grade-title {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        position: relative;
        z-index: 1;
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
        position: relative;
        z-index: 1;
    }

    .grade-features {
        list-style: none;
        padding: 0;
        margin: 1.5rem 0;
        text-align: left;
        position: relative;
        z-index: 1;
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

    .start-button {
        display: inline-block;
        padding: 1rem 3rem;
        border-radius: 50px;
        font-size: 1.1rem;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.3s ease;
        position: relative;
        z-index: 1;
        margin-top: 1rem;
    }

    .grade-card-7 .start-button {
        background: linear-gradient(135deg, #00ffcc, #00d4ff);
        color: #0a0f1c;
        box-shadow: 0 5px 20px rgba(0, 255, 204, 0.3);
    }

    .grade-card-7 .start-button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 30px rgba(0, 255, 204, 0.5);
    }

    .grade-card-8 .start-button {
        background: linear-gradient(135deg, #00ff88, #00d4ff);
        color: #0a1a0f;
        box-shadow: 0 5px 20px rgba(0, 255, 136, 0.3);
    }

    .grade-card-8 .start-button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 30px rgba(0, 255, 136, 0.5);
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
        animation: fadeInUp 1s ease-out;
        animation-delay: 0.3s;
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

    /* Features grid */
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
        transition: all 0.3s ease;
    }

    .feature-item:hover {
        background: rgba(255, 255, 255, 0.05);
        border-color: rgba(0, 255, 204, 0.3);
        transform: translateY(-5px);
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

    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes float {
        0%, 100% {
            transform: translateY(0);
        }
        50% {
            transform: translateY(-10px);
        }
    }

    /* Particle effect */
    .particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        overflow: hidden;
        z-index: -1;
    }

    .particle {
        position: absolute;
        width: 4px;
        height: 4px;
        background: rgba(0, 255, 204, 0.3);
        border-radius: 50%;
        animation: rise 10s infinite;
    }

    @keyframes rise {
        0% {
            opacity: 0;
            transform: translateY(100vh) scale(0);
        }
        50% {
            opacity: 1;
        }
        100% {
            opacity: 0;
            transform: translateY(-100vh) scale(1);
        }
    }

    /* Full screen presentation */
    .presentation-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 1000;
    }

    .presentation-container iframe {
        width: 100%;
        height: 100%;
        border: none;
    }

    .back-button {
        position: fixed;
        top: 20px;
        left: 20px;
        z-index: 1001;
        padding: 0.75rem 1.5rem;
        background: rgba(0, 0, 0, 0.7);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 50px;
        cursor: pointer;
        font-size: 0.9rem;
        transition: all 0.3s ease;
    }

    .back-button:hover {
        background: rgba(0, 255, 204, 0.2);
        border-color: rgba(0, 255, 204, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# Get URL parameters to show presentation
url_params = st.query_params
show_presentation = url_params.get("show", None)

# If showing presentation, display it full screen
if show_presentation:
    grade_num = url_params.get("grade", "7")

    st.markdown("""
    <button class="back-button" onclick="history.back()">← 返回选择</button>
    """, unsafe_allow_html=True)

    html_file = f"{'七' if grade_num == '7' else '八'}年级信息技术复习提纲_增强版.html"

    # Read HTML file
    html_path = Path(html_file)
    if html_path.exists():
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Display the HTML
        components.html(html_content, height=1000, scrolling=True)
    else:
        st.error(f"文件未找到: {html_file}")

# Landing page
else:
    # Hero section
    st.markdown("""
    <div class="particles">
        <div class="particle" style="left: 10%; animation-delay: 0s;"></div>
        <div class="particle" style="left: 20%; animation-delay: 2s;"></div>
        <div class="particle" style="left: 30%; animation-delay: 4s;"></div>
        <div class="particle" style="left: 40%; animation-delay: 1s;"></div>
        <div class="particle" style="left: 50%; animation-delay: 3s;"></div>
        <div class="particle" style="left: 60%; animation-delay: 5s;"></div>
        <div class="particle" style="left: 70%; animation-delay: 2.5s;"></div>
        <div class="particle" style="left: 80%; animation-delay: 1.5s;"></div>
        <div class="particle" style="left: 90%; animation-delay: 4.5s;"></div>
    </div>

    <div class="hero-section">
        <div class="hero-title">📚 信息技术复习提纲</div>
        <div class="hero-subtitle">八年级期末考试 · 互动式学习平台</div>
    </div>
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
        <div class="grade-card grade-card-7" onclick="window.open('?show=1&grade=7', '_self')">
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
            <div class="start-button">开始复习 →</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="grade-card grade-card-8" onclick="window.open('?show=1&grade=8', '_self')">
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
            <div class="start-button">开始复习 →</div>
        </div>
        """, unsafe_allow_html=True)

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
