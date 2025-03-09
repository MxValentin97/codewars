def solution(s):
    l = len(s)
    list = []
    a = 0
    b = 2
    z = l - 1
    x = ''
    if l % 2 == 0:
        while a < z:
            list.append(s[a:b])
            a = a + 2
            b = b + 2
    else:
        while a < (z-1):
            list.append(s[a:b])
            a = a + 2
            b = b + 2
        x = s[z] + '_'
        list.append(x)
    return list