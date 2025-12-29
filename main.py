from stats import get_num_words, count_characters


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    file_text = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(file_text)
    char_count = count_characters(file_text)
    print(f"Found {word_count} total words")
    print(char_count)

main()