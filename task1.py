number = int(input())
bits = 0


while number:
    bits += number & 1
    number = number >> 1
    if number == -1:
        bits += 1
        break


print(bits)