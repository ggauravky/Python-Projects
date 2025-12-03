<div align="center">

# 🐍 Python Projects Collection

![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Projects](https://img.shields.io/badge/Projects-5-orange?style=for-the-badge)

_A curated collection of innovative Python projects showcasing AI, web development, automation, and data management_

[🚀 Getting Started](#-getting-started) • [📂 Projects](#-projects-overview) • [⭐ Star This Repo](#-support)

</div>

---

## 📂 Projects Overview

| #   | Project                      | Tech Stack                                       | Description                                                              |
| --- | ---------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------ |
| 1   | **🎬 AI Reel Studio**        | Flask, FFmpeg, ElevenLabs API, HTML/CSS/JS       | Web app to create AI-powered video reels from images with text-to-speech |
| 2   | **📚 PDF to Audiobook**      | PyPDF2, pyttsx3, gTTS, tkinter                   | Convert PDF documents into audiobooks (MP3 or real-time speech)          |
| 3   | **🤖 JARVIS AI**             | SpeechRecognition, pyttsx3, Wikipedia API, pycaw | Voice-controlled AI assistant for system control, web searches & more    |
| 4   | **🏪 Grocery Store Manager** | Flask, MySQL, Bootstrap, jQuery, REST API        | Full-stack inventory & order management system with modern UI            |
| 5   | **📸 Instagram Scraper**     | Instaloader                                      | Fetch profile stats, bio, and download profile pictures from Instagram   |

---

## 🚀 Getting Started

### Prerequisites

```bash
# Ensure Python 3.7+ is installed
python --version

# Clone the repository
git clone https://github.com/ggauravky/Python-Projects.git
cd Python-Projects
```

### Quick Setup

Each project has its own directory with a simple setup process:

```bash
# Example: Navigate to any project
cd "001 AI Reel-Studio"

# Install dependencies
pip install -r requirements.txt  # or use pip install commands in project sections

# Run the project
python main.py
```

---

## 💡 Featured Projects

### 🎬 AI Reel Studio

Transform images into engaging video reels with AI voiceovers powered by ElevenLabs.

**Key Features:** Multi-image upload • AI text-to-speech • Auto video generation • Gallery view

**Setup:**

```bash
cd "001 AI Reel-Studio"
pip install flask werkzeug requests
# Add your ElevenLabs API key to config.py
python main.py
```

---

### 📚 PDF to Audiobook Converter

Convert any PDF into an audiobook with real-time speech or MP3 export.

**Key Features:** PDF text extraction • Real-time TTS • MP3 export • GUI file selector

**Setup:**

```bash
cd "002 PDF_to_Audio_Book_using_Python"
pip install PyPDF2 pyttsx3 gTTS
python main.py
```

---

### 🤖 JARVIS AI Assistant

Your personal voice-controlled AI assistant for system control and web automation.

**Key Features:** Voice commands • Wikipedia search • Music player • System control • Note-taking

**Popular Commands:**

- `"Wikipedia [topic]"` - Get Wikipedia summaries
- `"Play music"` - Play random songs
- `"Lock"` - Lock your computer
- `"Volume up/down"` - Control audio

**Setup:**

```bash
cd "003 JARVIS AI"
pip install pyttsx3 SpeechRecognition wikipedia-api pycaw comtypes
python main.py
```

---

### 🏪 Grocery Store Management System

Full-stack web application for inventory and order management with MySQL backend.

**Key Features:** Product CRUD • Order management • RESTful API • Responsive UI

**API Endpoints:**

- `GET /getProducts` - List all products
- `POST /insertOrder` - Create new order
- `GET /getAllOrders` - View orders

**Setup:**

```bash
cd "004 Grocery Store Application"
pip install flask flask-cors mysql-connector-python
mysql -u root -p < database_setup.sql
python backend/server.py
```

---

### 📸 Instagram Account Details Fetcher

Retrieve profile stats and download profile pictures from public Instagram accounts.

**Key Features:** Profile stats • Follower count • Bio extraction • Profile picture download

**Setup:**

```bash
cd "005 Get Instagram Account Details"
pip install instaloader
python main.py
```

---

## 🛠️ Tech Stack Overview

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

</div>

---

## 📋 Requirements

- **Python:** 3.7 or higher
- **pip:** Latest version
- **Additional:** MySQL (for Grocery Store project), FFmpeg (for AI Reel Studio)

---

## 👨‍💻 Author

<div align="center">

**Gaurav Kumar**

[![GitHub](https://img.shields.io/badge/GitHub-@ggauravky-181717?style=for-the-badge&logo=github)](https://github.com/ggauravky)

</div>

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests

---

## ⭐ Support

If you find these projects helpful, please consider giving this repository a star!

<div align="center">

[![Star](https://img.shields.io/github/stars/ggauravky/Python-Projects?style=social)](https://github.com/ggauravky/Python-Projects)

---

**Made with ❤️ by Gaurav Kumar**

_Last Updated: December 2025_

</div>
