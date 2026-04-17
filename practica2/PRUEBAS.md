# Documentación de Pruebas - Lenguajes Formales

## 1. GENERAR CADENAS

### Prueba 1: Alfabeto simple, longitud pequeña
**Entrada:**
- Alfabeto: `a,b`
- Longitud: `1`

**Salida esperada:**
```
[ε, 'a', 'b']
```

**Explicación:** Genera la cadena vacía y todas las cadenas de longitud 1 con el alfabeto {a, b}.

---

### Prueba 2: Alfabeto simple, longitud 2
**Entrada:**
- Alfabeto: `a,b`
- Longitud: `2`

**Salida esperada:**
```
[ε, 'a', 'b', 'aa', 'ab', 'ba', 'bb']
```

**Explicación:** Genera cadenas vacía y de longitud 1 y 2.

---

## 2. OPERACIÓN: PERTENECE

### Prueba 1: Cadena pertenece al lenguaje
**Entrada:**
- Lenguaje 1: `a,b,ab,ba`
- Cadena: `ab`

**Salida esperada:**
```
True
```

**Explicación:** La cadena 'ab' existe en el lenguaje.

---

### Prueba 2: Cadena NO pertenece al lenguaje
**Entrada:**
- Lenguaje 1: `a,b,ab,ba`
- Cadena: `aaa`

**Salida esperada:**
```
False
```

**Explicación:** La cadena 'aaa' no existe en el lenguaje.

---

## 3. OPERACIÓN: UNIÓN

### Prueba 1: Unión de dos lenguajes
**Entrada:**
- Lenguaje 1: `a,ab`
- Lenguaje 2: `b,ba`

**Salida esperada:**
```
['a', 'ab', 'b', 'ba']
```

**Explicación:** Combina todos los elementos de L1 y L2 sin duplicados, ordenados por longitud.

---

## 4. OPERACIÓN: CONCATENACIÓN

### Prueba 1: Concatenación simple
**Entrada:**
- Lenguaje 1: `a,b`
- Lenguaje 2: `c,d`

**Salida esperada:**
```
['ac', 'ad', 'bc', 'bd']
```

**Explicación:** Concatena cada elemento de L1 con cada elemento de L2.

---

### Prueba 2: Concatenación con vacío
**Entrada:**
- Lenguaje 1: `ε,a`
- Lenguaje 2: `b,c`

**Salida esperada:**
```
['b', 'c', 'ab', 'ac']
```

**Explicación:** El producto cartesiano, donde ε concatenado con algo da lo mismo.

---

## 5. OPERACIÓN: KLEENE STAR (*)

### Prueba 1: Kleene star básico
**Entrada:**
- Lenguaje: `a`
- Iteraciones: `2`

**Salida esperada:**
```
[ε, 'a', 'aa']
```

**Explicación:** L* = {ε} ∪ L ∪ L·L ∪ ... (hasta 2 iteraciones).

---

### Prueba 2: Kleene star con dos símbolos
**Entrada:**
- Lenguaje: `a,b`
- Iteraciones: `2`

**Salida esperada:**
```
[ε, 'a', 'b', 'aa', 'ab', 'ba', 'bb']
```

**Explicación:** Todas las combinaciones posibles de a y b hasta longitud 2.

---

## 6. OPERACIÓN: KLEENE PLUS (+)

### Prueba 1: Kleene plus (sin epsilon)
**Entrada:**
- Lenguaje: `a`
- Iteraciones: `2`

**Salida esperada:**
```
['a', 'aa']
```

**Explicación:** L+ = L ∪ L·L ∪ ... (igual a Kleene star pero sin ε).

---

### Prueba 2: Kleene plus con dos símbolos
**Entrada:**
- Lenguaje: `a,b`
- Iteraciones: `2`

**Salida esperada:**
```
['a', 'b', 'aa', 'ab', 'ba', 'bb']
```

**Explicación:** Lo mismo que Kleene star pero sin la cadena vacía.

---

## 7. OPERACIÓN: ANALIZAR CRECIMIENTO

### Prueba 1: Crecimiento con un símbolo
**Entrada:**
- Lenguaje: `a`
- Iteraciones: `3`

**Salida esperada:**
```
Iteracion: 1
Cantidad: 2
Crecimiento:
  ε
  'a'

Iteracion: 2
Cantidad: 3
Crecimiento:
  ε
  'a'
  'aa'

Iteracion: 3
Cantidad: 4
Crecimiento:
  ε
  'a'
  'aa'
  'aaa'
```

**Explicación:** Muestra cómo crece el lenguaje en cada iteración del Kleene star.

---

## CASOS DE PRUEBA RÁPIDOS (Copy-Paste)

### Test 1: Generar cadenas
- **Alfabeto:** `a,b`  
- **Longitud:** `2`

### Test 2: Pertenencia (True)
- **L1:** `a,b,ab,ba,aba`  
- **Cadena:** `aba`

### Test 3: Pertenencia (False)
- **L1:** `a,b,ab,ba`  
- **Cadena:** `bbb`

### Test 4: Unión
- **L1:** `a,aa`  
- **L2:** `b,bb`

### Test 5: Concatenación
- **L1:** `a,b`  
- **L2:** `x,y,z`

### Test 6: Kleene Star
- **Lenguaje:** `a,b`  
- **Iteraciones:** `2`

### Test 7: Kleene Plus
- **Lenguaje:** `a,b`  
- **Iteraciones:** `2`

### Test 8: Crecimiento
- **Lenguaje:** `a,b`  
- **Iteraciones:** `3`

