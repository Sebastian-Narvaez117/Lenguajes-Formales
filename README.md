# Lenguajes-Formales
# Teoría de Autómatas - Práctica 2

Aplicación web en Python para trabajar operaciones de lenguajes formales de manera visual.

El proyecto permite generar cadenas, validar pertenencia, calcular unión y concatenación, aplicar Kleene estrella y Kleene plus, y analizar el crecimiento del lenguaje por iteraciones.

## Vista general

Esta práctica está orientada al estudio de conceptos de Lenguajes Formales con una interfaz web simple y clara:

- Backend con Flask.
- Interfaz en HTML con Bootstrap y estilos personalizados.
- Resultados mostrados como chips horizontales con ajuste automático de línea.
- Soporte visual para la cadena vacía usando el símbolo ε.

## Funcionalidades

1. Generar cadenas
   - Genera cadenas a partir de un alfabeto y una longitud máxima.
   - Incluye la cadena vacía.
     <img width="1919" height="969" alt="image" src="https://github.com/user-attachments/assets/c0d7fef8-4a44-4bfe-9d6c-fa121d23ef07" />


2. Pertenencia
   - Verifica si una cadena pertenece a un lenguaje.
     <img width="1919" height="969" alt="image" src="https://github.com/user-attachments/assets/c493f3a2-08f7-4fb4-a8bb-6d38b6d3dbca" />


3. Unión
   - Combina dos lenguajes evitando duplicados.
     <img width="1919" height="969" alt="image" src="https://github.com/user-attachments/assets/7f266e06-1ac7-4dc3-aaab-3ffbe5815a45" />


4. Concatenación
   - Realiza el producto concatenado entre los elementos de dos lenguajes.
     <img width="1919" height="969" alt="image" src="https://github.com/user-attachments/assets/79998eea-34f4-4700-a280-c36fe55a9f4f" />


5. Kleene estrella
   - Calcula L* hasta un número de iteraciones definido.
      <img width="1919" height="969" alt="image" src="https://github.com/user-attachments/assets/e0ecce7c-e8b7-441d-864c-75a2fb0ac9ce" />
 

     

6. Kleene plus
   - Calcula L+ hasta un número de iteraciones (sin incluir ε).
     <img width="1919" height="969" alt="image" src="https://github.com/user-attachments/assets/b97c7309-df27-4563-8ec6-c312fc2664de" />
  
     


7. Analizar crecimiento
   - Muestra por iteración la cantidad de cadenas y su contenido.
     <img width="1919" height="969" alt="image" src="https://github.com/user-attachments/assets/520a57ed-6738-42ef-be3d-97580fa37b37" />


## Estructura del proyecto

    teoriaAutomatas/
    ├── README.md
    └── practica2/
        ├── Front.py
        ├── Problemas.py
        ├── PRUEBAS.md
        ├── Codigos ejecutables/
        │   ├── Analizar_crecimiento.py
        │   ├── Cadenas.py
        │   ├── Concatenacion.py
        │   ├── Kleene_plus.py
        │   ├── Kleene_star.py
        │   ├── Pertenecia.py
        │   └── Union.py
        └── templates/
            └── index.html

## Requisitos

- Python 3.10 o superior
- Flask

## Instalación

1. Clonar el repositorio.
2. Entrar al directorio del proyecto.
3. Crear y activar entorno virtual (opcional, recomendado).
4. Instalar dependencias.

Comandos sugeridos en Linux/macOS:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install flask

## Ejecutar la aplicación web

Desde la carpeta practica2:

    python Front.py

Luego abrir en el navegador:

    http://127.0.0.1:5000/

## Cómo usar la app

La interfaz está organizada en tres pestañas:

- Generar
  - Entrada: alfabeto (ejemplo: a,b) y longitud máxima.

- Operaciones
  - Entrada: Lenguaje 1, Lenguaje 2 y cadena.
  - Acciones: Pertenece, Unión, Concatenación.

- Kleene
  - Entrada: lenguaje e iteraciones.
  - Acciones: Kleene *, Kleene +, Analizar crecimiento.

Formato de entrada recomendado para lenguajes:

    a,b,ab,ba

## Scripts individuales

En la carpeta Codigos ejecutables hay scripts separados por operación para pruebas directas desde consola:

- Cadenas.py
- Pertenecia.py
- Union.py
- Concatenacion.py
- Kleene_star.py
- Kleene_plus.py
- Analizar_crecimiento.py

## Casos de prueba

Se documentaron casos de prueba para todas las operaciones en:

- practica2/PRUEBAS.md

Incluye ejemplos de entrada/salida para:

- Generar cadenas
- Pertenencia
- Unión
- Concatenación
- Kleene estrella
- Kleene plus
- Crecimiento

## Decisiones de implementación

- La cadena vacía se representa internamente como cadena vacía de Python y visualmente como ε.
- Los resultados de tipo lista se muestran ordenados por longitud y luego alfabéticamente para facilitar lectura.
- El análisis de crecimiento presenta bloques por iteración con contador de elementos.

## Próximas mejoras sugeridas

- Archivo requirements.txt para instalación reproducible.
- Tests automatizados con pytest.
- Exportar resultados a archivo.
- Validación de entrada más estricta para símbolos especiales.

## Autor

Joseph Sebastian Narvaez Quezada
