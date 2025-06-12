# Voice-Transulation-Bot
A Real-Time Voice Translation Web App with WhatsApp-Style Chat UI
This project is a Flask-based voice translator chatbot that enables users to speak into the microphone, transcribe the speech to text, translate the text into various Indian languages, and then play back the translated audio — all in a clean, mobile-messenger-style interface inspired by WhatsApp.
🚀 Features

    🎤 Voice Recording: Speak naturally to the app using your system microphone.

    📝 Speech-to-Text: Uses Google’s speech recognition to transcribe your voice.

    🌍 Language Translation: Translates your spoken text into a selected Indian language (Hindi, Telugu, Tamil, Malayalam, Kannada, English).

    🔊 Text-to-Speech: Plays back the translated text as audio using Google TTS.

    💬 WhatsApp-like Chat UI: Clean, intuitive chat interface for seamless interaction.

    🖥️ Responsive Web App: Works on desktops and adapts well to smaller screens.

🧑‍💻 Technologies Used

    Backend: Python, Flask

    Voice Recognition: speech_recognition, Google Web Speech API

    Translation: googletrans

    Text-to-Speech: gTTS (Google Text-to-Speech)

    Audio Recording: pyaudio, keyboard

    Frontend: HTML, CSS (custom), responsive layout with WhatsApp-style chat bubbles

🛠 Use Case

This app can be used for:

    Real-time multilingual communication

    Practicing language learning

    Accessibility tools for the hearing or speech-impaired

    Localizing simple chatbot responses in native Indian languages

🧪 How It Works

    The user selects a language and clicks Start Recording.

    The app records audio from the microphone.

    Upon pressing Stop, the audio is saved and processed.

    The voice is transcribed to text.

    The transcribed text is translated to the selected language.

    Translated text is converted to audio and played in the chat interface.

🌐 Supported Languages

    Hindi 🇮🇳 (hi)

    Telugu 🇮🇳 (te)

    Tamil 🇮🇳 (ta)

    Malayalam 🇮🇳 (ml)

    Kannada 🇮🇳 (kn)

    English 🇬🇧 (en)

**Running of this application**
Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # On Windows: venv\\Scripts\\activate

Install dependencies

pip install -r requirements.txt

Run the Flask app

python app.py

Open in browser
Visit http://127.0.0.1:5000/
