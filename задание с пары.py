print ('Веберите кол-во строк(столбцов) кв. матрицы')
print ()
razmer = int(input())
mat1 = []
mat2 = []
x = 0
y = 0
if razmer == 2:
    while x != 4:
        a = int(input("Введите элементы первой матрицы: "))
        mat1.append(a)
        x+=1
    print(mat1[0],' ',mat1[1])
    print(mat1[2], ' ', mat1[3])
    print()
    while y != 4:
        b = int(input("Введите элементы второй матрицы "))
        mat2.append(b)
        y+=1
    print(mat2[0], ' ', mat2[1])
    print(mat2[2], ' ', mat2[3])
    print()
    rez = []
    rez.append(mat1[0] * mat2[0] + mat1[1] * mat2[2])
    rez.append(mat1[0] * mat2[1] + mat1[1] * mat2[3])
    rez.append(mat1[2] * mat2[0] + mat1[3] * mat2[2])
    rez.append(mat1[2] * mat2[1] + mat1[3] * mat2[3])
    print('Произведение матриц')
    print(rez[0],' ',rez[1])
    print(rez[2], ' ', rez[3])

    det = rez[0]*rez[3]-rez[1]*rez[2]
    print('Определитель произведения матриц =', det)

if razmer == 3:
    while x != 9:
        a = int(input("Введите элементы первой матрицы: "))
        mat1.append(a)
        x+=1
    print(mat1[0], ' ', mat1[1],' ',mat1[2])
    print(mat1[3], ' ', mat1[4],' ',mat1[5])
    print(mat1[6], ' ', mat1[7], ' ', mat1[8])
    print()
    while y != 9:
        b = int(input("Введите элементы второй матрицы: "))
        mat2.append(b)
        y+=1
    print(mat2[0], ' ', mat2[1],' ',mat2[2])
    print(mat2[3], ' ', mat2[4],' ',mat2[5])
    print(mat2[6], ' ', mat2[7], ' ', mat2[8])
    print()
    rez = []
    rez.append(mat1[0] * mat2[0] + mat1[1] * mat2[3] + mat1[2]*mat2[6])
    rez.append(mat1[0] * mat2[1] + mat1[1] * mat2[4] + mat1[2] * mat2[7])
    rez.append(mat1[0] * mat2[2] + mat1[1] * mat2[5] + mat1[2] * mat2[8])
    rez.append(mat1[3] * mat2[0] + mat1[4] * mat2[3] + mat1[5] * mat2[6])
    rez.append(mat1[3] * mat2[1] + mat1[4] * mat2[4] + mat1[5] * mat2[7])
    rez.append(mat1[3] * mat2[2] + mat1[4] * mat2[5] + mat1[5] * mat2[8])
    rez.append(mat1[6] * mat2[0] + mat1[7] * mat2[3] + mat1[8] * mat2[6])
    rez.append(mat1[6] * mat2[1] + mat1[7] * mat2[4] + mat1[8] * mat2[7])
    rez.append(mat1[6] * mat2[2] + mat1[7] * mat2[5] + mat1[8] * mat2[8])
    print('Произведение матриц')
    print(rez[0], ' ', rez[1],' ',rez[2])
    print(rez[3], ' ', rez[4],' ',rez[5])
    print(rez[6], ' ', rez[7], ' ', rez[8])

    det = ((rez[0]*rez[4]*rez[8])+(rez[3]*rez[7]*rez[2])+(rez[1]*rez[5]*rez[6]))-((rez[2]*rez[4]*rez[6])+(rez[5]*rez[7]*rez[0])+(rez[2]*rez[1]*rez[8]))
    print('Определитель произведения матриц = ', det)
