# Ejercicio 1 sesion 4
# Autor: Jonatan

#Enunciado
# Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
edad = int(input("Ingrese su edad: "))

# verificar que ingrese una valida
if edad < 0 or edad > 100:
    print("Ingese una edad valida")
elif edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
