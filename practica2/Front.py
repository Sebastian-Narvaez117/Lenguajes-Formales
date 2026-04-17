from flask import Flask, render_template, request

app = Flask(__name__)

# -------- FUNCIONES --------

def parse_lista(texto):
    return [x.strip() for x in texto.split(",") if x.strip()]


def generar_cadenas(alfabeto, max_len):
    resultado = [""]

    for _ in range(max_len):
        nuevas = []
        for cadena in resultado:
            for simbolo in alfabeto:
                nuevas.append(cadena + simbolo)
        resultado += nuevas

    return list(set(resultado))


def pertenece(cadena, lenguaje):
    return cadena in lenguaje


def union(L1, L2):
    return list(set(L1 + L2))


def concatenacion(L1, L2):
    return [x + y for x in L1 for y in L2]


def kleene_star(L, max_iter):
    resultado = [""]
    actual = [""]

    for _ in range(max_iter):
        nuevo = []
        for x in actual:
            for y in L:
                nuevo.append(x + y)

        resultado = list(set(resultado + nuevo))
        actual = nuevo

    return resultado


def kleene_plus(L, max_iter):
    return [x for x in kleene_star(L, max_iter) if x != ""]


def analizar_crecimiento(L, max_iter=5):
    lineas = []

    for i in range(1, max_iter + 1):
        resultado = kleene_star(L, i)
        resultado_ordenado = sorted(resultado, key=lambda x: (len(x), x))
        lineas.append(f"Iteracion: {i}")
        lineas.append(f"Cantidad: {len(resultado)}")
        lineas.append("Crecimiento:")
        for cadena in resultado_ordenado:
            lineas.append(f"  {cadena!r}")
        lineas.append("")

    return "\n".join(lineas)




def formatear_resultado(valor):
    if isinstance(valor, bool):
        return str(valor)

    if isinstance(valor, list):
        if not valor:
            return "[]"

        lista_visual = formatear_lista_visual(valor)
        textos = [item["text"] for item in lista_visual]
        return "[" + ", ".join(textos) + "]"

    return str(valor)


def formatear_lista_visual(valor):
    valor_ordenado = sorted(valor, key=lambda elemento: (len(str(elemento)), str(elemento)))
    resultado = []
    for elemento in valor_ordenado:
        texto = "ε" if elemento == "" else repr(elemento)
        longitud = len(elemento) if elemento != "" else 0
        resultado.append({"text": texto, "length": longitud})
    return resultado


def formatear_crecimiento_visual(L, max_iter):
    bloques = []

    for i in range(1, max_iter + 1):
        cadenas = kleene_star(L, i)
        bloques.append({
            "iteracion": i,
            "cantidad": len(cadenas),
            "cadenas": formatear_lista_visual(cadenas),
        })

    return bloques


# -------- RUTA --------

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    resultado_lista = []
    resultado_crecimiento = []
    active_tab = "generar"

    datos = {
        "L1": "",
        "L2": "",
        "cadena": "",
        "n": ""
    }

    if request.method == "POST":
        op = request.form.get("operacion")

        # guardar datos para no perderlos
        datos["L1"] = request.form.get("L1", "")
        datos["L2"] = request.form.get("L2", "")
        datos["cadena"] = request.form.get("cadena", "")
        datos["n"] = request.form.get("n", "")

        try:
            L1 = parse_lista(datos["L1"])
            L2 = parse_lista(datos["L2"])
            cadena = datos["cadena"]
            n = int(datos["n"]) if datos["n"] else 2

            if op == "generar":
                resultado = generar_cadenas(L1, n)
                active_tab = "generar"

            elif op == "pertenece":
                resultado = pertenece(cadena, L1)
                active_tab = "operaciones"

            elif op == "union":
                resultado = union(L1, L2)
                active_tab = "operaciones"

            elif op == "concat":
                resultado = concatenacion(L1, L2)
                active_tab = "operaciones"

            elif op == "kleene":
                resultado = kleene_star(L1, n)
                active_tab = "kleene"

            elif op == "plus":
                resultado = kleene_plus(L1, n)
                active_tab = "kleene"

            elif op == "crecimiento":
                resultado = analizar_crecimiento(L1, n)
                resultado_crecimiento = formatear_crecimiento_visual(L1, n)
                active_tab = "kleene"

            if isinstance(resultado, list):
                resultado_lista = formatear_lista_visual(resultado)

            resultado = formatear_resultado(resultado)

        except Exception as e:
            resultado = f"Error: {e}"
            resultado_lista = []
            resultado_crecimiento = []

    return render_template(
        "index.html",
        resultado=resultado,
        resultado_lista=resultado_lista,
        resultado_crecimiento=resultado_crecimiento,
        active_tab=active_tab,
        datos=datos
    )

if __name__ == "__main__":
    app.run(debug=True)