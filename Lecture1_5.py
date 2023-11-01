#   циклы
lst2= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)#Элементы всегда храняться в памяти

for item in lst2:
    print(item)

print("-" * 10)

print(range(10))#Элементы генерируются в ходе выполнения цикла
print(list(range(10)))
for i in range(10):
    if i == 1:
        print("-")
        continue
    if i == 5:
        print("Всё")
        break
    print(i)

cats = ["Барсик", "Мурзик", "Василий"]
print(list(enumerate(cats)))
for idx, cat in enumerate(cats):
    print(f"{idx}. {cat}")

#print(reversed(cats))  Так просто не работает
print(list(reversed(cats)))
print(list(sorted(cats)))


eng_rus_dict = {
    "cat" : "кот",
    "car" : "машина"
    }
for key, value in eng_rus_dict.items():
    print(f"ключ {key}, значение {value}")

i = 0
while i != 5:
    i += 1
print(5)

print("a", ord('a'))
sym_num = ord('а')
print("я", ord('я'))
while sym_num <= ord('я'):
    print(sym_num, chr(sym_num))
    sym_num += 1
