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


# Ejemplo de uso
if __name__ == "__main__":
    lenguaje = ["a", "b"]
    max_iteraciones = 3
    resultado = kleene_star(lenguaje, max_iteraciones)
    print("Kleene Star de", lenguaje, "con máximo de iteraciones", max_iteraciones, "es:")
    print(resultado)