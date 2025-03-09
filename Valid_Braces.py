def valid_braces(string):
    l = len (string) - 1
    i = 0
    v1 = ''
    v2 = ''
    if len(string) % 2 == 0:
        while i < (len(string)/2):
            v1 = string[i] + string[i+1]
            v2 = string[i] + string[l-i]
            if v1 not in ('()', '[]', '{}') and v2 not in ('()', '[]', '{}'):
                return False
            else:
                i = i + 2
        return True
    else:
        return False