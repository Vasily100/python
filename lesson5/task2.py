"""
2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
    выполнить подсчёт строк и слов в каждой строке.
"""
with open("File") as file:
    file_lines = file.readlines()
    print("Количество строк: ", len(file_lines))
    for line_number, line in enumerate(file_lines, 1):
        print(f"Количество слов в строке {line_number}:", len(line.split()))
