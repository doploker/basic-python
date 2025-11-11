class Cat:
    name = None
    age = None
    eat = None
    color = None
    def set_data(self,username,age,eat,color):
        self.name = username
        self.age = age
        self.color = color
        self.eat = eat
    

    def print_data (self):
        print(cat1.age,cat1.color,cat1.eat,cat1.name)

    def 


cat1 = Cat()
cat1.name = 'Цезарь'
cat1.age = 2
cat1.eat = True
cat1.color = 'light gray'

cat1.print_data()
cat1.set_data('бублик',5,False,'light')
cat1.print_data()