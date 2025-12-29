from stats import get_num_words, count_characters, sort_char_count


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    file_text = get_book_text("books/frankenstein.txt")
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