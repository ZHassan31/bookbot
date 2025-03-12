import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    
    try:
        with open(book_path, 'r') as f:
            text = f.read()
        
        # Count letters
        letter_counts = {}
        for char in text.lower():
            if char.isalpha():
                letter_counts[char] = letter_counts.get(char, 0) + 1
        
        # Print report - JUST the counts as specified in the test
        # No headers, no formatting, just the bare minimum
        for char in sorted(letter_counts, key=letter_counts.get, reverse=True):
            print(f"{char}: {letter_counts[char]}")
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()