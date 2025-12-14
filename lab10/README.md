##Лабароторная работа №10

#Теория

Стек (Stack)

    Принцип: LIFO — Last In, First Out.

    Операции:
        push(x) — положить элемент сверху;
        pop() — снять верхний элемент;
        peek() — посмотреть верхний, не снимая.

    Типичные применения:
        история действий (undo/redo);
        обход графа/дерева в глубину (DFS);
        парсинг выражений, проверка скобок.

    Асимптотика (при реализации на массиве / списке):
        push — O(1) амортизированно;
        pop — O(1);
        peek — O(1);
        проверка пустоты — O(1).

    Пример:
```py
s = Stack()
s.push(10)
s.push(20)

print(s.pop())   # 20
print(s.peek())  # 10
print(s.is_empty())  # False
```

Очередь (Queue)

    Принцип: FIFO — First In, First Out.

    Операции:
        enqueue(x) — добавить в конец;
        dequeue() — взять элемент из начала;
        peek() — посмотреть первый элемент, не удаляя.

    Типичные применения:
        обработка задач по очереди (job queue);
        обход графа/дерева в ширину (BFS);
        буферы (сетевые, файловые, очереди сообщений).

    В Python:
        обычный list плохо подходит для реализации очереди:
            удаление с начала pop(0) — это O(n) (все элементы сдвигаются);
        collections.deque даёт O(1) операции по краям:
            append / appendleft — O(1);
            pop / popleft — O(1).

    Асимптотика (на нормальной очереди):
        enqueue — O(1);
        dequeue — O(1);
        peek — O(1).

    Пример:
```py
q = Queue()
q.enqueue("A")
q.enqueue("B")

print(q.dequeue())  # A
print(q.peek())     # B
print(q.is_empty()) # False
```
Односвязный список (Singly Linked List)

    Структура:
        состоит из узлов Node;
        каждый узел хранит:
            value — значение элемента;
            next — ссылку на следующий узел или None (если это последний).

    Основные идеи:
        элементы не хранятся подряд в памяти, как в массиве;
        каждый элемент знает только «следующего соседа».

    Плюсы:
        вставка/удаление в начало списка за O(1):
            если есть ссылка на голову (head), достаточно перенаправить одну ссылку;
        при удалении из середины не нужно сдвигать остальные элементы:
            достаточно обновить ссылки узлов;
        удобно использовать как базовый строительный блок для других структур (например, для очередей, стеков, хеш-таблиц с цепочками).

    Минусы:
        доступ по индексу i — O(n):
            чтобы добраться до позиции i, нужно пройти i шагов от головы;
        нет быстрого доступа к предыдущему элементу:
            чтобы удалить узел, нужно знать его предыдущий узел → часто нужен дополнительный проход.

    Типичные оценки:
        prepend (добавить в начало) — O(1);
        append:
            при наличии tail — O(1),
            без tail — O(n), т.к. требуется пройти до конца;
        поиск по значению — O(n).

    Пример:
```py
sll = SinglyLinkedList()
sll.prepend(10)
sll.prepend(20)
sll.prepend(30)

sll.print_list()
# Вывод: 30 -> 20 -> 10 -> None

node = sll.find(20)
print(node.value if node else "Not found")  # 20
```

Двусвязный список (Doubly Linked List)

Структура:

    также состоит из узлов DNode;
    каждый узел хранит:
        value — значение элемента;
        next — ссылку на следующий узел;
        prev — ссылку на предыдущий узел.

Основные идеи:

    можно двигаться как вперёд, так и назад по цепочке узлов;
    удобно хранить ссылки на оба конца: head и tail.

Плюсы по сравнению с односвязным:

    удаление узла по ссылке на него — O(1):
        достаточно «вытащить» его, перенастроив prev.next и next.prev;
        не нужно искать предыдущий узел линейным проходом;
    эффективен для структур, где часто нужно удалять/добавлять элементы в середине, имея на них прямые ссылки (например, реализация LRU-кэша);
    можно легко идти в обе стороны:
        прямой и обратный обход списка.

Минусы:

    узел занимает больше памяти:
        нужно хранить две ссылки (prev, next);
    код более сложный:
        легко забыть обновить одну из ссылок и «сломать» структуру;
    сложнее отлаживать.

Типичные оценки (при наличии head и tail):

    вставка/удаление в начале/конце — O(1);
    вставка/удаление по ссылке на узел — O(1);
    доступ по индексу — O(n) (нужно идти от головы или хвоста);
    поиск по значению — O(n).

Пример:
```py
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)

dll.print_forward()
# Вывод: 10 <-> 20 <-> 30 <-> None

dll.print_backward()
# Вывод: 30 <-> 20 <-> 10 <-> None
```

Пример текстовой визуализации:

```py
None <- [A] <-> [B] <-> [C] -> None
```

