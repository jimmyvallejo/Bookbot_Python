def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    lowered_text = text.lower()
    num_words = get_num_words(text)
    num_chars = get_characters(lowered_text)
    word_list = set_to_list(num_chars)
    word_list.sort(reverse=True, key=sort_on)
    
    print("--- Begin report of books/frankenstein.txt")
    print(f"{num_words} words found in the document")
    for dict in word_list:
        print(f"The \"{dict["name"]}\" character was found {dict["num"]} ")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_characters(text):
    hash_map = {}
    for char in text:
        lowered = char.lower()
        if lowered in hash_map:
            hash_map[lowered] += 1
        else:
            hash_map[lowered] = 1
    return hash_map

def sort_on(dict):
    return dict["num"]

def set_to_list(dict):
    list = []
    for key in dict:
        if key.isalpha():
            list.append({"name": key, "num": dict[key]})
    return list

main()