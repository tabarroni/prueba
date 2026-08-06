def eliminar_duplicados(lista):
    #el sin_duplicados elimina los duplicados manualmente
    sin_duplicados = []
    # Recorremos cada número en la lista original
    for numero in lista:
        # Verificamos manualmente si el número ya está en la lista resultante
        existe = False
        # Recorremos la lista sin_duplicados para comprobar si el número ya existe
        for item in sin_duplicados:
            if item == numero:
                existe = True
                break
        if not existe:
            sin_duplicados.append(numero)

    #ordenar la lista de menor a mayor (Algoritmo Bubble Sort)
    n = len(sin_duplicados)
    # Recorremos la lista varias veces
    for i in range(n):
        for j in range(0, n - i - 1):
            if sin_duplicados[j] > sin_duplicados[j + 1]:
                # Intercambio de valores (swap)
                temp = sin_duplicados[j]
                sin_duplicados[j] = sin_duplicados[j + 1]
                sin_duplicados[j + 1] = temp
    return sin_duplicados
#este es un ejemplo de uso de la función eliminar_duplicados
#entrada = [4, 2, 7, 2, 4, 9, 1]
#entrada = [4, 2, 7, 2, 4, 9, 1,10, 3, 5, 6, 8, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# --- BLOQUE DINÁMICO para entrada de usuario ---
if __name__ == "__main__":
    # Pedimos al usuario que ingrese los números separados por comas o espacios
    entrada_usuario = input("Ingresa una lista de números enteros (separados por espacio o coma): ")

    # Normalizamos la entrada (reemplazamos comas por espacios) y la dividimos en una lista de strings
    elementos = entrada_usuario.replace(',', ' ').split()

    # Convertimos cada string a entero
    entrada = []
    for item in elementos:
        try:
            entrada.append(int(item))
        except ValueError:
            print(f"Advertencia: '{item}' no es un número entero válido y será ignorado.")
salida = eliminar_duplicados(entrada)

print("Entrada:", entrada)
print("Salida: ", salida)