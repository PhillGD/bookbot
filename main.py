def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    #print(book_text)
    word_count = count_words(book_text)
    chars_dict = get_chars_dict(book_text)
    print(f"--- Begin Report of {book_path} ---")
    print(f"Word Count: {word_count}")
    print("Character Count:")
    sorted_chars_dict = sort_dict(chars_dict)
    for char in sorted_chars_dict:
        if char.isalpha():
            print(f"'{char}' : {sorted_chars_dict[char]}")
    print("--- End Report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def get_chars_dict(text):
    low_text = text.lower()
    chars_dict = {}
    for char in low_text:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def sort_dict(unsorted_dict):
    sorted_dict = dict(sorted(unsorted_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

main()