import time
import threading

# Simple chat response
def chat_response():
    user_input = input("You: ")
    responses = {
        "hello": "Hello! 👋",
        "how are you": "I'm just a simple program, but I'm good!",
        "bye": "Goodbye! 👋",
    }
    print(f"Bot: {responses.get(user_input.lower(), 'I don’t understand that.')}\n")

# Simple poll system
def create_poll():
    question = input("Enter the poll question: ")
    options = input("Enter options separated by commas: ").split(",")
    votes = {option.strip(): 0 for option in options}

    print("\nPoll Started!")
    print(question)
    for i, option in enumerate(votes.keys(), 1):
        print(f"{i}. {option}")

    while True:
        vote = input("\nVote by entering option number (or type 'end' to finish): ")
        if vote.lower() == "end":
            break
        if vote.isdigit() and 1 <= int(vote) <= len(votes):
            option = list(votes.keys())[int(vote) - 1]
            votes[option] += 1
            print(f"Voted for {option}!")

    print("\nPoll Results:")
    for option, count in votes.items():
        print(f"{option}: {count} votes")

# Reminder system
reminders = []

def set_reminder():
    message = input("Enter reminder message: ")
    seconds = int(input("Enter time in seconds: "))
    reminders.append((message, time.time() + seconds))
    print(f"Reminder set for {seconds} seconds from now.")

def check_reminders():
    while True:
        now = time.time()
        for reminder in reminders[:]:
            message, remind_time = reminder
            if now >= remind_time:
                print(f"\nReminder: {message}")
                reminders.remove(reminder)
        time.sleep(1)

# Music queue system
music_queue = []

def add_song():
    song = input("Enter song name: ")
    music_queue.append(song)
    print(f"{song} added to queue.")

def play_next():
    if music_queue:
        print(f"Now playing: {music_queue.pop(0)}")
    else:
        print("No songs in queue.")

# Background reminder thread
threading.Thread(target=check_reminders, daemon=True).start()

# Main menu loop
while True:
    print("\nOptions: [1] Chat [2] Poll [3] Reminder [4] Add Song [5] Play Song [6] Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        chat_response()
    elif choice == "2":
        create_poll()
    elif choice == "3":
        set_reminder()
    elif choice == "4":
        add_song()
    elif choice == "5":
        play_next()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
1