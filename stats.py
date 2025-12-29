def get_num_words(text):
    return len(text.split())


def count_characters(text):
    characters = text.lower()
    char_count = {}
    for char in characters:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_on(items):
    return items["num"]

def sort_char_count(char_dict):
    list_of_dicts = []
    for char in char_dict:
        if not char.isalpha():
            continue
        temp_dict = {"char": char, "num": char_dict[char]}
        list_of_dicts.append(temp_dict)

    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts    