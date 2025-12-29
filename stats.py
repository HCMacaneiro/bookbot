def get_num_words(text):
    return len(text.split())


def count_characters(text):
    characters = text.lower()
    print(f"Lower text: {characters}")
    char_count = {}
    for char in characters:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count