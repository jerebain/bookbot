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