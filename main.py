from stats import count_words
from stats import count_characters
from stats import sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    else:
        path = sys.argv[1]
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        count_words(get_book_text(path))
        print("--------- Character Count -------")
        sort_dict(count_characters(get_book_text(path)))
main()
