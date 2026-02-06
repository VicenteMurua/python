# Casos de Uso de Stacks

Un **stack** (pila) es una estructura de datos LIFO (Last In, First Out), donde el último elemento agregado es el primero en salir.  
Se utiliza en muchos contextos en programación y aplicaciones reales.

---

## 1. Validación de expresiones

- Paréntesis, llaves y corchetes balanceados.
- Expresiones matemáticas: conversión de notación infija → posfija.
- Ejemplo: `"([]{})"` → balanceado.

---

## 2. Deshacer / Rehacer (Undo / Redo)

- Aplicaciones de texto, editores gráficos o hojas de cálculo.
- Cada acción se almacena en el stack y se puede revertir sacando del tope.

---

## 3. Historial de navegación

- Navegadores web: botón “Atrás”.
- Aplicaciones con pantallas navegables: guardan historial de estados.

---

## 4. Recursión simulada

- Stack de ejecución de funciones.
- Permite transformar recursión en iteración usando un stack manual.

---

## 5. Evaluación de expresiones y calculadoras

- Convertir y evaluar expresiones matemáticas posfijas.
- Algoritmo “Shunting Yard” de Dijkstra.

---

## 6. Algoritmos de recorrido de grafos

- DFS (Depth-First Search) usa un stack.
- Backtracking en laberintos o puzzles.

---

## 7. Manejo de memoria

- Stack de llamadas (call stack) para funciones.
- Guarda variables locales y direcciones de retorno.

---

## 8. Backtracking y puzzles

- Resolver laberintos, Sudoku, problemas combinatorios.
- Guardar estados anteriores y retroceder si falla.

---

## 9. Procesamiento de texto

- Parsing de lenguajes de programación.
- Matching de etiquetas HTML/XML.

---

### Nota

Cualquier problema que requiera **guardar un historial de pasos o estados y luego retroceder** se puede resolver con un stack. La clave: **LIFO (Last In, First Out)**.
