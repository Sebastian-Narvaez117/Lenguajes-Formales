from Kleene_star import kleene_star

# 7. Crecimiento
def analizar_crecimiento(L):
    for i in range(1, 6):
        resultado = kleene_star(L, i)
        print(f"Iteración: {i}")
        print(f"Cantidad: {len(resultado)}")


# Ejemplo de uso
if __name__ == "__main__":
    L = ["a", "b"]
    analizar_crecimiento(L)