import sounddevice as sd
import queue
import json
import time
import re
from vosk import Model, KaldiRecognizer
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
from langchain_groq import ChatGroq

# Load Vosk model
model_path = "vosk-model"
model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

# Initialize AI model
api_key = "get your own api lol😛"  
llm = ChatGroq(groq_api_key=api_key, model_name="llama3-8b-8192")

# Audio queue for speech processing
q = queue.Queue()
speaking = False  # Prevents listening while speaking

def callback(indata, frames, time, status):
    if status:
        print(status)
    if not speaking:  # Only process audio when not speaking
        q.put(bytes(indata))

def clean_text(text):
    """ Remove punctuation from text for natural speech output. """
    return re.sub(r"[^\w\s]", "", text)

def speak(text):
    """ Convert text to speech and play it. """
    global speaking
    speaking = True  

    text = clean_text(text)  # Remove unwanted symbols
    print("Speaking:", text)

    tts = gTTS(text=text, lang='en')
    audio_data = BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)

    # Play speech
    audio_segment = AudioSegment.from_file(audio_data, format="mp3")
    play(audio_segment)

    speaking = False  

def get_ai_response(query):
    """ Get AI response that is naturally 20 words or less. """
    response = llm.invoke(f"Answer in 20 words or less: {query}")
    clean_response = response.content.strip()
    
    # Ensure the response is actually ≤ 20 words
    words = clean_response.split()
    if len(words) > 20:
        clean_response = " ".join(words[:20])  # Trim if needed

    return clean_response

def speech_to_text():
    """ Main function to listen, process speech, and respond with AI output. """
    global speaking
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("Listening...")

        while True:
            if speaking:  # Don't process new input while speaking
                time.sleep(0.1)
                continue

            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                user_query = result["text"].strip()

                if user_query:  # Only process if something was said
                    print("You asked:", user_query)
                    ai_response = get_ai_response(user_query)
                    print("AI response:", ai_response)
                    speak(ai_response)  # Speak the AI response

                    print("Listening again...")  # Ready for next input

if __name__ == "__main__":
    speech_to_text()
