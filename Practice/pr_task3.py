import datetime



class message:
    def __init__(self,sender,content):
        self.sender=sender
        self.content=content
        self.timestamp=datetime.datetime.now().strftime("%H:%M:%S")
    def __str__(self):
        return f"[{self.timestamp}] {self.sender.name}: {self.content}"

class User:
    def __init__(self,name):
        self.name=name
        self.rooms=[]
    def __str__(self):
        return self.name
    def join_room(self,room):
        if room not in self.rooms:
            self.rooms.append(room)
            room.add_user(self)
    def leave_room(self,room):
        if room in self.rooms:
            self.rooms.remove(room)
            room.remove_user(self)      
    def send_message(self,room,content):
        if room in self.rooms:
            msg=message(self,content)
            room.receive_message(msg)
        else:
            print(f"{self.name} is not in this room!")
class ChatRoom:
    def __init__(self,room_name):
        self.messages=[]
        self.users=[]
        self.room_name=room_name
    def add_user(self,user):
        if user not in self.users:
            self.users.append(user)
        print(f"{user.name} joined the {self.room_name}")
    def remove_user(self,user):
        if user in self.users:
            self.users.remove(user)
        print(f"{user.name} left the {self.room_name}")
    def receive_message(self,msg):
        self.messages.append(msg)
        print(msg)
    def view_history(self):
        print(f"\n--- Chat History: {self.room_name} ---")
        if not self.messages:
            print("No messages yet")
        for msg in self.messages:
            print(msg)
        print("-----------------------------------\n")
    def show_users(self):
        print(f"Users in {self.room_name}: {[u.name for u in self.users]}")
    
    # create users
alice = User("Alice")
bob   = User("Bob")
carol = User("Carol")

# create room
room = ChatRoom("General")

# join
alice.join_room(room)    # Alice joined 'General'
bob.join_room(room)      # Bob joined 'General'
carol.join_room(room)    # Carol joined 'General'

room.show_users()        # ['Alice', 'Bob', 'Carol']

# send messages
alice.send_message(room, "Hello everyone!")
bob.send_message(room, "Hey Alice!")
carol.send_message(room, "Hi guys!")

# carol leaves
carol.leave_room(room)   # Carol left 'General'

# carol tries to send after leaving
carol.send_message(room, "Can I still send?")  # Carol is not in this room!

# view history
room.view_history()    