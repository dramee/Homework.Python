number = int(input())
bits = 0


while number:
    if number == -1:
        bits += 1
        break
    bits += number & 1
    number = number >> 1


print(bits)