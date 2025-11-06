# 🚀 My Python Projects Collection

A curated collection of 5 innovative Python projects showcasing web development, AI integration, automation, and data management. Each project demonstrates practical applications of Python in solving real-world problems.

---

## 📑 Table of Contents

1. [AI Reel Studio](#1-ai-reel-studio)
2. [PDF to Audio Book Converter](#2-pdf-to-audio-book-converter)
3. [JARVIS AI Assistant](#3-jarvis-ai-assistant)
4. [Grocery Store Management System](#4-grocery-store-management-system)
5. [Instagram Account Details Fetcher](#5-instagram-account-details-fetcher)

---

## 1. 🎬 AI Reel Studio

Transform your images and text into engaging video reels with AI-powered voiceovers! This web-based application automatically generates professional-looking short video reels by combining your uploaded images with AI-generated audio narration.

### ✨ Features

- 🌐 **Web-Based Interface**: Clean, intuitive UI for seamless reel creation
- 🖼️ **Multi-Image Upload**: Upload multiple images (PNG, JPG, JPEG) for your reel
- 🎙️ **AI Text-to-Speech**: Powered by ElevenLabs API for natural-sounding voiceovers
- 🎥 **Automatic Video Generation**: Uses FFmpeg to create professional slideshows
- 🎵 **Audio-Video Sync**: Perfectly synchronized audio and visual content
- 📁 **Gallery View**: Browse and manage all your generated reels
- 🔄 **Background Processing**: Non-blocking reel generation with monitoring system

### 🛠️ Technologies Used

- **Python 3.x** - Core programming language
- **Flask** - Web framework for the application
- **FFmpeg** - Video processing and generation
- **ElevenLabs API** - AI-powered text-to-speech
- **HTML/CSS/JavaScript** - Frontend interface

### 📦 Setup and Installation

```bash
# Clone the repository
git clone https://github.com/ggauravky/My-all-Python-Projects-.git

# Navigate to project directory
cd "My-all-Python-Projects-/001 AI Reel-Studio"

# Install required dependencies
pip install flask werkzeug requests

# Create config.py and add your API key
echo "ELEVENLABS_API_KEY = 'YOUR_API_KEY'" > config.py

# Run the main application
python main.py

# In a separate terminal, run the background processor
python generate_process.py
```

### 🚀 Usage

1. Open your browser and navigate to `http://127.0.0.1:5000`
2. Click on "Create Reel" and upload your images
3. Enter your text description for the voiceover
4. Submit and wait for the background process to generate your reel
5. View your completed reels in the "Gallery" section

---

## 2. 📚 PDF to Audio Book Converter

Convert any PDF document into an audiobook! This tool extracts text from PDF files and either reads it aloud in real-time or saves it as an MP3 file for later listening. Perfect for consuming content on-the-go or for accessibility purposes.

### ✨ Features

- 📖 **PDF Text Extraction**: Automatically extracts all readable text from PDF files
- 🗣️ **Real-Time Speech**: Listen to your PDF content immediately using pyttsx3
- 💾 **MP3 Export**: Save audiobooks as MP3 files using Google Text-to-Speech (gTTS)
- 🎯 **Interactive GUI**: Easy file selection with tkinter file dialog
- 📄 **Multi-Page Support**: Processes PDFs of any length automatically
- ✅ **Error Handling**: Validates PDF content and provides clear feedback

### 🛠️ Technologies Used

- **Python 3.x** - Core programming language
- **PyPDF2** - PDF text extraction
- **pyttsx3** - Offline text-to-speech engine
- **gTTS** - Google Text-to-Speech API
- **tkinter** - File selection dialog

### 📦 Setup and Installation

```bash
# Navigate to project directory
cd "My-all-Python-Projects-/002 PDF_to_Audio_Book_using_Python"

# Install required dependencies
pip install PyPDF2 pyttsx3 gTTS

# Run the application
python main.py
```

### 🚀 Usage

1. Run the script: `python main.py`
2. Select your PDF file from the file dialog
3. Choose your preferred option:
   - **Option 1**: Speak the content in real-time
   - **Option 2**: Save as `audiobook.mp3` file
4. Enjoy your audiobook!

---

## 3. 🤖 JARVIS AI Assistant

Your personal AI voice assistant inspired by Iron Man's JARVIS! This intelligent assistant can perform web searches, play music, control your system, take notes, and much more through natural voice commands.

### ✨ Features

- 🎤 **Voice Recognition**: Listens and understands your commands using Google Speech Recognition
- 🗣️ **Voice Responses**: Speaks back to you with natural-sounding voice synthesis
- 🕐 **Smart Greetings**: Contextual greetings based on time of day (morning/afternoon/evening)
- 🌐 **Web Integration**: 
  - Search and read Wikipedia articles
  - Open websites (YouTube, Google, Notion, GitHub)
  - Perform Google and YouTube searches
- 🎵 **Music Player**: Play random songs from your music library
- 📝 **Note Taking**: Remember and recall information on command
- 🖥️ **System Control**:
  - Lock your computer
  - Sleep/Hibernate system
  - Mute/Unmute volume
  - Increase/Decrease volume
- ⏰ **Time Telling**: Ask for the current time
- 💻 **App Launcher**: Open VS Code and other applications

### 🛠️ Technologies Used

- **Python 3.x** - Core programming language
- **pyttsx3** - Text-to-speech conversion
- **speech_recognition** - Voice command recognition
- **wikipedia** - Wikipedia API integration
- **webbrowser** - Web control
- **pycaw** - Windows audio control
- **datetime** - Time and date handling

### 📦 Setup and Installation

```bash
# Navigate to project directory
cd "My-all-Python-Projects-/003 JARVIS AI"

# Install required dependencies
pip install pyttsx3 SpeechRecognition wikipedia-api pycaw comtypes

# Run the application
python main.py
```

### 🚀 Voice Commands

- **"Wikipedia [topic]"** - Search and read Wikipedia articles
- **"Open YouTube/Google/GitHub/Notion"** - Open websites
- **"Play music"** - Play random song from your library
- **"What time is it?"** - Get current time
- **"Remember that [note]"** - Save a note
- **"What do you remember?"** - Recall saved notes
- **"Search on Google [query]"** - Google search
- **"Search on YouTube [query]"** - YouTube search
- **"Lock"** - Lock your computer
- **"Mute/Unmute"** - Control system volume
- **"Volume up/down"** - Adjust volume
- **"Exit/Bye"** - Close JARVIS

---

## 4. 🏪 Grocery Store Management System

A full-stack web application for managing grocery store inventory and orders. Features a modern UI with real-time product management, order processing, and MySQL database integration. Perfect for small to medium-sized grocery stores.

### ✨ Features

- 📊 **Product Management**:
  - View all products with pricing and units
  - Add new products with custom UOM (Unit of Measurement)
  - Update existing product details
  - Delete products from inventory
- 🛒 **Order Management**:
  - Create new orders with multiple products
  - View all orders with customer details
  - View detailed order breakdowns
  - Delete orders when needed
- 📏 **UOM Support**: Multiple units (kg, liter, piece, dozen, gram, ml, packet)
- 🌐 **RESTful API**: Complete backend API with Flask
- 🎨 **Modern UI**: Responsive Bootstrap-based interface
- 💾 **MySQL Database**: Robust data storage with relationships
- 🔄 **CORS Enabled**: Full cross-origin resource sharing support
- ✅ **Health Monitoring**: Built-in health check endpoint

### 🛠️ Technologies Used

**Backend:**
- **Python 3.x** - Server-side programming
- **Flask** - Web framework
- **Flask-CORS** - Cross-origin resource sharing
- **MySQL** - Database management
- **mysql-connector-python** - Database connectivity

**Frontend:**
- **HTML5/CSS3** - Structure and styling
- **JavaScript** - Interactive functionality
- **Bootstrap** - Responsive UI framework
- **jQuery** - DOM manipulation

### 📦 Setup and Installation

```bash
# Navigate to project directory
cd "My-all-Python-Projects-/004 Grocery Store Application"

# Install required dependencies
pip install flask flask-cors mysql-connector-python

# Set up MySQL database
mysql -u root -p < database_setup.sql

# Update database credentials in backend/sql_connection.py
# Edit the connection details:
# - host
# - user
# - password

# Run the Flask server
python backend/server.py

# Open the UI in your browser
# Navigate to the ui folder and open index.html
```

### 🚀 API Endpoints

- `GET /getProducts` - Retrieve all products
- `POST /insertProduct` - Add a new product
- `POST /updateProduct` - Update product details
- `POST /deleteProduct` - Remove a product
- `GET /getUOM` - Get all units of measurement
- `POST /insertOrder` - Create new order
- `GET /getAllOrders` - Retrieve all orders
- `POST /getOrderDetails` - Get specific order details
- `POST /deleteOrder` - Delete an order
- `GET /health` - Health check endpoint

### 📂 Project Structure

```
004 Grocery Store Application/
├── backend/
│   ├── server.py           # Flask API server
│   ├── products_dao.py     # Product database operations
│   ├── orders_dao.py       # Order database operations
│   ├── uom_dao.py          # Unit of measurement operations
│   └── sql_connection.py   # Database connection pool
├── ui/
│   ├── index.html          # Dashboard
│   ├── manage-product.html # Product management
│   ├── order.html          # Order management
│   ├── css/                # Stylesheets
│   └── js/                 # JavaScript files
└── database_setup.sql      # Database schema
```

---

## 5. 📸 Instagram Account Details Fetcher

Quickly retrieve comprehensive information about any public Instagram account! This tool fetches profile statistics, bio information, and downloads profile pictures with just a username. Perfect for social media analysis and research.

### ✨ Features

- 👤 **Profile Information Retrieval**:
  - Username verification
  - Total number of posts
  - Follower count
  - Following count
  - Biography/Bio text
- 🖼️ **Profile Picture Download**: Automatically saves high-quality profile picture
- 🔍 **Public Account Access**: Works with any public Instagram profile
- ⚡ **Fast Processing**: Quick data retrieval using Instaloader library
- 💻 **CLI Interface**: Simple command-line interaction
- 📊 **Formatted Output**: Clean, readable statistics display

![Instagram Profile Fetcher Demo](005%20Get%20Instagram%20Account%20Details/insta1.png)
*Example: Fetching account statistics*

![Profile Picture Download](005%20Get%20Instagram%20Account%20Details/insta2.png)
*Example: Downloaded profile picture*

### 🛠️ Technologies Used

- **Python 3.x** - Core programming language
- **Instaloader** - Instagram scraping library

### 📦 Setup and Installation

```bash
# Navigate to project directory
cd "My-all-Python-Projects-/005 Get Instagram Account Details"

# Install required dependencies
pip install instaloader

# Run the application
python main.py
```

### 🚀 Usage

1. Run the script: `python main.py`
2. Enter the Instagram username when prompted
3. The tool will display:
   - Username
   - Total number of posts
   - Follower count
   - Following count
   - Biography
4. Profile picture will be automatically downloaded to the current directory

### 📊 Example Output

```
Enter username: nasa
Username:  nasa
Number of Posts Uploaded:  6543
nasa is having 98765432 followers.
nasa is following 54 people
Bio:  Exploring the universe and our home planet. 🚀🌍
Profile picture saved!
```

### ⚠️ Important Notes

- Only works with **public** Instagram accounts
- Respects Instagram's rate limits
- For private accounts, you'll need to be logged in
- No authentication required for public profiles

---

## 🎯 General Requirements

All projects require:
- **Python 3.7+**
- **pip** (Python package manager)

## 📝 License

These projects are open-source and available for educational purposes. Feel free to modify and use them in your own projects!

## 👨‍💻 Author

**Gaurav Kumar**
- GitHub: [@ggauravky](https://github.com/ggauravky)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page or submit a pull request.

## ⭐ Support

If you found these projects helpful, please consider giving this repository a star!

---

*Last Updated: November 2025*