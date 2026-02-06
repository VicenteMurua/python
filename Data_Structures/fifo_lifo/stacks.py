"""
stacks.py

Definición de una pila (stack) y sus métodos clásicos.
"""

class Stack:
    """Clase que representa una pila (LIFO: Last In, First Out)."""

    def __init__(self):
        """Inicializa la pila vacía."""
        self._items = []

    def __repr__(self):
        """Devuelve la representacion de la pila."""
        return f"{self.__class__.__name__} {str(self._items)}"

    def push(self, item):
        """
        Agrega un elemento al tope de la pila.

        Args:
            item: Elemento a agregar.
        """
        self._items.append(item)

    def pop(self):
        """
        Saca y devuelve el elemento del tope de la pila.
        Lanza IndexError si la pila está vacía.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """
        Devuelve el elemento del tope sin sacarlo.
        Lanza IndexError si la pila está vacía.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """Devuelve True si la pila está vacía, False si tiene elementos."""
        return len(self._items) == 0

    def size(self):
        """Devuelve la cantidad de elementos en la pila."""
        return len(self._items)

    def clear(self):
        """Vacía la pila completamente."""
        self._items.clear()


# Ejemplo rápido de uso:
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print(stack.peek())  # 20
    print(stack.pop())   # 20
    print(stack.size())  # 1
