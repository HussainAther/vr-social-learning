# text_chat.py

class TextChat:
    def __init__(self):
        self.chat_history = []

    def send_message(self, sender, message):
        # Send a message and log it in the chat history
        chat_entry = f"{sender}: {message}"
        self.chat_history.append(chat_entry)
        self.display_message(chat_entry)

    def display_message(self, message):
        # Display message (placeholder for actual VR UI display)
        print(message)

    def get_chat_history(self):
        # Retrieve chat history
        return self.chat_history

# Usage example
chat = TextChat()
chat.send_message("Alice", "Hello, everyone!")
chat.send_message("Bob", "Hi Alice!")
print("Chat History:", chat.get_chat_history())

