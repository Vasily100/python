"""
6. Сформировать (не программно) текстовый файл.
    В нём каждая строка должна описывать учебный предмет и наличие лекционных,
    практических и лабораторных занятий по предмету.
    Сюда должно входить и количество занятий.
    Необязательно, чтобы для каждого предмета были все типы занятий.
    Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
    Вывести его на экран.
"""

result_dict = {}
with open("File6") as file:
    for line in file:
        lesson_type, *lessons = line.split()
        lesson_count = [int(lesson.rstrip('(л)(пр)(лаб)')) for lesson in lessons if lesson != '-']
        result_dict.update({lesson_type.rstrip(":"): sum(lesson_count)})

print(result_dict)
