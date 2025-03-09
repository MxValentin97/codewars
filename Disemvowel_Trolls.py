def disemvowel(string_):
    l = len(string_)
    i = 0
    newstring = ''
    while i < l:
        if string_[i] not in ('a','e','i','o','u','A','E','I','O','U'):
            newstring = newstring + string_[i]
            i = i + 1
        else:
            i = i + 1
    return newstring