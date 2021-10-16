'''
Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. 
La primera con los números pares, 
y la segunda con los números impares

'''
lista_ingresada = []

def separar(lista_numeros):
    lista_pares = []
    lista_impares = []
    for i in lista_numeros:
        if i % 2 == 0:
            lista_pares.append(i)
        else:
            lista_impares.append(i)
    lista_impares.sort()
    lista_pares.sort()
    return [lista_impares,lista_pares]

# Inicio funcion para convertir los datos a numeros
def convertir(dato):
	while dato.isnumeric() == False: # Mientras que el dato del numero no sea un numero
		print("¡Lo ingresado no es un número!")
		dato = input("Ingrese el dato nuevamente: ") # Se pide nuevamente el dato
	dato = int(dato) # Se convierte el dato 
	return dato

while True:
    print("Desea ingresar un numero:\n1.Si\n2.No")
    opcion = int(input())
    if opcion == 1:
        numero_a_ingresar = input("Ingrese el numero: ")
        numero_a_ingresar = convertir(numero_a_ingresar)
        lista_ingresada.append(numero_a_ingresar)
    elif opcion == 2:
        listas_devueltas = separar(lista_ingresada)
        print(listas_devueltas)
        print("La lista impar es: {}\nLa lista par es: {}".format(listas_devueltas[0],listas_devueltas[1]))
        break
    else:
        print("Ingreso opcion incorrecta")







