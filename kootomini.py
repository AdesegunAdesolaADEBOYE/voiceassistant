import speech_recognition as sr
from gtts import gTTS
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        return user_input.lower()
    except sr.UnknownValueError:
        return None

def respond(text):
    tts = gTTS(text=text, lang='en')
    tts.save('response.mp3')
    os.system('mpg321 response.mp3')

def process_input(user_input):
    if "hello" in user_input:
        respond("Hello! How can I assist you?")
    elif "commercial towns" in user_input:
        # Dummy data for demonstration
        data = {"lagos": ["Rice", "Fish"], "abuja": ["Maize", "Groundnut"]}
        respond(str(data))
    else:
        respond("Sorry, I didn't understand that.")

# Main loop
while True:
    user_input = listen()

    if user_input is not None:
        print("User said:", user_input)
        process_input(user_input)