import random

# Constants for text colors (note: actual console output may vary across platforms)
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"

# Sample travel suggestions
travel_suggestions = [
    {"destination": "Paris", "activity": "visit the Eiffel Tower"},
    {"destination": "Tokyo", "activity": "explore Shibuya"},
    {"destination": "New York", "activity": "see a Broadway show"},
    {"destination": "Sydney", "activity": "walk by the Opera House"},
    {"destination": "Cairo", "activity": "tour the pyramids"},
]

# Sample jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
]

# Function to display a welcome message
def welcome_message():
    print(f"{BLUE}Welcome to TravelBot! Let's find your next adventure!{RESET}")

# Function to provide a travel suggestion
def suggest_travel():
    suggestion = random.choice(travel_suggestions)
    print(f"{GREEN}How about you {suggestion['activity']} in {suggestion['destination']}?{RESET}")

# Function to tell a joke
def tell_joke():
    joke = random.choice(jokes)
    print(f"{YELLOW}Here's a joke for you: {joke}{RESET}")

# Function to show help
def show_help():
    print(f"{BLUE}You can ask TravelBot for travel suggestions, jokes, or help.{RESET}")

# Main chatbot function
def travel_bot():
    welcome_message()
    while True:
        user_input = input(f"{RED}You: {RESET}").lower()
        if "suggest" in user_input or "travel" in user_input:
            suggest_travel()
        elif "joke" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "bye" in user_input or "exit" in user_input:
            print(f"{BLUE}Goodbye! Safe travels!{RESET}")
            break
        else:
            print(f"{RED}TravelBot: Sorry, I don't understand that. Try 'suggest', 'joke', or 'help'.{RESET}")

# Run the chatbot
if __name__ == "__main__":
    travel_bot()
