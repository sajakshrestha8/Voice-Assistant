import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
  with sr.Microphone() as source:
    print("Adjusting for background noise...")
    recognizer.adjust_for_ambient_noise(source, duration=1)

    print("Listening...speak now!")
    audio = recognizer.listen(source)

  try:
    print("Recognizing...")
    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")
    return text

  except sr.UnknownValueError:
    print("Sorry, I didn't catch that.")
    return None

  except sr.RequestError:
    print("Couldn't connect to google. Check your internet")
    return None

if __name__ == "__main__":
  listen()
