import speech_recognition as sr

def speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        # Listen for user input
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")

        # Use Google Web Speech API to perform speech recognition
        text = recognizer.recognize_google(audio)

        return text

    except sr.UnknownValueError:
        print("Could not understand audio.")

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# Example usage:
text = speech_to_text()
print("You said:", text)
