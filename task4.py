""""
 Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
 Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
 Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_name, productivity, rate_per_hour, bonus = argv
print("Name of script: ", script_name)
print('Productivity, hours: ', productivity)
print('Rate per hour: ', rate_per_hour)
print('Bonus: ', bonus)
print('Salary: ', int(productivity) * int(rate_per_hour) + int(bonus))

"""
Представлен список чисел. 
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. 
Для его формирования используйте генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_new_list = [my_list[index] for index in range(1, len(my_list)) if my_list[index] > my_list[index - 1]]
print(f'Исходный список: {my_list}')
print(f'Результат: {my_new_list}')

"""
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. 
Решите задание в одну строку.
Подсказка: используйте функцию range() и генератор.
"""
print(f'Числа кратные 20 или 21: {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

"""
Представлен список чисел. 
Определите элементы списка, не имеющие повторений. 
Сформируйте итоговый массив чисел, соответствующих требованию. 
Элементы выведите в порядке их следования в исходном списке. 
Для выполнения задания обязательно используйте генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_new_list = [el for el in my_list if my_list.count(el) == 1]
print(my_new_list)

"""
Реализовать формирование списка, используя функцию range() и возможности генератора. 
В список должны войти чётные числа от 100 до 1000 (включая границы). 
Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def my_func(el_p, el):
    return el_p * el


print(f'Исходный список: {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат: {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

"""
Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее. 
Подсказка: используйте функцию count() и cycle() модуля itertools. 
Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
Предусмотрите условие его завершения. 
#### Например, в первом задании выводим целые числа, начиная с 3. 
При достижении числа 10 — завершаем цикл. 
Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.
"""
from itertools import count

start_from = 10
iterations_count = 0


def integer_generator(start_from):
    for el in count(start_from):
        if el > start_from + 10:
            break
        yield el


for el in integer_generator(3):
    print(el)

from itertools import cycle

iterable = "12345"
iterations_count = 0

for el in cycle(iterable):
    if el == iterable[0]:
        iterations_count += 1
    if iterations_count < 5:
        print(el)
    else:
        break

"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
При вызове функции должен создаваться объект-генератор. 
Функция вызывается следующим образом: for el in fact(n). 
Она отвечает за получение факториала числа. 
В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. 
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
from itertools import count
from math import factorial


def fact():
    for el in count(1):
        yield factorial(el)


gen = fact()
x = 0
for i in gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break
