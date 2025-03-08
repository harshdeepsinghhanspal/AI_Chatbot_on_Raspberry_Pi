# 🗣️ AI Voice Assistant

An interactive AI-powered voice assistant using **Vosk** for speech recognition, **gTTS** for text-to-speech, and **Langchain + Groq** for AI responses. This assistant listens to your voice, processes your query, and responds with a naturally spoken reply! 🎙️💡

---

## 🚀 Features
- 🎧 **Real-time Speech Recognition** using [Vosk](https://alphacephei.com/vosk/)
- 🤖 **AI-Powered Responses** via [Langchain + Groq](https://groq.com/)
- 🔊 **Text-to-Speech Output** using [gTTS](https://pypi.org/project/gTTS/)
- 🔄 **Continuous Conversation Mode**
- 🧹 **Auto-Cleans Responses** for natural speech output

---

## 📦 Installation

First, clone this repository:
```bash
git clone https://github.com/your-username/ai-voice-assistant.git
cd ai-voice-assistant
```

### 1️⃣ Install Dependencies(--break-system-packages for systemwide installation of packages)
```bash
pip install --break-system-packages sounddevice queue vosk gtts pydub langchain_groq
```

### 2️⃣ Download Vosk Model
Download a Vosk model (e.g., `vosk-model-small-en-us`) and extract it to your project directory.
```bash
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip -d vosk-model
```

### 3️⃣ Set Up Groq API Key
Sign up at [Groq](https://groq.com/) and get an API key. Replace `api_key` in the script with your key.

---

## 🎯 Usage

Simply run the script and start speaking:
```bash
python main.py
```

### How It Works 🛠️
1. 🎙️ **Listens** for speech input
2. 🧠 **Processes** the text using AI
3. 🔊 **Speaks back** a concise response

---

## 📝 Example
**You:** "What is AI?"

**AI Assistant:** "AI is the simulation of human intelligence in machines."

---

## 🔧 Customization
- Adjust `get_ai_response()` to change response length
- Modify `speak()` for different TTS settings
- Use a different Vosk model for better accuracy

---

## 🏆 Contributing
Feel free to submit issues and pull requests to improve the assistant! 😊

---

## 📜 License
This project is licensed under the MIT License.

---

⭐ **If you like this project, give it a star!** ⭐

