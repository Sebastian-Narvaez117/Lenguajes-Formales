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


# Ejemplo de uso
if __name__ == "__main__":
    alfabeto = ['a', 'b']
    max_len = 2
    cadenas = generar_cadenas(alfabeto, max_len)
    print(cadenas)  # Output: ['', 'a', 'b', 'aa', 'ab', 'ba', 'bb']