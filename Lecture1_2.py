#Тут же лекция 1.3
#-----------------


#name = "Вася"
name = input("Введите имя: ")
#age = 10.1
age = float(input("Введите возраст: "))
#is_working_now = True
is_working_now = input("Работает сейчас? (1 или 0): ") == "1" #Любая непустая строка -- True по умолчанию, потому сравниваем
workplace = None #Null из других яп
if is_working_now:
    workplace = input("Где работает?: ")

#if((workplace == "") or (workplace is None)): #'''is_working_now and'''
#    print("Не заполнено место работы")
if is_working_now and not workplace:
    print("Не заполнено место работы")


if age >= 20:
    print("Пользователю юольше 20 лет")
elif age >= 18:
    print("Совершеннолетний")
else:
    print("Несовершеннолетний")

print(name + "-Дурак")

#print(f"Вы ввели: {input()}")
#print(f"Как ваши дела? {input()}") #Сперва принимает значение потом выводит Полную строчку

#print("Имя: " + name)
print(f"Имя: {name}") #f-string-и помогают делать так
print("Возраст: " + str(age))
print(f"Работает ли сейчас: {is_working_now}")
if is_working_now:
    print("Место работы: " + workplace)

str_template = "Информация о пользователе: {} - {}"#Сделали шаблон
print(str_template.format(name, age)) #Ещё вариант вывода строк"

str_smth = "Имя и кличка: {} -- {}"
#print(str_smth.format(input("Введите имя: "), input("Введите кличку: "))) #Сперва спрашивает потом выводит
str_how_r_u = "Вы ответили: {}. Так вот, у меня тоже"
#print(str_how_r_u.format(input("Как у вас дела?")))

print(name.upper()) #Верхний регистр -- все буквы строки с маленькой
print(name.lower()) #Нижний регистр -- с большой
print(name.find("я")) #Нашли букву "а". выдаст индекс символа
print(name.replace("я", "ян"))
print(name) #Остаётся

a = 2
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(5 // a)
#минута6:57

#number = input("Введите число: ")
#number = int(number)
#print(number * 2)

c = 4
c += 1
