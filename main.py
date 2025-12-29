def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    file_text = get_book_text("books/frankenstein.txt")
    word_count = len(file_text.split())
    print(f"Found {word_count} total words")

main()