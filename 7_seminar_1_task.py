'''Напишите функцию группового переименования файлов. Она должна:
принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
принимать параметр количество цифр в порядковом номере.
принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
принимать параметр расширение конечного файла.
принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение. 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.'''

import os
from pathlib import Path


def group_rename(count_len: int, extension: str, new_extension: str, interval: list, new_name=''):
    count = 0
    for file in os.listdir():
        if file.endswith(extension):
            count += 1
            Path(file).rename(f"{file.split('.')[0][interval[0]:interval[1]]}{new_name}{count:0>{count_len}}.{new_extension}")