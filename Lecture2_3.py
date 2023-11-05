import sys
#import os
#from os import path
#from pathlib import Path 
#МОДУЛЬ SYS

print(sys.version) #Версия в текстовом формате 3.11.4
print(sys.version_info) #Версия в подробном формате
                        #3 = major, 11 = minor, 4 = micro
                        #Мажорная, минорная и микро версии системы

print(sys.argv) #Содрежит Имя файла (полное?)

#Вызываем командную строку или GitBash в папке с файлом проги
#Пишем там py Lecture2_3.py и таким образом вызываем эту прогу
#Пишем py Lecture2_3.py source_dir end_dir и таким образом даём на вход эти папки 
if len(sys.argv) < 3:
    print("Отсутствует папка источника или папка назначения")
    exit(1)#В консоли это не покажется, но в целом мы можем это использовать
else:
    source_dir = sys.argv[1]
    end_dir = sys.argv[2]
    print("source_dir: ", source_dir)
    print("end_dir: ", end_dir)

#print(len(sys.argv))


'''
cur_dir = os.getcwd()
source_dir = Path(cur_dir) / "source_dir"
end_dir = Path(cur_dir) / "end_dir"
if not (Path("source_dir").exists() & Path("end_dir").exists()):
    print("Отсутствует папка-источник или папка назначения")
    exit(2) #Мы заканчиваем программу с кодом 1. Если код отличается от 0, то он плохой


end_dir = Path(cur_dir) / "end_dir"
print("source_dir :", source_dir)
print("end_dir :", end_dir)
sys.argv.append(source_dir)
sys.argv.append(end_dir)

for el in sys.argv:
    print(el)
    '''
