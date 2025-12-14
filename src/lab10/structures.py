from collections import deque


class Stack:
    """Стек (LIFO-Last In First Out) на основе списка"""

    def __init__(self):
        """Внутреннее хранилище стека"""
        self._data = []

    def push(self, item):
        """Добавить элемент на вершину стека (в конец) O(1)"""
        self._data.append(item)

    def pop(self):
        """Снять верхний элемент и вернуть его (удалить из стека) O(1)"""
        if self.is_empty():
            raise IndexError("Нельзя удалить из пустого стека")
        return self._data.pop()  ## pop() - удаляет с конца, pop(0) - удаляет с начала

    def peek(self):
        """Вернуть верхний элемент без удаления. O(1)"""
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self):
        """Проверить, пуст ли стек. O(1)"""
        return len(self._data) == 0

    def __len__(self):
        """Количество элементов в стеке. O(1)"""
        return len(self._data)

    def __repr__(self):
        return f"Stack({self._data})"


class Queue:
    """Очередь (FIFO-First In First Out)"""

    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        """Добавить элемент в конец очереди. O(1)"""
        self._data.append(item)

    def dequeue(self):
        """Взять элемент из начала очереди и удалить. O(1)"""
        if self.is_empty():
            raise IndexError("Нельзя удалить из пустой очереди")
        return self._data.popleft()

    def peek(self):
        """Вернуть первый элемент без удаления. O(1)"""
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self):
        """Проверить, пуста ли очередь. O(1)"""
        return len(self._data) == 0

    def __len__(self):
        """Количество элементов в очереди. O(1)"""
        return len(self._data)

    def __repr__(self):
        return f"Queue({list(self._data)})"
