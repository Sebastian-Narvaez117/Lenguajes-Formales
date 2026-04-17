# 4. Concatenación
def concatenacion(L1, L2):
    resultado = []
    for x in L1:
        for y in L2:
            resultado.append(x + y)
    return resultado

# Ejemplo de uso
L1 = ["a", "b"]
L2 = ["c", "d"]
print(concatenacion(L1, L2))  # Output: ['ac', 'ad', 'bc', 'bd']