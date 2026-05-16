from speech import listen
from voice import speak
from brain import process

def run():
    speak("Hey sajak! Happy to see you again. How can I help you?")

    while True:
        user_input = listen()

        if user_input:
            print(f"You said: {user_input}")

            response = process(user_input)
            print(f"Assistant: {response}")

            speak(response)

            if any(word in user_input.lower() for word in ["bye", "exit", "quit"]):
                break

if __name__ == "__main__":
    run()
