# 2. Pertenencia
def pertenece(cadena, lenguaje):
    for elem in lenguaje:
        if elem == cadena:
            return True
    return False

# Ejemplo de uso
if __name__ == "__main__":
    lenguaje = ["hola", "mundo", "python"]
    cadena1 = "hola"
    cadena2 = "java"

    print(pertenece(cadena1, lenguaje))  # Debería imprimir: True
    print(pertenece(cadena2, lenguaje))  # Debería imprimir: False