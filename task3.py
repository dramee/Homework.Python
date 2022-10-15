matrix = [[]]

string = input().split()
i = 0
for s in string:
    if s != "|":
        matrix[i].append(float(s))
    else:
        matrix.append([])
        i += 1


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end = " ")
    print("")