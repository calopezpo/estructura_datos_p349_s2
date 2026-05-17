import time

matriz = list(range(0, 1000001))
numero = int(input("Ingrese el numero que desea buscar: "))

inicio_secuencial = time.time()

pasos_secuencial = 0
encontrado = False

for i in range(len(matriz)):

    pasos_secuencial += 1

    if matriz[i] == numero:

        encontrado = True

        print("="*50)
        print("BUSQUEDA SECUENCIAL")
        print("Número encontrado:", numero)
        print("Posición:", i)
        print("Pasos:", pasos_secuencial)
        print("Tiempo:", time.time() - inicio_secuencial, "segundos")
        print("="*50)

        break

if encontrado == False:

    print("="*50)
    print("BUSQUEDA SECUENCIAL")
    print("Número no encontrado")
    print("Tiempo:", time.time() - inicio_secuencial, "segundos")
    print("="*50)


inicio_binaria = time.time()

izquierda = 0
derecha = len(matriz) - 1

pasos_binaria = 0
encontrado = False

while izquierda <= derecha:

    pasos_binaria += 1

    medio = (izquierda + derecha) // 2

    if matriz[medio] == numero:

        encontrado = True

        print("="*50)
        print("BUSQUEDA BINARIA")
        print("Número encontrado:", numero)
        print("Posición:", medio)
        print("Pasos realizados:", pasos_binaria)
        print("Tiempo:", time.time() - inicio_binaria, "segundos")
        print("="*50)

        break

    elif matriz[medio] < numero:

        izquierda = medio + 1

    else:

        derecha = medio - 1

if encontrado == False:

    print("="*50)
    print("BUSQUEDA BINARIA")
    print("Número no encontrado")
    print("Tiempo:", time.time() - inicio_binaria, "segundos")
    print("="*50)

        