Выводы по бенчмаркам:
1.Очередь на deque работает быстрее, чем очередь на list
     - deque.popleft() выполняется за O(1)
     - list.pop(0) выполняется за O(n), так как требует сдвига элементов
2.Стек на list является эффективным
     - операции append и pop с конца списка выполняются за O(1)
3.Связные списки
     - выгодны при частых вставках и удалениях
     - проигрывают массивам по скорости доступа к элементам

#Задание 1
```py
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
```

#Задание 2
```py
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        # размер начинается с 0
        self._size = 0

    def append(self, value):
        """Добавить элемент в конец списка O(n)"""
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def prepend(self, value):
        """Добавить элемент в начало списка O(1)"""
        # Создаем новый узел, который указывает на текущую голову
        new_node = Node(value, next=self.head)
        if self._size == 0:
            self.tail = new_node
        self.head = new_node
        self._size += 1

    def insert(self, idx, value):
        """Вставка по индексу O(n)"""
        # Проверяем, что индекс в допустимых пределах
        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size}]")

        # Если вставляем в начало
        if idx == 0:
            self.prepend(value)
            return

        if idx == self._size:
            self.append(value)
            return

        # Ищем позицию для вставки
        current = self.head
        # Переходим к узлу перед нужной позицией
        for _ in range(idx - 1):
            current = current.next

        # Вставляем новый узел
        new_node = Node(value, next=current.next)
        current.next = new_node

        # ИСПРАВЛЕНО: увеличиваем размер
        self._size += 1

    def __iter__(self):
        """Итератор по значениям списка"""
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        """Возвращает количество элементов O(1)"""
        return self._size

    def __repr__(self):
        """Строковое представление списка"""
        values = list(self)
        return f"SinglyLinkedList({values})"
```
Код теста:
from structures import Stack, Queue
from linked_list import SinglyLinkedList

print("Тест Stack")
s = Stack()

print("1. Пустой стек:")
print(f"   is_empty = {s.is_empty()}")  # True
print(f"   peek = {s.peek()}")  # None
print("2. Добавляем 1, 2, 3:")
s.push(1)
s.push(2)
s.push(3)
print(f"   Стек: {s}")
print(f"   Длина: {len(s)}")  # 3
print(f"   peek = {s.peek()}")  # 3
print("3. Удаляем элементы:")
print(f"   pop = {s.pop()}")  # 3
print(f"   pop = {s.pop()}")  # 2
print(f"   Осталось: {s}")
print("4. Проверка ошибки:")
s.pop()
try:
    s.pop()
except IndexError as e:
    print(f"   Ошибка при pop из пустого стека: {e}")
print("Тест Queue")
q = Queue()
print("1. Пустая очередь:")
print(f"   is_empty = {q.is_empty()}")
print(f"   peek = {q.peek()}")
print("2. Добавляем 'a', 'b', 'c':")
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
print(f"   Очередь: {q}")
print(f"   Длина: {len(q)}")
print(f"   peek = {q.peek()}")
print("3. Удаляем элементы:")
print(f"   dequeue = {q.dequeue()}")
print(f"   dequeue = {q.dequeue()}")
print(f"   Осталось: {q}")
print("4. Проверяем состояние:")
q.enqueue("d")
print(f"   Добавили 'd': {q}")
print(f"   peek = {q.peek()}")
print(f"   is_empty = {q.is_empty()}")
print("5. Проверка ошибки:")
q.dequeue()
q.dequeue()
try:
    q.dequeue()
except IndexError as e:
    print(f"   Ошибка при dequeue из пустой очереди: {e}")
print("Тест SinglyLinkedList")
lst = SinglyLinkedList()
print("1. Пустой список:")
print(f"   Список: {lst}")
print(f"   Длина: {len(lst)}")
print("2. Добавляем в конец (append):")
lst.append(10)
lst.append(20)
lst.append(30)
print(f"   После append: {lst}")
print(f"   Длина: {len(lst)}")  # 3
print("3. Добавляем в начало (prepend):")
lst.prepend(5)
print(f"   После prepend(5): {lst}")
print("4. Вставляем по индексу (insert):")
lst.insert(2, 15)
print(f"   После insert(2, 15): {lst}")
print("5. Проверяем цикл for:")
print("   Элементы:", end=" ")
for x in lst:
    print(x, end=" ")
print()
print("6. Граничные случаи:")
lst.insert(0, 1)
lst.insert(len(lst), 100)
print(f"   После insert в начало и конец: {lst}")
print("7. Проверяем ошибки:")
try:
    lst.insert(-5, 999)
except IndexError as e:
    print(f"   Ошибка при insert(-5): {e}")
try:
    lst.insert(100, 100)
except IndexError as e:
    print(f"   Ошибка при insert(100): {e}")
```
Результаты тестов:

Задание 1

![LABA](./images/01.png)

Задание 2

![LABA](./images/02.png)
