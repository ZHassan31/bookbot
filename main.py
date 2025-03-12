from stats import get_num_words,get_book_text,hashmap,sorted_hashmap
import sys
# def get_book_text(filepath):
#     """Reads the contents of a file and returns it as a string."""
#     with open(filepath, 'r', encoding='utf-8') as f:
#         return f.read()
# def words_in_text(text):
#     """Returns a list of words in a text."""
#     return text.split()

def main():
    """Main function that prints the contents of frankenstein.txt."""
        # Argument validation
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the book path from the command-line argument
    book_path = sys.argv[1]

    try:
        book_text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: File not found at path '{book_path}'")
        sys.exit(1)
    # book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    num_words = len(get_num_words(book_text))
    # print(hashmap(book_text))
    # print(f"{num_words} words found in the document.")
    book = sorted_hashmap(book_text)
        # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for character, count in book.items():
        print(f"{character}: {count}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()
