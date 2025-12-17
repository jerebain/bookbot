def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    print(get_book_text("books/frankenstein.txt"))

from stats import word_count, character_count, sorted_dictionary

contents = get_book_text("books/frankenstein.txt")
total_words = word_count(contents)
dictionary_text = character_count(contents)
sorted = sorted_dictionary(dictionary_text)
print (f"============ BOOKBOT ============ Analyzing book found at books/frankenstein.txt... ------------ Word Count ------------ Found {total_words} total words ------------ Character Count ------------ {sorted}")