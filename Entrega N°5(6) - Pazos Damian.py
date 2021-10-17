'''
Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. 
La primera con los números pares, 
y la segunda con los números impares

'''

# Ingreso una lista vacia para ingresar los numeros.
lista_ingresada = []

# Inicia la funcion pedida
def separar(lista_numeros):
    # Declaro dos listas vacias para almacenar los datos de numero pares e impares.
    lista_pares = []
    lista_impares = []
    # Recorro la lista ingresada en la funcion.
    for i in lista_numeros:
        # Separo los numeros por pares e impares y luego los agrego a la lista corespondiente.
        if i % 2 == 0:
            lista_pares.append(i)
        else:
            lista_impares.append(i)
    # Ordeno de menor a mayor ambas listas
    lista_impares.sort()
    lista_pares.sort()
    return [lista_impares,lista_pares] # Devuelvo una lista que contiene ambas listas

# Inicio funcion para convertir los datos a numeros
def convertir(dato):
	while dato.isnumeric() == False: # Mientras que el dato del numero no sea un numero
		print("¡Lo ingresado no es valido!")
		dato = input("Ingrese el dato nuevamente: ") # Se pide nuevamente el dato
	dato = int(dato) # Se convierte el dato 
	return dato

# Inicio un While para el ingreso de numeros con un mini menu de opcion.
while True:
    print("Desea ingresar un numero:\n1.Si\n2.No")
    opcion = convertir(input())
    if opcion == 1: # Opcion de ingresar numero
        numero_a_ingresar = input("Ingrese el numero: ")
        numero_a_ingresar = convertir(numero_a_ingresar)
        lista_ingresada.append(numero_a_ingresar)
    elif opcion == 2: # Opcion de no ingresar mas numeros
        listas_devueltas = separar(lista_ingresada)
        print(listas_devueltas)
        print("La lista impar es: {}\nLa lista par es: {}".format(listas_devueltas[0],listas_devueltas[1]))
        break
    else: # Opcion incorrecta
        print("Ingreso opcion incorrecta")







