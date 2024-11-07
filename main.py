def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    #print(book_text)
    word_count = count_words(book_text)
    #print(f"Word Count: {word_count}")
    chars_dict = get_chars_dict(book_text)
    print(f"Character Dictionary: {chars_dict}")

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