import os                   #Модуль взаимодействующий с ос
from os import path         #Модуль с классом path который помогает общаться напряму к path (До этого везде писали os.path)
from pathlib import Path    #Модуль с классом Path который помогает создавать объекты для работы с путями

'''                     
print("Файл open_me.txt: ")
file = open("open_me.txt", "w")
print(file.read())
file.close()

#Файлы .txt нужно добвалять в .gitignore
print("Файл variables.txt: ")
with open("variables.txt", "r") as file: #Менеджер, который автоматически закрывает файл
    for line in file:
        print(line.strip()) #strip() убирает лишние пробелы, переносы и пустоты в файле в начале и конце строки
'''

cur_path = os.getcwd() #Взяли путь к текущей папке
files_dir = Path(cur_path) / "files" #По сути тот же path.join() -- Вариант с Path
'''
files_dir = os.path.join(cur_path, "files") -- Только модуль os 
files_dir = path.join(cur_path, "files") -- Модуль os + класс path
#Объединяет пути. грубо говоря мы обозначили место и имя папки, но ещё не создали
                                           #Нужно это тк в винде используется \, а в линуксе /
                                           #НЕЛЬЗЯ ПИСАТЬ ПУТИ ВРУЧНУЮ
'''
print(cur_path)
try: #При повторном создании папки выдаётся ошибка, мы не хотим ошибок
    files_dir.mkdir() #Path
    #os.mkdir(files_dir) #Создали папку 
except FileExistsError:
    pass #пропустить команду в случае ошибки

file_path = files_dir / "file123.txt" #Path
#file_path = path.join(files_dir, 'file.txt') #Создали ф папку files файл file.txt

#rb, wb, ab -- Отркывают файл в бинарном формате (для картинок, программ)
#x -- открывает файл на запись, но выдаст исключние, если файла не существовало ранее

with file_path.open('a+') as file: #Path
#with open(file_path, "a+") as file: #w+ -- Возможность писать и чистать информацию
                                        #w -- Запись с обнуленением предыдущего текста, создаст если файла не существовало
                                        #a -- Открфывает файл на дозапись
                                        #a+ -- Дозапись чтение во время записи
    
    file.write("text")#После выполнения ф-ии write указатель будет в конце, соответственно 
    file.seek(0)#Сместили указатель в начало
    print(file.read())
try:
    os.remove("Kill_me.py") #Убирает файл
except FileNotFoundError:
    pass
print(Path("file.txt").exists()) #Path
print(path.exists("Kill_me.py")) #Сука сработалo
                                    #Реально удалился файл и его директория пропала из папки
print(file_path) 
print(path.basename(file_path)) #Имя файла
print(path.dirname(file_path)) #Путь до папки
print(path.splitext("file.txt")) #Расширение файла, разделеие идёт исключительно по раширению

print("------------------------")
print(path.join('..', 'How_to_call_this_thing-')) #Путь до папки выше нынешней (нынешняя files) -- относительный директорий
print(path.abspath(path.join('..', 'testdir')))#Превращение локального директория в абсолютный,
                                               #то есть не зависящий от папки, в которой лежит проект

os.chdir(path.join('..', 'How_to_call_this_thing-')) #os.chdir() -- помогает перейти по адресу
print(os.getcwd())


#ПЕРЕМЕННЫЕ ОКРУЖЕНИЯ
#-- Это переменные которые меняются извне (Пользователем)
TEST = os.environ.get("TEST",
                     "default value for environ variable")
#os.environ -- Словарь в котором храняться переменные окружения

