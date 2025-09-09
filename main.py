from stats import count_words
from stats import count_characters
from stats import sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    path="./books/frankenstein.txt"
    count_words(get_book_text(path))
    sort_dict(get_book_text(count_characters(get_book_text(path))))

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
main()
