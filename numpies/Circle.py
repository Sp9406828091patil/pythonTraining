class Circle: 
    a = 'Aboli' 

    @classmethod 
    def greet(cls):
        obj = cls.__new__(cls)
        print('Welcome to the program of Area and Perimeter of the circle')
        return obj
