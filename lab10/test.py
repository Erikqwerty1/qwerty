from structures import Stack, Queue
from linked_list import SinglyLinkedList

# Тест Stack
print("Тест Stack")
s = Stack()

# Проверяем пустой стек
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
