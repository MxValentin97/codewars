def rgb(r, g, b):
    input = [r, g, b]
    hex_code = ''
    hexadecimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for x in input:
        if x > 255:
            x = 255
        else:
            if x < 0:
                x = 0
        hex = ''
        while len(hex) < 2:
            remainder = x % 16
            x = x // 16
            hex += hexadecimal[remainder]
        hex_code += hex[::-1]
    return hex_code