#МОДУЛИ filecmp, zipfile, shutil
import os
import filecmp #Входит в стандартную библиотеку Python
import shutil #Shell Utilities --Доп инструменты для работы с консолью
import tempfile #Позволяет создавать временные файлы и папки
import zipfile # Позволяет создать zip- архивы
from pathlib import Path

files_dir = Path("files")
#Функция сравнения двух файлов: Если одинаковы то True, иначе False
result = filecmp.cmp(
    files_dir/"file.txt",
    files_dir/"file_01.txt")
print(result)

#Сравнивает две папки с файлами по файлу,
#который мы укажем третьим аргументом
result_dir = filecmp.cmpfiles("files1",
                              "files",
                              ["am_I_error.txt"])
                              #["file.txt"]
#Возвращает кортеж из 3 списков:
#([match], [mismatch], [errors])
match, mismatch, errors = result_dir
print(result_dir)
print(match)
print(mismatch)
print(errors)
#Возвращает кортеж из 3 списков:
#([match], [mismatch], [errors])

#shutil.rmtree("files2")# Удаляет папку files1 вместе с файлами
#shutil.copytree("files", "files2")#Копирует дерево папок
#из одного дерева в другое
#os.rmdir("files") #Пожалуется, что папка не пуста
#os.copy() #Копирует только файлы по отдельности
print(shutil.disk_usage('.')) #Показывает насколько занят диск,
#в котором лежит указанная директория

with tempfile.NamedTemporaryFile(suffix = '.zip', delete = False) as temp_file:#Удаляется по умолчанию при выходе из with
    print(temp_file.name) #Создали временный файл и вывели путь до него
    with zipfile.ZipFile(temp_file.name, 'w') as zip_file:
                            #Создаём объект ZipFile
                            #посылаем в него путь до нужного файла
                            #и указываем модификатор доступа
                            #(тот же что и при открытии файлов)
        zip_file.write(files_dir / 'file.txt', 'file.txt')# сперва имя файла на диске, потом в архиве
        zip_file.write(files_dir / 'file_01.txt', 'file_01.txt')
