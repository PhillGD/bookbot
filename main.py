def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    #print(book_text)
    word_count = count_words(book_text)
    chars_dict = get_chars_dict(book_text)
    print(f"--- Begin Report of {book_path} ---")
    print(f"Word Count: {word_count}")
    print("Character Count:")
    for char in sorted(chars_dict, key=chars_dict.get, reverse=True):
        if char.isalpha():
            print(f"'{char}' : {chars_dict[char]}")
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

main()