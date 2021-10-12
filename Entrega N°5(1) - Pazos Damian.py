'''
Realiza una función llamada area_rectangulo() 
que devuelva el área del rectángulo a partir de una base y una altura. 
Calcula el área de un rectángulo de 15 de base y 10 de altura
'''

def area_rectangulo(base,altura):
    return "El area de un rectangulo es {} metros cuadrados".format(base*altura)

def convertir(dato):
	while dato.isnumeric() == False:
		print("¡Lo ingresado no es un número!")
		dato = input("Ingrese el dato nuevamente: ")
	dato = int(dato)
	return dato

base_ingresada = input("Ingrese la base: \n")
base_ingresada = convertir(base_ingresada)

altura_ingresada = input("Ingrese la altura: \n")
altura_ingresada = convertir(altura_ingresada)

print(area_rectangulo(base_ingresada,altura_ingresada))