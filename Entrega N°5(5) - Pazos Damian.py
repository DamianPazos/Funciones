'''
Realizá una función llamada recortar() que reciba tres parámetros. 
El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. 
La función tendrá que cumplir lo siguiente:

1.	Devolver el límite inferior si el número es menor que éste
2.	Devolver el límite superior si el número es mayor que éste.
3.	Devolver el número sin cambios si no se supera ningún límite.
Comprueba el resultado de recortar 15 entre los límites 0 y 10

'''

# Inicio la funcion recortar
def recortar (recorte,lim_inferior,lim_superior): 
    # Se verifica que el limite inferior sea menor al limite superior
    if lim_inferior < lim_superior:
        # Se verifica si el numero de recorte se encuentra entre los limites
        if lim_inferior < recorte < lim_superior:
            return recorte # Se retorna el valor
        # Se verifica si el numero de recorte es mayor al limite superior
        elif recorte > lim_superior:
            return lim_superior # Se retorna el valor
        # Se verifica si el numero de recorte es menor al limite inferior
        elif recorte < lim_inferior:
            return lim_inferior # Se retorna el valor
    else:
        return "El limite inferior debe ser menor al limite superior" # Si el valor del limite inferior es mayor al superior devuelve el siguiente mensaje

# Inicio funcion para convertir los datos a numeros
def convertir(dato):
	while dato.isnumeric() == False: # Mientras que el dato del numero no sea un numero
		print("¡Lo ingresado no es un número!")
		dato = input("Ingrese el dato nuevamente: ") # Se pide nuevamente el dato
	dato = int(dato) # Se convierte el dato 
	return dato

# Se ingresa el valor a recortar
num_a_recortar = input("Ingrese el numero a recortar: \n")
num_a_recortar = convertir(num_a_recortar)

# Se ingresa el limite inferior
num_lim_inf = input("Ingrese el limite inferior: \n")
num_lim_inf = convertir(num_lim_inf)

# Se ingresa el limite superior
num_lim_sup = input("Ingrese el limite superior: \n")
num_lim_sup = convertir(num_lim_sup)

print(recortar(num_a_recortar,num_lim_inf,num_lim_sup))  # Se imprime el uso de la funcion