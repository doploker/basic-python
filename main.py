print('hello world!')
#string- строчные
#int - численные
#bul - true/false
#float - дробные
#None - ничего



def func():
    input('ввод')
    a = input()
    print(a)

    b = input ('ввод')
    try: 
        c = int(b)
        f = float(b)
        print (c,f)
    except ValueError:
        print('непавильное преобразование типа')
        


#func()
# == - это знак равенства
# > - больше
# < - меньше
# => - больше или равно
# =< - меньше или равно
# != - не равно
def statement():
    name = input('введите своё Имя')
    if  name == 'Дима':
        print('да')
    else: 
        print('нет')

    age =  int(input('введите свой возраст'))
    if age > 30 or name == 'Дима':
        print('.!.')
    elif age < 30 and name == 'Дима':
        print('не скуф')
    elif age == 30:
        print ("нажми \"В БОЙ, скуфяра\"")


# statement()

#Словарь
#Списки
#Множества
#Кортежи

spisok = [1,12,123,123,1234,True,'имя']

print (spisok[6])
spisok.remove('имя')
print (spisok)
spisok.append('новоеимя')
print (spisok)
spisok.pop(4)
print (spisok)
print(f"count {spisok.count(123)}, index {spisok.index(12)}")

slovar = {
    'ключ1': "значение1",
    'person': {
        'id': 1,
        'name': 'имялюбое',
        'age': 25,
        3: 'три'
    }
}

print(slovar)
print (slovar['ключ1'])
print (slovar['person'])
print (slovar['person']['age'])
print (slovar['person'][3])

kortej = (1,2,2,2,3,3,3,3,3,3,4,4,5)
print(kortej)
print(kortej[0])

#цикл for
for item in spisok:
    print(item)

for key, value in slovar['person'].items():
    print(key, value)

    
