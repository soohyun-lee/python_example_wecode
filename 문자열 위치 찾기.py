def get_find(text1, text2):
    search = 'text1'
    if text1 in text2:
        return text2.index(text1)
    else:
        return -1

print(get_find('a', 'I am a hacker'))