# 1. Generar cadenas
def generar_cadenas(alfabeto, max_len):
    resultado = [""]

    for _ in range(max_len):
        nuevas = []
        for cadena in resultado:
            for simbolo in alfabeto:
                nuevas.append(cadena + simbolo)
        resultado += nuevas

    # eliminar duplicados
    final = []
    for elem in resultado:
        if elem not in final:
            final.append(elem)

    return final


# 2. Pertenencia
def pertenece(cadena, lenguaje):
    for elem in lenguaje:
        if elem == cadena:
            return True
    return False


# 3. Unión
def union(L1, L2):
    resultado = L1.copy()
    for elem in L2:
        if elem not in resultado:
            resultado.append(elem)
    return resultado


# 4. Concatenación
def concatenacion(L1, L2):
    resultado = []
    for x in L1:
        for y in L2:
            resultado.append(x + y)
    return resultado


# 5. Kleene Star
def kleene_star(L, max_iter):
    resultado = [""]
    actual = [""]

    for _ in range(max_iter):
        nuevo = []
        for x in actual:
            for y in L:
                nuevo.append(x + y)

        for elem in nuevo:
            if elem not in resultado:
                resultado.append(elem)

        actual = nuevo

    return resultado


# 6. Kleene Plus
def kleene_plus(L, max_iter):
    ks = kleene_star(L, max_iter)
    resultado = []

    for elem in ks:
        if elem != "":
            resultado.append(elem)

    return resultado


# 7. Crecimiento
def analizar_crecimiento(L):
    for i in range(1, 6):
        resultado = kleene_star(L, i)
        print(f"Iteración: {i}")
        print(f"Cantidad: {len(resultado)}")