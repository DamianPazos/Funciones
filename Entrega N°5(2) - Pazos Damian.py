'''
Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. 
Calcula el área de un círculo de 5 de radio
'''

# Inicio la funcion pedida
def area_circulo(radio):
    constante_pi = 3.14159 # Coloco la constante pi
    area_total = constante_pi * radio * radio # Calculo el area total
    return area_total # Retorno el area total del circulo

print("El area total del circulo es", area_circulo(5)) # Imprimo el valor pedido


