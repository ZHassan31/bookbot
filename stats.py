from collections import Counter
def get_book_text(filepath):
    """Reads the contents of a file and returns it as a string."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
def get_num_words(text):
    """Returns a list of words in a text."""
    return text.split()
def hashmap(text):
    letters = [char.lower() for char in text]
    # Use Counter to count occurrences
    letter_counts = Counter(letters)
    
    return letter_counts
def sorted_hashmap(text):
    letter_counts = hashmap(text)
    # Filter out non-alphabet characters and sort the dictionary by key
    sorted_counts = {k: v for k, v in sorted(letter_counts.items(), key=lambda item: item[1], reverse=True) if k.isalpha()}
    return sorted_counts