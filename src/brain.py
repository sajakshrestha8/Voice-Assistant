import datetime
import webbrowser
import subprocess

# ---Filler words for commands ---
FILLER_WORDS = [
    "please", "open", "can you", "could you", "launch",
    "start", "run", "execute", "hey", "kindly", "would you",
    "will you", "for me", "close", "quit", "kill", "stop"
]

# -----App Dictionary -------- == ENUMS
APPS = {
    "terminal"      : ["gnome-terminal"],
    "files"         : ["nautilus"],
    "file manager"  : ["nautilus"],
    "calculator"    : ["gnome-calculator"],
    "text editor"   : ["gedit"],
    "settings"      : ["gnome-control-center"],
    "vs code"       : ["code"],
    "vscode"        : ["code"],
    "chrome"        : ["google-chrome"],
    "google chrome" : ["google-chrome"],
    "firefox"       : ["firefox"],
    "vlc"           : ["vlc"],
    "spotify"       : ["spotify"],
}

# ----close apps---
CLOSE_APPS = {
    "terminal"      : "gnome-terminal",
    "files"         : "nautilus",
    "file manager"  : "nautilus",
    "calculator"    : "gnome-calculator",
    "text editor"   : "gedit",
    "settings"      : "gnome-control-center",
    "vs code"       : "code",
    "vscode"        : "code",
    "chrome"        : "google-chrome",
    "google chrome" : "google-chrome",
    "firefox"       : "firefox",
    "vlc"           : "vlc",
    "spotify"       : "spotify",
}

def clean_text(text):
    for word in FILLER_WORDS:
        text = text.replace(word, "")
    return text.strip()

# --Function to open app -----
def open_app(command):
  try:
    subprocess.Popen(command)
    return True
  except FileNotFoundError:
    return False

def close_app(command):
  try:
    subprocess.Pkill(["pkill", "-f", command])
    return True
  except Exception:
    return False

def process(text):
  text = text.lower()

  # ---Function to open app ---
  open_triggers = ["open", "launch", "start", "run"]
  if any(trigger in text for trigger in open_triggers):
      app_name = clean_text(text)
      if app_name in APPS:
          success = open_app(APPS[app_name])
          return f"Opening {app_name}!" if success else f"{app_name} is not installed."
      else:
          return f"I don't know how to open {app_name} yet."

  # ---- function to close app ----
  close_triggers = ["close", "quit", "kill", "stop", "exit"]
  if any(trigger in text for trigger in close_triggers):
      # don't exit the assistant itself unless user says bye
      if any(word in text for word in ["bye", "goodbye"]):
          return "Goodbye! Have a great day!"

      app_name = clean_text(text)
      # also remove close trigger words from input
      for word in close_triggers:
          app_name = app_name.replace(word, "").strip()

      if app_name in CLOSE_APPS:
          success = close_app(CLOSE_APPS[app_name])
          return f"Closing {app_name}!" if success else f"Could not close {app_name}."
      else:
          return f"I don't know how to close {app_name} yet."


  if "time" in text:
    time = datetime.datetime.now().strftime("%I:%M %P")
    return f"The current time is {time}"

  elif "date" in text:
        date = datetime.datetime.now().strftime("%B %d, %Y")
        return f"Today is {date}"

  elif "hello" in text or "hi" in text:
      return "Hii! How can I help you?"

  elif "let's play a game" in text:
      return "Thikai xa sathi tmro k xa"

  elif "how are you" in text:
      return "I am fine being the robot. What about you!"

  elif "who are you" in text:
      return "I am your personal voice assistant, you can call me popy!"

  elif "what can you do" in text:
      return "I can have a conversation with you along with some commands on it."

  elif "bye" in text or "exit" in text or "quit" in text or "see you" in text:
      return "Goodbye! Have a great day!"

  elif "open youtube" in text:
      webbrowser.open("https://www.youtube.com")
      return "Opening YouTube!"

  else:
      return "I am not sure how to help with that yet. I am still learning!"

if __name__ == "__main__":
  while True:
    user_input = input("You: ")
    reponse = process(user_input)
    print(f"Assistant: {reponse}")
    if user_input.lower() in ["bye", "exit", "quit", "see you"]:
      break
