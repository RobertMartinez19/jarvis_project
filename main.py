from core.speaker import speak
from core.ai_response import get_ai_response

def main():
    # Initial greeting
    greeting = "Hello Roberto. I am online and ready to assist you."
    print(f"Jarvis: {greeting}")
    speak(greeting)

    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() in ['exit', 'quit', 'shutdown']:
                farewell = "Shutting down. Have a great day, Roberto."
                print(f"Jarvis: {farewell}")
                speak(farewell)
                break

            # Get AI-generated response
            ai_reply = get_ai_response(user_input)
            print(f"Jarvis: {ai_reply}")
            speak(ai_reply)

        except KeyboardInterrupt:
            print("\n[Interrupted by user]")
            break
        except Exception as e:
            error_msg = f"An error occurred: {e}"
            print(f"Jarvis: {error_msg}")
            speak("Sorry, something went wrong.")

if __name__ == "__main__":
    main()
