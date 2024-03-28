import tkinter as tk
import random

words = {"Avatar", "The Dark Knight", "Inception", "Interstellar", "The Avengers", "Titanic", "Black Panther", "La La Land",
         "The Wolf of Wall Street", "Gravity", "The Lord of the Rings The Return of the King", "The Shape of Water",
         "Mad Max Fury Road", "The Revenant", "Joker", "The Social Network", "Frozen", "The Grand Budapest Hotel", "Django Unchained",
         "The Martian", "Whiplash", "Avengers Infinity War", "Avengers Endgame", "The Departed", "The Kings Speech", "The Prestige",
         "The Dark Knight Rises", "12 Years a Slave", "Toy Story 3", "Birdman", "The Shape of Water", "Moonlight", "The Hurt Locker",
         "Slumdog Millionaire", "The Artist", "No Country for Old Men", "The Curious Case of Benjamin Button", "District 9",
         "The Hurt Locker", "A Beautiful Mind", "Manchester by the Sea", "The Big Short", "Argo", "Whiplash", "Moonlight", "Her",
         "The Grand Budapest Hotel", "Spotlight", "The Help", "1917", "The Irishman", "Parasite", "Get Out", "The Shape of Water",
         "Lady Bird", "A Star Is Born", "La La Land", "Ford v Ferrari", "The Favourite", "Bohemian Rhapsody", "Call Me by Your Name",
         "The Theory of Everything", "The Imitation Game", "Silver Linings Playbook", "American Hustle", "Dallas Buyers Club",
         "The Fighter", "The Kings Speech", "The Revenant", "Birdman", "12 Years a Slave", "Room", "The Shape of Water", "Moonlight",
         "La La Land", "The Artist", "The Descendants", "The Tree of Life", "The Social Network", "Inception", "Toy Story 3",
         "Inglourious Basterds", "Up", "The Hurt Locker", "Avatar", "Slumdog Millionaire", "No Country for Old Men", "The Departed",
         "Crash", "Million Dollar Baby", "The Lord of the Rings The Return of the King", "Chicago", "A Beautiful Mind", "Gladiator",
         "American Beauty", "Shakespeare in Love", "Titanic", "The English Patient", "Braveheart", "Forrest Gump", "Schindler's List",
         "Unforgiven", "The Silence of the Lambs", "Dances with Wolves", "Driving Miss Daisy", "Rain Man", "The Last Emperor",
         "Platoon", "Out of Africa", "Amadeus", "Terms of Endearment", "Gandhi", "Chariots of Fire", "Ordinary People",
         "Kramer vs Kramer", "The Deer Hunter", "Annie Hall", "Rocky", "One Flew Over the Cuckoos Nest", "The Godfather Part II",
         "The Sting", "The French Connection", "Patton", "Midnight Cowboy", "Oliver!", "In the Heat of the Night",
         "A Man for All Seasons", "The Sound of Music", "My Fair Lady", "Tom Jones", "Lawrence of Arabia", "West Side Story",
         "The Apartment", "Ben-Hur", "Gigi", "The Bridge on the River Kwai", "Around the World in 80 Days", "Marty",
         "On the Waterfront", "From Here to Eternity", "An American in Paris", "All About Eve", "All the Kings Men", "Hamlet",
         "Gentlemans Agreement", "The Best Years of Our Lives", "The Lost Weekend", "Going My Way", "Casablanca", "Mrs Miniver",
         "How Green Was My Valley", "Rebecca", "Gone with the Wind", "You Cant Take It with You", "The Life of Emile Zola",
         "The Great Ziegfeld", "Mutiny on the Bounty", "It Happened One Night", "Cavalcade", "Grand Hotel", "Cimarron",
         "All Quiet on the Western Front", "The Broadway Melody", "Wings", "Sunset Boulevard", "All About Eve", "An American in Paris",
         "Around the World in 80 Days", "The Bridge on the River Kwai", "Gigi", "Ben-Hur", "West Side Story", "Lawrence of Arabia",
         "Tom Jones", "My Fair Lady", "The Sound of Music", "A Man for All Seasons", "Oliver!", "Midnight Cowboy", "Patton",
         "The French Connection", "The Godfather Part II", "One Flew Over the Cuckoos Nest", "Rocky", "Annie Hall", "The Deer Hunter",
         "Kramer vs Kramer", "Ordinary People", "Chariots of Fire", "Gandhi", "Terms of Endearment", "Amadeus", "Out of Africa",
         "Platoon", "The Last Emperor", "Rain Man", "Driving Miss Daisy", "Dances with Wolves", "The Silence of the Lambs",
         "Schindlers List", "Pulp Fiction", "Forrest Gump", "The Shawshank Redemption", "The Matrix", "Fight Club",
         "The Lord of the Rings The Fellowship of the Ring", "The Lord of the Rings The Two Towers",
         "The Lord of the Rings The Return of the King", "The Godfather", "The Godfather Part II", "The Godfather Part III",
         "The Shawshank Redemption", "The Green Mile", "Goodfellas", "The Silence of the Lambs", "The Sixth Sense", "Schindlers List",
         "Gladiator", "Braveheart", "Saving Private Ryan", "The Departed", "American History X", "The Prestige",
         "Inglourious Basterds", "Eternal Sunshine of the Spotless Mind", "The Truman Show", "The Lion King", "The Dark Knight Rises",
         "The Shining", "A Clockwork Orange", "2001 A Space Odyssey", "Inception", "The Grand Budapest Hotel", "The Shape of Water",
         "Pans Labyrinth", "Life is Beautiful", "City of God", "Spirited Away", "Amelie", "Crouching Tiger, Hidden Dragon", "Oldboy",
         "The Intouchables", "The Lives of Others", "The Pianist", "The Social Network", "Whiplash"}
unique_words = set(words)


def process_word():
    global original_word, processed_chars
    original_word = random.choice(list(unique_words)).lower()
    print(original_word)
    processed_chars = []
    for letter in original_word:
        if letter.lower() in {'a', 'e', 'i', 'o', 'u'}:
            processed_chars.append('X')
        elif letter.isdigit():
            processed_chars.append('.')
        elif letter == ' ':
            processed_chars.append('/')
        else:
            processed_chars.append('_')

    display_processed_word()


def display_processed_word():
    for label in processed_word_labels:
        label.destroy()
    for char in processed_chars:
        label = tk.Label(window, text=char, font=("Courier", 16), padx=5, pady=5)
        label.pack(side="left", padx=(2, 2))
        processed_word_labels.append(label)


def update_word():
    global processed_chars

    char = entry.get().strip()
    entry.delete(0, tk.END)

    for i, original_char in enumerate(original_word):
        if char.lower() == original_char.lower():
            processed_chars[i] = original_char

    display_processed_word()


window = tk.Tk()
window.title("Hangman")

processed_word_labels = []
num_words_label = tk.Label(window, font=("Arial", 12))
num_words_label.pack(pady=5)

process_button = tk.Button(window, text="Process New Word", command=process_word)
process_button.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=10)
entry.bind('<Return>', lambda event=None: update_word())

window.mainloop()
