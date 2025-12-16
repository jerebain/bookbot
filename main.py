def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    print(get_book_text("books/frankenstein.txt"))

from stats import word_count, character_count

contents = get_book_text("books/frankenstein.txt")
total_words = word_count(contents)
print(f"Found {total_words} total words")
print(character_count(contents))