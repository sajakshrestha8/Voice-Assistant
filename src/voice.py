import pyttsx3

engine = pyttsx3.init()

def configure_voice():
  voices = engine.getProperty('voices');
  engine.setProperty('voice', voices[24].id)
  engine.setProperty('rate', 140)
  engine.setProperty('volume', 1.0)

def speak(text):
  configure_voice()
  engine.say(text)
  engine.runAndWait()


if __name__ == "__main__":
  speak("Hello I am voice assistant I am alive")
