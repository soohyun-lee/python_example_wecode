def find_longest_word(word_list):
    long_word = ''
    long_size = 0
    for word in word_list:
        if len(word) > long_size:
            long_word = word
            long_size = len(word)
    return long_word