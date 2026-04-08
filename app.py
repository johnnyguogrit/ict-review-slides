import streamlit as st
import base64
from pathlib import Path

# Page config
st.set_page_config(
    page_title="信息技术复习提纲",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .stApp { background-color: #0a0f1c; }
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #00ffcc 0%, #ff00aa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 2rem;
    }
    .grade-badge {
        display: inline-block;
        padding: 0.5rem 1.5rem;
        border-radius: 20px;
        font-weight: 600;
        margin: 0.5rem;
    }
    .grade-7 { background: rgba(0, 255, 204, 0.2); color: #00ffcc; border: 1px solid #00ffcc; }
    .grade-8 { background: rgba(0, 255, 136, 0.2); color: #00ff88; border: 1px solid #00ff88; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">📚 信息技术复习提纲</div>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("选择年级")
grade = st.sidebar.radio(
    "年级",
    ["📘 七年级 - 互联网基础", "📗 八年级 - 物联网"],
    label_visibility="collapsed"
)

# Info section
st.sidebar.markdown("---")
st.sidebar.markdown("### 🎯 功能特点")
st.sidebar.markdown("""
- **6-7个单元** 完整覆盖
- **互动测验** 即时反馈
- **键盘导航** ↑↓ 箭头键
- **响应式** 支持手机/平板
""")
st.sidebar.markdown("---")
st.sidebar.markdown("### ⌨️ 快捷键")
st.sidebar.markdown("""
- `↑/↓` - 上一页/下一页
- `空格` - 下一页
- `E` - 编辑模式
- `Home` - 第一页
- `End` - 最后一页
""")

def display_html(file_path, title, description):
    """Display HTML file in iframe"""
    html_file = Path(file_path)

    if not html_file.exists():
        st.error(f"文件不存在: {file_path}")
        return

    # Read and encode HTML
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Encode for iframe
    b64_content = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')

    # Display info
    st.markdown(f"### {title}")
    st.markdown(f"<p style='color: rgba(255,255,255,0.6);'>{description}</p>", unsafe_allow_html=True)

    # Display in iframe
    st.markdown(f"""
    <iframe src="data:text/html;base64,{b64_content}"
            width="100%"
            height="800px"
            style="border: 2px solid rgba(0, 255, 204, 0.3); border-radius: 12px; box-shadow: 0 0 30px rgba(0, 255, 204, 0.1);">
    </iframe>
    """, unsafe_allow_html=True)

# Main content
col1, col2 = st.columns(2)

if "七年级" in grade:
    st.markdown('<span class="grade-badge grade-7">七年级</span>', unsafe_allow_html=True)
    st.markdown("### 互联网与信息处理")
    st.markdown("""
    **涵盖内容:**
    - 互联网起源与发展趋势
    - 搜索引擎与信息检索
    - 网站制作与HTML基础
    - 网络原理与协议
    - 互联网创新应用
    - 网络安全与防范
    - 人工智能初识
    """)

    display_html(
        "七年级信息技术复习提纲_增强版.html",
        "📘 七年级信息技术复习提纲",
        "互联网 · 信息处理 · 网站制作 · 网络原理 · 创新应用 · 安全防范 · 人工智能"
    )

else:  # 八年级
    st.markdown('<span class="grade-badge grade-8">八年级</span>', unsafe_allow_html=True)
    st.markdown("### 物联网技术")
    st.markdown("""
    **涵盖内容:**
    - 物联网定义与三层架构
    - 感知层技术 (二维码、RFID、红外)
    - 网络层技术 (蓝牙、Wi-Fi、MQTT)
    - 物联网系统实践
    - 物联网创新应用
    - 物联网安全与发展
    """)

    display_html(
        "八年级信息技术复习提纲_增强版.html",
        "📗 八年级信息技术复习提纲",
        "物联网架构 · 感知层 · 网络层 · 物联应用 · 安全发展"
    )

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: rgba(255,255,255,0.4); padding: 2rem;'>
    <p>💡 提示: 在演示文稿中使用键盘或鼠标滚轮导航 | 按 E 键进入编辑模式</p>
    <p style='font-size: 0.8rem;'>信息技术复习提纲 · 期末备考专用</p>
</div>
""", unsafe_allow_html=True)
