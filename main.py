import speech_recognition as sr
import translators as ts

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)

# Recognize the spoken text
try:
    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")
    translatedtext = ts.translate_text(text, translator = 'google', from_language = 'auto', to_language = 'fr')
    print(f"Translation: {translatedtext}")

except sr.UnknownValueError:
    print("Sorry, I could not understand your audio.")

except sr.RequestError as e:
    print(f"Sorry, an error occurred: {str(e)}")