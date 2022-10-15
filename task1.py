number = int(input())
bits = 0


while number:
    if number == -1:
        bits += 1
        break
    number = number >> 1
    bits += number & 1

print(bits)