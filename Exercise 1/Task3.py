class User:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return self.username


class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def __str__(self):
        return f"[{self.sender.username}]: {self.content}"


class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.members = []
        self.chat_history = []

    def join(self, user):
        if user not in self.members:
            self.members.append(user)
            print(f"{user.username} has joined '{self.room_name}'.")
        else:
            print(f"{user.username} is already in the room.")

    def leave(self, user):
        if user in self.members:
            self.members.remove(user)
            print(f"{user.username} has left '{self.room_name}'.")
        else:
            print(f"{user.username} is not in the room.")

    def send_message(self, user, content):
        if user in self.members:
            msg = Message(user, content)
            self.chat_history.append(msg)
            print(f"Message sent: {msg}")
        else:
            print(f"{user.username} must join the room before sending messages.")

    def view_history(self):
        print(f"\n--- Chat History for '{self.room_name}' ---")
        if not self.chat_history:
            print("No messages yet.")
        else:
            for msg in self.chat_history:
                print(msg)
        print("-------------------------------------------\n")


# Demo
room = ChatRoom("Python Learners")
alice = User("Alice")
bob = User("Bob")
charlie = User("Charlie")

room.join(alice)
room.join(bob)
room.join(charlie)

room.send_message(alice, "Hello everyone!")
room.send_message(bob, "Hi Alice! How are you?")
room.send_message(charlie, "Hey guys, excited to learn Python!")
room.send_message(alice, "Let's start with OOP concepts today.")

room.view_history()

room.leave(charlie)
room.send_message(charlie, "Can I still send messages?")
