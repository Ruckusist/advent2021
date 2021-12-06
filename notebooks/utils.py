def open_day(day=1):
    return [x.strip() for x in open(f"../data/day{day}.txt", "r").readlines()]

def b2n(binary):
    binary = int(str(binary, encoding='utf-8'))
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal