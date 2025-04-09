from stats import word_counter, char_counter
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    for book_path in sys.argv[1:]:
        book_text = get_book_text(book_path)
        num_words = word_counter(book_text)
        char_dict = char_counter(book_text)
        sorted_dict = sorted(char_dict.items(), key=lambda x:x[1], reverse=True)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        for k, v in sorted_dict:
            if k.isalpha() == True:
                print(f"{k}: {v}\n")

        print("============= END ===============")
    
main()