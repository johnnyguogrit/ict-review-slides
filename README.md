# 信息技术复习提纲 - Interactive Presentations

Interactive HTML presentations for Grade 7 and Grade 8 ICT exam preparation.

## 🎯 Project Overview

This is a Streamlit web application that hosts interactive HTML presentations for middle school ICT exam preparation. The presentations feature quizzes, keyboard navigation, and responsive design.

## 📚 Content

| Grade | Topics | Units | Quizzes |
|-------|--------|-------|---------|
| **七年级 (Grade 7)** | 互联网基础 | 7 | 28 questions |
| **八年级 (Grade 8)** | 物联网技术 | 6 | 42 questions |

### Grade 7 - 互联网与信息处理
- 互联网起源与发展趋势
- 搜索引擎与信息检索
- 网站制作与HTML基础
- 网络原理与协议 (IP, DNS, TCP/IP)
- 互联网创新应用 (在线学习、协同工作)
- 网络安全与防范
- 人工智能初识

### Grade 8 - 物联网技术
- 物联网定义与三层架构
- 感知层 (二维码、RFID、红外传感、多传感器融合)
- 网络层 (蓝牙、Wi-Fi、MQTT协议)
- 物联网系统实践 (本地/远程/控制应用)
- 物联网创新应用 (健康、交通、农业、医疗)
- 物联网安全与发展

## 🚀 Live Demo

**https://ict-review-slides.streamlit.app**

## 🛠️ Tech Stack

- **Streamlit** - Web framework
- **HTML/CSS/JavaScript** - Presentations
- **Git/GitHub** - Version control

## 📦 Project Structure

```
fontendslide/
├── app.py                              # Streamlit main application
├── requirements.txt                     # Python dependencies
├── 七年级信息技术复习提纲_增强版.html    # Grade 7 presentation
├── 八年级信息技术复习提纲_增强版.html    # Grade 8 presentation
├── 七年级信息技术复习提纲.docx          # Source document
├── 八年级复习提纲.docx                  # Source document
└── README.md                            # This file
```

## 💻 Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```

## 🌐 Deployment

The app is deployed on [Streamlit Community Cloud](https://share.streamlit.io/).

### Deployment Steps
1. Code is pushed to `https://github.com/johnnyguogrit/ict-review-slides`
2. Streamlit Cloud auto-deploys from the `master` branch
3. Main file: `app.py`

### Manual Deployment
1. Go to https://share.streamlit.io
2. Connect GitHub repository
3. Select `johnnyguogrit/ict-review-slides`
4. Main file path: `app.py`

## ✨ Features

### Presentations
- **Keyboard Navigation** - Use ↑↓ arrow keys, spacebar
- **Inline Editing** - Press `E` to toggle edit mode
- **Responsive Design** - Works on mobile, tablet, desktop
- **Progress Tracking** - Visual progress bar and navigation dots
- **Touch Support** - Swipe gestures on mobile devices

### Quizzes
- Interactive multiple-choice questions
- Instant feedback with explanations
- Score tracking and retry options
- 70+ total questions across both grades

## 📝 Usage

1. Open the app
2. Select grade by clicking the card
3. Navigate through slides using:
   - Arrow keys (↑/↓)
   - Spacebar (next slide)
   - Mouse scroll / touch swipe
4. Take quizzes after each unit
5. Press `E` to edit content inline

## 🔄 Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-04-08 | Initial release with Grade 7 & 8 presentations |
| v1.1 | 2026-04-08 | Added landing page with grade selection cards |
| v1.2 | 2026-04-08 | Fixed React onClick error using native Streamlit buttons |

## 📄 License

Educational use only.

## 👤 Author

Created with Claude Code for ICT exam preparation.
