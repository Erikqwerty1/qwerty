from pathlib import Path
import csv

def chtenie(path, encoding="utf-8"):
    file_path = Path(path)
    with open(file_path, "r", encoding=encoding) as file:
        stroka = file.read()
        return stroka

def zapis(rows, path, header=None):
    """
    Создает CSV файл с данными.
    rows - список строк (каждая строка - это кортеж или список)
    path - путь к CSV файлу
    header - заголовок таблицы (кортеж)
    """
    file_path = Path(path)
    # Создаю папки если их нет
    create_folders(file_path)
    # Проверяю, что все строки одинаковой длины
    if rows:
        first_row_length = len(rows[0])
        for row in rows:
            if len(row) != first_row_length:
                raise ValueError(f"Все строки должны быть одинаковой длины!")
    
    # Открываю файл для записи
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        # Пишу заголовок, если он есть
        if header is not None:
            writer.writerow(header)
        
        # Пишу все строки
        for row in rows:
            writer.writerow(row)


def create_folders(path):
    """
    Создаю папки для файла если их нет.
    """
    file_path = Path(path)
    folder_path = file_path.parent
    folder_path.mkdir(parents=True, exist_ok=True)

# Пробую прочитать и создать файл
try:
    text = chtenie("data/input.txt")
    print(f"Содержимое: {text}")
    zapis([("test", 3)], "data/check.csv", header=("word", "count"))
except FileNotFoundError:
    print("Ошибка: файл не найден")
except UnicodeDecodeError:
    print("Ошибка: неправильная кодировка файла")
