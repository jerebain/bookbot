def word_count(file_contents):
    num = file_contents.split()
    num_words = len(num)
    return num_words

def character_count(file_contents):
    lower_case = file_contents.lower()
    symbols = {}
    for i in lower_case:
        if i in symbols:
            symbols[i] += 1
        else:
            symbols[i] = 1
    return symbols

def sort_on(text):
    return text["num"]

def sorted_dictionary(file_contents):
    ready = []
    for i in file_contents:
        number = file_contents[i]
        ready.append({"char": i, "num": number})
    ready.sort(reverse=True, key=sort_on)
    return ready
