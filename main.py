from core.listener import listen
from core.speaker import speak
from core.commands import handle_command
from core.jarvis_voice import speak

def main():
    speak("Hello Berto, I'm ready for your command.")
    while True:
        try:
            command = listen()
            if command:
                print(f"You said: {command}")
                response = handle_command(command)
                speak(response)
        except KeyboardInterrupt:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
