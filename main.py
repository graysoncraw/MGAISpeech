import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)

# Recognize the spoken text
try:
    text = recognizer.recognize_google(audio)
    print(f"You said:{text}")

    # Add logic to execute commands based on recognized text

    if "hello" in text:
        # Execute a command to open a web browser
        print("I heard hello!")

except sr.UnknownValueError:
    print("Sorry, I could not understand your audio.")

except sr.RequestError as e:
    print(f"Sorry, an error occurred: {str(e)}")