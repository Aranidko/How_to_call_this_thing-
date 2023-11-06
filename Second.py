import os
from os import path
from pathlib import Path


print("Выберете действие с папками: ")
print("pwd -- просмотр текущей папки")
print("cd -- Переход в другую папку")
print("touch -- создание пустого файла ")
print("cat -- вывод содержимого файла")
print("Is -- вывод списка файлов в папке")
print("rm -- удаление файла")


def pwd():
    cur_dir = os.getcwd()
    return cur_dir


#Идея для cd() -- если имя файла -- пустая строка,
        #то подъём по дереву на одну папку
def cd(dirfile):
    cur_dir = pwd()
    if dirfile != "":
        new_dir = os.path.join(cur_dir, dirfile)
        if path.exists(new_dir):
            os.chdir(new_dir)
            return "Вы перешли по адресу: ", pwd()
        else:
            return "Такой папки не существует."
    else:
        new_dir = os.path.join("..")
        os.chdir(new_dir)
        return "Вы перешли по адресу: " + pwd()


def touch(filename):
    cur_dir = pwd()
    filename_dir = Path(cur_dir) / filename
    try:
        with filename_dir.open('w') as file:
            return "Ваш файл расположен по адресу: " + file.name
    except FileExistsError:
        return "Такой файл уже существует."


def cat(filename):
    cur_dir = pwd()
    filename_dir = Path(cur_dir) / filename #строка с адресом
    if filename_dir.exists():
        with filename_dir.open('r') as file:
            return file.read()
    else:
        return "Такого файла не сушествует."


def Is():
    return os.listdir()
    
def rm(filename):
    cur_dir = pwd()
    file_path = Path(cur_dir) / filename
    try:
        os.remove(file_path)
        return "Файл " + filename + " удалён."
    except FileExistsError:
        return "Такого файла не существует в данной папке."
        

while True:
    command = input()
    if command == "pwd":
        print(pwd())
    elif command == "cd":
        print("Введите название папки: ")
        dirname = input()
        print(cd(dirname))
    elif command == "touch":
        print("Введите название файла с расширением: ")
        filename = input()
        print(touch(filename))
    elif command == "cat":
        print("Введите название файла с расширением: ")
        filename = input()
        print(cat(filename))
    elif command == "Is":
        print("Содержимое папки: ")
        print(Is())
    elif command == "rm":
        print("Введите название файла с расширением: ")
        filename = input()
        print(rm(filename))
    else:
        print("Такой команды не существует")


