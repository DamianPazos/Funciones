'''
Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

1.	Si el primer número es mayor que el segundo, debe devolver 1.
2.	Si el primer número es menor que el segundo, debe devolver -1.
3.	Si ambos números son iguales, debe devolver un 0.

Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'
'''

# Inicio la funcion con los dos argumentos
def relacion (num_1, num_2):
    if num_1 > num_2: # Si el primer argumento es mayor al segundo
        return 1
    elif num_1 < num_2: # Si el primer argumento es menor al segundo
        return -1
    else: # Si los argumentos son iguales
        return 0

# Inicio funcion para convertir los datos a numeros
def convertir(dato):
	while dato.isnumeric() == False: # Mientras que el dato del numero no sea un numero
		print("¡Lo ingresado no es un número!")
		dato = input("Ingrese el dato nuevamente: ") # Se pide nuevamente el dato
	dato = int(dato) # Se convierte el dato 
	return dato

# Se ingresa el primer valor
num_1_ingresado = input("Ingrese el primer numero")
num_1_ingresado = convertir(num_1_ingresado)

# Se ingresa el segundo valor
num_2_ingresado = input("Ingrese el segundo numero")
num_2_ingresado = convertir(num_2_ingresado)

# Muestra el resultado
print(relacion(num_1_ingresado,num_2_ingresado))