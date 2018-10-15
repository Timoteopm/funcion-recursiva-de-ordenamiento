author = 'Timoteo P Martinez'

class numerosEnteros:

    numero =[13, 3, 9, 0, 15, 11, 5, 7, 1]
    print(numero)

    numero.sort()
    print(numero)


numeros2 = [7, 5, 9, 6, 10, 4, 8, 3, 11, 2, 12, 1]

if (numeros2[0] > numeros2[1]):
    num = numeros2[0]
    numeros2[0] = numeros2[1]
    numeros2[1] = num


if (numeros2[0] > numeros2[2]):
    num = numeros2[0]
    numeros2[0] = numeros2[2]
    numeros2[2] = num

if (numeros2[0] > numeros2[3]):
    num = numeros2[0]
    numeros2[0] = numeros2[3]
    numeros2[3] = num

if (numeros2[0] > numeros2[4]):
    num = numeros2[0]
    numeros2[0] = numeros2[4]
    numeros2[4] = num

if (numeros2[0] > numeros2[5]):
    num = numeros2[0]
    numeros2[0] = numeros2[5]
    numeros2[5] = num

if (numeros2[0] > numeros2[6]):
    num = numeros2[0]
    numeros2[0] = numeros2[6]
    numeros2[6] = num

if (numeros2[0] > numeros2[7]):
    num = numeros2[0]
    numeros2[0] = numeros2[7]
    numeros2[7] = num

if (numeros2[0] > numeros2[8]):
    num = numeros2[0]
    numeros2[0] = numeros2[8]
    numeros2[8] = num

if (numeros2[0] > numeros2[9]):
    num = numeros2[0]
    numeros2[0] = numeros2[9]
    numeros2[9] = num

if (numeros2[0] > numeros2[10]):
    num = numeros2[0]
    numeros2[0] = numeros2[10]
    numeros2[10] = num

if (numeros2[0] > numeros2[11]):
    num = numeros2[0]
    numeros2[0] = numeros2[11]
    numeros2[11] = num

#print(numeros2)


numeros4 = [7, 5, 9, 6, 10, 4, 8, 3, 2, 11, 1, 13, 17, 19, 21, 15]

for ordenar in range(1, len(numeros4)):
    for inicio in range(len(numeros4) - ordenar):
        if numeros4[inicio] > numeros4[inicio + 1]:
            x = numeros4[inicio]
            numeros4[inicio] = numeros4[inicio + 1]
            numeros4[inicio + 1] = x

            print(numeros4)
