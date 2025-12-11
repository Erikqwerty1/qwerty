import sys
from pathlib import Path

sys.path.append("C:/Users/ПК/Desktop/qwerty")
from src.lab08.models import Student
from src.lab09.group import Group

# Создаём экземпляр группы
group = Group("src/lab09/data/students.csv")

print("Список студентов:")
students = group.get_list()
for s in students:
    print(f"  {s.fio} | Группа: {s.group} | GPA: {s.gpa}")
print("-" * 60)

print("Поиск студентов с 'анна':")
found = group.find("анна")
for s in found:
    print(f"  {s.fio} — {s.gpa}")
print("-" * 60)

new_student = Student(
    fio="Сергани Карим Мухаммад", birthdate="2000-12-06", group="БИВТ-25-4", gpa=4.7
)
group.add(new_student)
print(f"Добавлен: {new_student.fio}")
print("-" * 60)

print("Обновляем GPA Сергани Карима Мухаммада до 5.0")
group.update("Сергани Карим Мухаммад", gpa=5.0)
print("-" * 60)

print("Проверим, изменился ли GPA у Карима:")
sergani = group.find("Карим")[0]
print(f"  {sergani.fio} — {sergani.gpa}")
print("-" * 60)

print("Удаляем Межеровскую Анну Сергеевну")
try:
    group.remove("Межеровская Анна Сергеевна")
    print("Удалена")
except ValueError as e:
    print(f"Ошибка: {e}")
print("-" * 60)

print("Статистика по группе(БИВТ-25-4):")
stats = group.stats()

print(f"Всего студентов: {stats['count']}")
print(
    f"Мин. GPA: {stats['min_gpa']}, Макс. GPA: {stats['max_gpa']}, Средний: {stats['avg_gpa']}"
)
print("Распределение по группам:")
for gr, count in stats["groups"].items():
    print(f"  {gr}: {count}")

print("Топ-5 студентов:")
for i, s in enumerate(stats["top_5_students"], 1):
    print(f"  {i}. {s['fio']} — {s['gpa']}")
print("-" * 60)

print("Актуальный список после всех изменений:")
for s in group.get_list():
    print(f"  {s.fio} | {s.group} | {s.gpa}")
