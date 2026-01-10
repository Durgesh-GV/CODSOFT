from datetime import datetime, date, timedelta, timezone
def chatbot_response(user_input, user_name):
    user_input = user_input.lower()
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return f"Hello {user_name}!"
    elif "how are you" in user_input:
        return "I'm doing great, thanks for asking!"
    elif "time" in user_input:
        utc_time = datetime.now(timezone.utc)
        ist_timezone = timezone(timedelta(hours=5, minutes=30))
        ist_time = utc_time.astimezone(ist_timezone)
        return "Current time is " + ist_time.strftime("%H:%M:%S")
    elif "date" in user_input:
        today = date.today()
        return "Today's date is " + today.strftime("%d-%m-%Y")
    elif "project" in user_input:
        return "This project demonstrates a rule-based chatbot using Python."
    elif any(word in user_input for word in ["bye", "exit", "quit"]):
        return "Goodbye! Wishing you success in your life."
    else:
        return "Sorry,I couldn't understand that. Please try again."
print("Chatbot: Hello! I am a smart rule-based chatbot.")
user_name = input("Chatbot: May I know your name?\nYou: ")
print(f"Chatbot: Nice to meet you, {user_name}! How can I assist you?")
while True:
    user_input = input("You: ")
    print("Chatbot:", chatbot_response(user_input, user_name))
    if any(word in user_input.lower() for word in ["bye", "exit", "quit"]):
        break
input("\nPress Enter to exit...")
