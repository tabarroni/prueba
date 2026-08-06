def eliminar_duplicados(lista):
    #eliminar duplicados manualmente
    sin_duplicados = []
    for numero in lista:
        # Verificamos manualmente si el número ya está en la lista resultante
        existe = False
        for item in sin_duplicados:
            if item == numero:
                existe = True
                break
        if not existe:
            sin_duplicados.append(numero)

    #ordenar la lista de menor a mayor (Algoritmo Bubble Sort)
    n = len(sin_duplicados)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sin_duplicados[j] > sin_duplicados[j + 1]:
                # Intercambio de valores (swap)
                temp = sin_duplicados[j]
                sin_duplicados[j] = sin_duplicados[j + 1]
                sin_duplicados[j + 1] = temp
    return sin_duplicados

entrada = [4, 2, 7, 2, 4, 9, 1]
salida = eliminar_duplicados(entrada)

print("Entrada:", entrada)
print("Salida: ", salida)