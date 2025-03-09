def invert(lst):
    i = 0
    l = len(lst) - 1
    newlst = []
    while i <= l:
        n = lst [i] * -1
        newlst.append(n)
        i = i + 1
    return newlst