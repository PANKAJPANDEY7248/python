import colorama
from colorama import Fore, Style
from textblob import TextBlob
import datetime

colorama.init()

def print_intro():
    print(Fore.MAGENTA + "Welcome to the Sentiment Spy!" + Style.RESET_ALL)
    print("This chatbot analyzes your text and tells you the sentiment.")
    print("Type 'exit' to end the conversation.\n")

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment_type = "positive"
    elif polarity < 0:
        sentiment_type = "negative"
    else:
        sentiment_type = "neutral"
    return polarity, sentiment_type

def print_sentiment(polarity, sentiment_type):
    if sentiment_type == "positive":
        print(Fore.GREEN + f"Sentiment: {sentiment_type} ({polarity})" + Style.RESET_ALL)
    elif sentiment_type == "negative":
        print(Fore.RED + f"Sentiment: {sentiment_type} ({polarity})" + Style.RESET_ALL)
    else:
        print(Fore.CYAN + f"Sentiment: {sentiment_type} ({polarity})" + Style.RESET_ALL)

def print_exit_message():
    print(Fore.MAGENTA + "Thank you for using Sentiment Spy. Farewell!" + Style.RESET_ALL)

def main():
    print_intro()
    conversation_history = []
    while True:
        user_input = input(Fore.BLUE + "You: " + Style.RESET_ALL)
        if user_input.lower() == "exit":
            print_exit_message()
            break
        polarity, sentiment_type = analyze_sentiment(user_input)
        print_sentiment(polarity, sentiment_type)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conversation_history.append((timestamp, user_input, polarity, sentiment_type))
        print(Fore.YELLOW + "\nConversation History:" + Style.RESET_ALL)
        for entry in conversation_history:
            ts, text, pol, stype = entry
            print(Fore.YELLOW + f"[{ts}] You said: '{text}'" + Style.RESET_ALL)
            if stype == "positive":
                print(Fore.GREEN + f" -> Sentiment: {stype} ({pol})" + Style.RESET_ALL)
            elif stype == "negative":
                print(Fore.RED + f" -> Sentiment: {stype} ({pol})" + Style.RESET_ALL)
            else:
                print(Fore.CYAN + f" -> Sentiment: {stype} ({pol})" + Style.RESET_ALL)
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()
