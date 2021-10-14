'''
Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio:

Comprueba el punto intermedio entre -12 y 24

'''

# Inicio la funcion
def intermedio (num1,num2):
    nro_intermedio = (num1 + num2) / 2 # Realizo el calculo de numero intermedio
    return nro_intermedio # Devuelvo el numero intermedio

# Inicio funcion para convertir los datos a numeros
def convertir(dato):
	while dato.isnumeric() == False: # Mientras que el dato del numero no sea un numero
		print("¡Lo ingresado no es un número!")
		dato = input("Ingrese el dato nuevamente: ") # Se pide nuevamente el dato
	dato = int(dato) # Se convierte el dato 
	return dato

# Se ingresa el primer valor
num_1_ingresado = input("Ingrese el primer numero: \n")
num_1_ingresado = convertir(num_1_ingresado)

# Se ingresa el segundo valor
num_2_ingresado = input("Ingrese el segundo numero: \n")
num_2_ingresado = convertir(num_2_ingresado)

# Muestra el resultado
print(intermedio(num_1_ingresado,num_2_ingresado))

