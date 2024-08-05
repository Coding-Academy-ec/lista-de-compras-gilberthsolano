# Lista de compras
compras = input("Ingrese una lista de compras: ")
productos = compras.split(", ")
print(f"Los productos en la lista de compras son: {productos}")

# Convertir la lista de compras en una tupla
def convertir_lista_a_tupla(lista):
    return tuple(lista)  # Corregido para usar el argumento de la función

tuplas_productos = convertir_lista_a_tupla(productos)
print(f"Los productos en la lista son: {tuplas_productos}")
