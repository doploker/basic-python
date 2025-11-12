# a = 0
# while a < 5:
#     print(a)
#     a += 1

flag = True
a = 0
while flag:
    a += 1
    print('df')

    if a != 7:
        # flag = False
        continue
    else:
        break
        
    

#for <любая перемнная> in range(от, до)
    # операции

for i in range(5,10,2):
    print(i)

# i for i in range(1, 10)
numbers = [number for number in range(1, 10)]
print(numbers)

numbers.clear()
for number in range(1, 15):
    numbers.append(number)

print(numbers)