## Лабораторная работа 1
            
            #Задание 1
name = input("Имя: ")
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age + 1}.")

![lab01](./src/images1/lab01/01_greeting.png)

            #Задание 2
a = float(input(("Введите первое число=")))
b = float(input(("Введите первое число=")))
sum=a+b
avg = sum/2
print(f"sum={sum:.2f}",";",f"avg={avg:.2f}")
![lab01](./src/images/02.png)

![lab01](./src/images1/lab01/02_sum_avg.png)
            
            #Задание 3
price = float(input("Введите цену="))
discount= float(input("Скидка="))
vat = float(input("НДС="))
base = price*(1-discount/100)
vat_amount = base * vat / 100
total = base + vat_amount
print(f"База после скидки:{base:.2f} ₽")
print(f"НДС:{vat_amount:.2f} ₽")
print(f"Итого к оплате:{total:.2f} ₽")
![lab01](./src/images/03.png)

![lab01](./src/images1/lab01/03_discount_vat.png)

            #Задание 4
m = int(input("Введите количество минут="))
h = m//60
mm = m % 60
print(f"{h}:{mm:02d}")
![lab01](./src/images/04.png)

![lab01](./src/images1/lab01/04_minutes_to_hhmm.png)

            #Задание 5
fio = input("Введите ФИО ").split()
print("Инициалы=",fio[0][0],fio[1][0],fio[2][0],sep='')
print(len(fio[0]+fio[1]+fio[2])+2)
![lab01](./src/images/05.png)

![lab01](./src/images1/lab01/05_initials_and_len.png)