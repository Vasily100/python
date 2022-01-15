"""
Поработайте с переменными, создайте несколько, выведите на экран.
Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.
"""

name = input("Как вас зовут? ")
work = input("Кем вы работаете? ")
years = int(input("Сколько лет вы работаете? "))
print(f"{name} работает {work} {years} лет")

"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

time = int(input("Введите время в секундах: "))
hours = time // 3600
minutes = time % 3600 // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"{hours:02} : {minutes:02} : {seconds:02}")

"""
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""

n = int(input("Введите число: "))
result = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
print(result)

"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

n = (int(input("Введите целое положительное число: ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
        continue
    if n == 9:
        break
print("Наибольшая цифра в числе: ", max)

"""
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма.
Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
Выведите соответствующее сообщение.

Если фирма отработала с прибылью, вычислите рентабельность выручки.
Это отношение прибыли к выручке.
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
"""

revenue = int(input("Какая выручка фирмы? "))
costs = int(input("Какие издержки фирмы? "))
profit = revenue - costs
if revenue > costs:
    print(f"Рентабельность выручки составила: {profit/revenue * 100:.2f}%")
    workers = int(input("Введите количество сотрудников: "))
    print(f"Прибыль в расчете на одного сторудника: {revenue/workers}")
elif revenue == costs:
    print("У фирмы нулевая прибыль")
else:
    print("Фирма работает в убыток")

"""
Спортсмен занимается ежедневными пробежками. 
В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее b километров. 
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.
Результат: 
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на шестой день спортсмен достиг результата — не менее 3 км.
"""

a = int(input("Сколько километров спортсмен пробежал в первый день? "))
b = int(input("Желаемый результат: "))
result_days = 1
while a < b:
    a *= 1.1
    result_days += 1
print(f"Спортсмен достигнет результата в {b} км на {result_days} день")