import sys 
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

from stats import word_count, character_count, sorted_dictionary

contents = get_book_text(sys.argv[1])
total_words = word_count(contents)
dictionary_text = character_count(contents)
sorted = sorted_dictionary(dictionary_text)

report_start = (
    f"============ BOOKBOT ============ \n"
    f"Analyzing book found at {sys.argv[1]}... \n"
    "----------- Word Count ---------- \n"
    f"Found {total_words} total words \n"
    "--------- Character Count -------")
print(report_start)
for i in sorted:
    char = i["char"]
    num = i["num"]
    if char.isalpha():
        print(f"{char}: {num}")
print("============= END ===============")