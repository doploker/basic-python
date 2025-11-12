class Cat:
    name = None
    age = None
    eat = None
    color = None

    def __init__(self, name, age, eat, color='white'):
        self.name = name
        self.age = age
        self.eat = eat
        self.color = color
    
    def set_data(self,username,age,eat,color):
        self.name = username
        self.age = age
        self.color = color
        self.eat = eat
    

    def print_data (self):
        print(self.name, self.age, self.eat, self.color)

     


# cat1 = Cat()
# cat1.name = 'Цезарь'
# cat1.age = 2
# cat1.eat = True
# cat1.color = 'light gray'

cat1 = Cat('Цезарь', 2, True)

cat1.print_data()
cat1.set_data('бублик',5,False,'light')
cat1.print_data()

class Tiger(Cat):
    # инкапсуляци (защита данных)
    __is_active = True
    __solo = False

    def jump():
        print('jump')
    def run():
        print('run')

    # полиморфизм
    def print_data(self):
        super().print_data()
        print(f"active: {self.__is_active} solo: {self.__solo}")
        

tiger1 = Tiger('тигруля',5,True,'orange')
tiger1.print_data()
