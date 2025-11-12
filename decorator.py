def auth(func):
    def wrapper(name):
        if name in "name.":
            return func(name)
        else: 
            return 'неверный секретный ключ'
        
    return wrapper

    

@auth
def my_string(name):
    return f'secret key: {name}'

print(my_string('name.s'))  
