# Ejercicio 2
# Enunciado
# Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
# Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

# Solucion
for i in range(1, 16):
    if i % 2 != 0:
        print(f"{i}")