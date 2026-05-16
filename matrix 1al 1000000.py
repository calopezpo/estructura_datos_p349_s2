matriz = list(range(1, 1000000))
numero = int(input("Ingrese el numero que desea buscar: "))


pasos_secuencial = 0

for i in range(len(matriz)):
    pasos_secuencial += 1

    if matriz[i] == numero:
        print("="*50)
        print("BUSQUEDA SECUENCIAL")
        print("Número encontrado con búsqueda secuencial", numero)
        print("Pasos:", pasos_secuencial)
        print("="*50)

        break

izquierda = 0
derecha = len(matriz) - 1

pasos_binaria = 0

while izquierda <= derecha:

    pasos_binaria += 1

    medio = (izquierda + derecha) // 2

    if matriz[medio] == numero:

        print("="*50)
        print("BUSQUEDA BINARIA")
        print("Número encontrado:", numero)
        print("Pasos realizados:", pasos_binaria)
        print("="*50)
        break

    elif matriz[medio] < numero:

        izquierda = medio + 1

    else:

        derecha = medio - 1

        asdasda