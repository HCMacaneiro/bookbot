from stats import get_num_words


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    file_text = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(file_text)
    print(f"Found {word_count} total words")

main()