def duplicate_encode(word):
    l = len(word)
    word = word.lower()
    char = ''
    i = 0
    newword = ''
    while i < l:
        c = 0
        j = 0
        while j < l:
            if word[i] == word [j]:
                c = c + 1
                j = j + 1
            else:
                j = j + 1
        if c > 1:
            newword = newword + ')'
        else:
            newword = newword + '('
        i = i + 1
    return newword