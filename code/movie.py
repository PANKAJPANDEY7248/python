import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import init, Fore
import random

init(autoreset=True)

# Load dataset
def load_data(file_path='imdb_top_1000.csv'):
    try:
        df = pd.read_csv(file_path)
        df['combined_features'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
        return df
    except FileNotFoundError:
        print(Fore.RED + f"Error: File '{file_path}' not found.")
        exit()

movies_df = load_data()

# TF-IDF vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_df['combined_features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# List unique genres
def list_genres(df):
    return sorted(set(genre.strip() for sublist in df['Genre'].dropna().str.split(', ') for genre in sublist))

genres = list_genres(movies_df)

# Recommend movies
def recommend_movies(genre=None, mood=None, rating=None, top_n=5):
    filtered_df = movies_df
    if genre:
        filtered_df = filtered_df[filtered_df['Genre'].str.contains(genre, case=False, na=False)]
    if rating:
        filtered_df = filtered_df[filtered_df['IMDB_Rating'] >= rating]
    filtered_df = filtered_df.sample(frac=1).reset_index(drop=True)

    recommendations = []
    for _, row in filtered_df.iterrows():
        overview = row['Overview']
        if pd.isna(overview):
            continue
        polarity = TextBlob(overview).sentiment.polarity
        if (mood and ((TextBlob(mood).sentiment.polarity < 0 and polarity > 0) or polarity >= 0)) or not mood:
            recommendations.append((row['Series_Title'], polarity))
        if len(recommendations) == top_n:
            break
    return recommendations if recommendations else "No suitable movie recommendations found."

# Display recommendations
def display_recommendations(recs, name):
    print(Fore.YELLOW + f"\n🎬 AI-Analyzed Movie Recommendations for {name}:")
    for idx, (title, polarity) in enumerate(recs, 1):
        sentiment = "Positive 😊" if polarity > 0 else "Negative 😞" if polarity < 0 else "Neutral 😐"
        print(f"{Fore.CYAN}{idx}. 🎥 {title} (Polarity: {polarity:.2f}, {sentiment})")

# Main interaction
def main():
    print(Fore.BLUE + "🎉 Welcome to your AI Movie Recommendation Assistant!")
    name = input(Fore.YELLOW + "What's your name? ").strip()
    print(Fore.GREEN + f"\nHi {name}, let's find a movie you'll love!")

    print(Fore.GREEN + "\nAvailable Genres:")
    for idx, genre in enumerate(genres, 1):
        print(f"{Fore.CYAN}{idx}. {genre}")
    
    genre_input = input(Fore.YELLOW + "\nEnter genre name: ").strip().title()
    mood = input(Fore.YELLOW + "How do you feel today? (Describe your mood): ").strip()
    rating_input = input(Fore.YELLOW + "Enter minimum IMDb rating (or press Enter to skip): ").strip()
    rating = float(rating_input) if rating_input else None

    recs = recommend_movies(genre=genre_input, mood=mood, rating=rating, top_n=5)
    if isinstance(recs, str):
        print(Fore.RED + recs)
    else:
        display_recommendations(recs, name)

if __name__ == "__main__":
    main()
