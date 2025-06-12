# from flask import Flask, render_template, request
# from gtts import gTTS
# import os
# import time

# app = Flask(__name__)
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     audio_file = None
#     version = str(int(time.time()))  # Used for cache-busting

#     if request.method == 'POST':
#         text = request.form.get('text', '')
#         if text.strip() != "":
#             tts = gTTS(text)
#             audio_rel_path = os.path.join('static', 'output.mp3')
#             audio_abs_path = os.path.join(BASE_DIR, audio_rel_path)
#             tts.save(audio_abs_path)
#             audio_file = audio_rel_path

#     return render_template('index.html', audio_file=audio_file, version=version)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, jsonify, url_for
import os
import wave
import pyaudio
import threading
import time
import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator

# App Setup
app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_FILE = os.path.join(BASE_DIR, 'static', 'recorded.wav')
TTS_FILE = os.path.join(BASE_DIR, 'static', 'translated_audio.mp3')

# PyAudio Config
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

languages = {
    "1": ("te", "Telugu"),
    "2": ("hi", "Hindi"),
    "3": ("ta", "Tamil"),
    "4": ("kn", "Kannada"),
    "5": ("ml", "Malayalam"),
    "6": ("en", "English")
}

stop_recording = False

def record_audio():
    global stop_recording
    stop_recording = False
    frames = []

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("🔴 Recording...")

    try:
        while not stop_recording:
            data = stream.read(CHUNK)
            frames.append(data)
    except Exception as e:
        print("❌ Error:", e)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(AUDIO_FILE, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

def transcribe_audio():
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(AUDIO_FILE) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            return text
    except Exception as e:
        return f"Transcription failed: {e}"

def translate_text(text, target_lang):
    try:
        translator = Translator()
        translated = translator.translate(text, dest=target_lang).text
        return translated
    except Exception as e:
        return f"Translation failed: {e}"

def text_to_speech(text):
    tts = gTTS(text)
    tts.save(TTS_FILE)

@app.route('/', methods=['GET', 'POST'])
def index():
    transcript = ""
    translated = ""
    lang_choice = None
    version = str(int(time.time()))

    if request.method == 'POST':
        lang_key = request.form.get("language")
        lang_code, lang_name = languages.get(lang_key, ("hi", "Hindi"))

        record_audio()

        transcript = transcribe_audio()
        translated = translate_text(transcript, lang_code)
        text_to_speech(translated)

        return render_template("index.html", 
                               transcript=transcript, 
                               translated=translated, 
                               audio_url=url_for('static', filename='translated_audio.mp3') + f"?v={version}", 
                               languages=languages, 
                               selected=lang_key)

    return render_template("index.html", languages=languages)

@app.route('/stop', methods=['POST'])
def stop():
    global stop_recording
    stop_recording = True
    return jsonify({"message": "Recording stopped."})

if __name__ == '__main__':
    app.run(debug=True)