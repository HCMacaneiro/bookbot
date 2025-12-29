import sys
from stats import get_num_words, count_characters, sort_char_count


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_text = get_book_text(sys.argv[1])
    word_count = get_num_words(file_text)
    char_count = count_characters(file_text)
    sorted_dict_list = sort_char_count(char_count)
    print(f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
    for dict in sorted_dict_list:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()