#СПИСКИ:
lst = [1, 2, 3]
lst.append(4) #Методы
lst.remove(3)

print(lst)
print(lst[0], lst[-1])

if 2 in lst: #in -- Ключевое слово
    print(2, " Есть в списке")
else:
    print("2 нет в списке")

'''lst_console = input("Введите список чисел через пробел: ")#Из строки в список
print(lst_console)
numbers = lst_console.split(" ")#СОздали список из строк разделённых пробелами
print(numbers)'''


#КОРТЕЖИ (Таплы):
#Неизменяемые списки
tup = (3, 5, 2)
print(tup)
print(tup[0])
print(tup[-1])
#tup.append(2) -- С кортежами нельзя
#tup.remove(3)

first, second, third = tup #РАспаковали в несколько переменных
print("1", first)
print("2", second)
print("3", third)

print(3 in tup) #Проверка


#СЛОВАРИ:
eng_rus_dict = {
    "cat": "Кошка",
    "car": "Машина"
    }
print(eng_rus_dict)
print(eng_rus_dict["cat"])
eng_rus_dict["cat"] = "Кот"
print(eng_rus_dict["cat"]) #Достали значение по ключу
#5:40
print("car" in eng_rus_dict)
print(eng_rus_dict.values()) #Список значений
print("Кот" in eng_rus_dict.values()) #Достали значение по значению (Проверили наличие)
print(eng_rus_dict.keys()) #Список ключей

print(eng_rus_dict.items()) #Список из кортежей/таплов (ключ, значение)

#print(eng_rus_dict(["Brother"])) --- Прога упала
print(eng_rus_dict.get("Brother")) #Прока жива вывела None
print(eng_rus_dict.get("Brother", "(Нет перевода)"))


#МНОЖЕСТВА :
set_example = {1, 2, 3}
set_from_lst = set(lst)
print(set_from_lst)
print(set_example)

set_example.add(5)
set_example.remove(2)
print(set_example)
print(set_example - {3, 5})
print(set_example.union({6, 7}))
print(set_example)
print(set_example == {3, 1, 5})

#Для списков мно;еств словарей есть:
print(len("Брат"))
print(len(lst))
print(len(eng_rus_dict))
print(len(set_example))
