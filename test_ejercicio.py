import ejercicio

def test_convertir_lista_a_tupla():
    compras = "manzanas, plátanos, leche, pan"
    productos = compras.split(", ")
    tupla_productos = ejercicio.convertir_lista_a_tupla(productos)
    assert isinstance(tupla_productos, tuple)
    assert tupla_productos == ('manzanas', 'plátanos', 'leche', 'pan') 

test_convertir_lista_a_tupla()
