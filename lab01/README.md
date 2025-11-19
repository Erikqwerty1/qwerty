## Лабораторная работа 1

Задание 1
```python
name = input("Имя: ")
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```
![01_greeting.py](./src/01_greeting.py)

Задание 2
```python
a = float(input(("Введите первое число=")))
b = float(input(("Введите первое число=")))
sum=a+b
avg = sum/2
print(f"sum={sum:.2f}",";",f"avg={avg:.2f}")
```
![lab01](./lab01/images/02_sum_avg.png)

Задание 3
```python
price = float(input("Введите цену="))
discount= float(input("Скидка="))
vat = float(input("НДС="))
base = price*(1-discount/100)
vat_amount = base * vat / 100
total = base + vat_amount
print(f"База после скидки:{base:.2f} ₽")
print(f"НДС:{vat_amount:.2f} ₽")
print(f"Итого к оплате:{total:.2f} ₽")
```
![lab01](./lab01/images/03_discount_vat.png)

Задание 4
```python
m = int(input("Введите количество минут="))
h = m//60
mm = m % 60
print(f"{h}:{mm:02d}")
```
![lab01](./lab01/images/04_minutes_to_hhmm.png)

Задание 5
```python
fio = input("Введите ФИО ").split()
print("Инициалы=",fio[0][0],fio[1][0],fio[2][0],sep='')
print(len(fio[0]+fio[1]+fio[2])+2)
```
![lab01](./lab01/images/05_initials_and_len.png)
