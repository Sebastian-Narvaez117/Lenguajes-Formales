# 3. Unión
def union(L1, L2):
    resultado = L1.copy()
    for elem in L2:
        if elem not in resultado:
            resultado.append(elem)
    return resultado


# Ejemplo de uso
L1 = ["a", "b", "c"]
L2 = ["b", "c", "d"]
resultado_union = union(L1, L2)
print("Unión de L1 y L2:", resultado_union)
