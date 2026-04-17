from Kleene_star import kleene_star


# 6. Kleene Plus
def kleene_plus(L, max_iter):
    ks = kleene_star(L, max_iter)
    resultado = []

    for elem in ks:
        if elem != "":
            resultado.append(elem)

    return resultado

# Ejemplo de uso
if __name__ == "__main__":
    lenguaje = ["a", "b"]
    max_iteraciones = 3
    resultado = kleene_plus(lenguaje, max_iteraciones)
    print("Kleene Plus de", lenguaje, "con máximo de iteraciones", max_iteraciones, "es:")
    print(resultado)