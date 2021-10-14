'''
Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. 
Calcula el área de un círculo de 5 de radio
'''

# Inicio la funcion pedida
def area_circulo(radio):
    constante_pi = 3.14159 # Coloco la constante pi
    area_total = constante_pi * radio * radio # Calculo el area total
    return area_total # Retorno el area total del circulo

# Inicio funcion para convertir los datos a numeros
def convertir(dato):
	while dato.isnumeric() == False: # Mientras que el dato del numero no sea un numero
		print("¡Lo ingresado no es un número!")
		dato = input("Ingrese el dato nuevamente: ") # Se pide nuevamente el dato
	dato = int(dato) # Se convierte el dato 
	return dato

# Se ingresa el radio
radio_ingresado = input("Ingrese el radio: \n")
radio_ingresado = convertir(radio_ingresado)

# Se muestra el resultado del area
print("El area total del circulo es", area_circulo(radio_ingresado)) # Imprimo el valor pedido