# 🗣 Google Voice Assistant with Gemini API

## 🚀 Features
- Open Google, YouTube, LinkedIn, Instagram, GitHub, and Facebook with a voice or text command
- Chat with Google Gemini AI for responses in speech and text mode
- Supports both **Text Mode** (manual input) and **Speech Mode** (voice recognition)

---

## 📌 Prerequisites
Before running this project, ensure you have the following installed:

1️⃣ Install Python (if not installed)  
   - [Download Python](https://www.python.org/downloads/)  

2️⃣ Install required Python packages  
   ```sh
   pip install speechrecognition pyttsx3 requests
   ```

3️⃣ Install additional dependencies (for speech recognition)  
   ```sh
   pip install pyaudio
   ```
   - If you face issues installing `pyaudio`, use:  
     ```sh
     pip install pipwin
     pipwin install pyaudio
     ```  

4️⃣ Generate a **Gemini API Key** (if using AI responses)  
   - Visit [Google AI](https://aistudio.google.com/)  
   - Generate an API key and keep it ready  

---

## 🎯 How to Run
1. Select **Text Mode (T) or Speech Mode (S)**
2. If using AI, provide your **Gemini API Key** when prompted
3. Say "**Quit Google**" to exit the assistant  

---

## 🤖 Future Improvements
- Add more website shortcuts  
- Enhance conversation memory  
- Improve speech recognition accuracy  
