from datetime import datetime

def handle_command(command):
    command = command.lower()
    if "time" in command:
        return f"The current time is {datetime.now().strftime('%H:%M')}"
    elif "hello" in command:
        return "Hi Berto, how can I help you?"
    else:
        return "Sorry, I don't understand that yet."
