# file = open('luboe.txt','a')
# file.write('hello, wor\njuahfeoligufujgposhdwuthfjsdiowoqheqeqweeewq\n')
# file.close()



try:
    file = open('luboe.txt','r')
    print(file.read())
    file.close()
except FileNotFoundError:
    print('АДАЙ ФАЙЛ luboe.txt')
    file = open('luboe.txt','w')
    file.write('hello, wor\njuahfeoligufujgposhdwuthfjsdiowoqheqeqweeewq\n')
    file.close()


with open('luboe.txt', 'r') as file:
    print(file.read())
