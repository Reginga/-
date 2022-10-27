import numpy as np

print('Программа поддерживает только матрицы 3x3');
print()
n = 3
stolb = 3
print()

mat = []
stroki = 1
for i in range(n):
    print('Введите', stolb, 'элемент(а)', stroki, '-ой строки через пробел: ')
    row = input().split()
    while len(row) < stolb:
        print('В данной строке кол-во элементов меньше', stolb, ', введите строку ещё раз: ')
        row = input().split()
        while len(row) > stolb:
            print('В данной строке кол-во элементов больше', stolb, ', введите строку ещё раз: ')
            row = input().split()
    while len(row) > stolb:
        print('В данной строке кол-во элементов больше', stolb, ', введите строку ещё раз: ')
        row = input().split()
        while len(row) < stolb:
            print('В данной строке кол-во элементов меньше', stolb, ', введите строку ещё раз: ')
            row = input().split()
    stroki += 1
    for i in range(len(row)):
        row[i] = int(row[i])
    mat.append(row)
print()

opr = np.linalg.det(mat)
if opr == 0:
    print('Данная матрица необратима')
else:
    print();
    print('Матрица: ');
    print(np.array(mat));
    print()
    obr = np.linalg.inv(mat)
    print(obr)