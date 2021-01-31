
#inheritance and class of object integers and strings :-
#class

class BYKE(object):
    def __init__(self,name,highspeed,color):
        self.name = name
        self.highspeed = highspeed
        self.color = color

    def speak(self):
        print("hi, i am",self.name,"and my highest speed is",self.highspeed," and my color is",self.color)

    def change_speed(self,highspeed):
        self.highspeed = highspeed

class Scooter(BYKE):
    def __init__(self,name,highspeed,color):
        self.name = name
        self.highspeed = highspeed
        self.color = color

    def speak(self):
        print("hi, i am scooter",self.name,"and my highest speed is",self.highspeed," and my color is",self.color)


class SUPERBIKES(Scooter):
    def __init__(self, name,highspeed,color,speciality,engine):
        self.name = name
        self.highspeed = highspeed
        self.color = color
        self.speciality = speciality
        self.engine = engine

    def speak(self):
        print("hi, i am superbike",self.name,"and my speed is",self.highspeed,"and my color is",self.color,".I go 0 to 100 in",self.speciality,"and my engine is",self.engine)

    def change_speed(self,highspeed):
        self.highspeed = highspeed
#inheriting
class MOTORCYCLES(SUPERBIKES):
    def __init__(self,name,highspeed,color,speciality,engine):
        super().__init__(name,highspeed,color,speciality,engine)
        self.engine = engine


    def speak(self):
        print("hi, i am motorcycle",self.name,"and my speed is",self.highspeed,"and my color is",self.color,".I go 0 to 100 in",self.speciality,"and my engine is",self.engine)




#overloading

class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.coordinate = (self.x,self.y)

    def move(self,x,y):
        self.x += x
        self.y += y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return self.x * p.x +self.y * p.y


    def __truediv__(self, p):
        return Point(self.x //p.x, self.y //p.y)


    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)

 #eq,gt,lt

    def __gt__(self, p):
        return self.length() > p.length()

    def __lt__(self, p):
        return self.length()  < p.length()

    def __le__(self,p):
        return self.length()  >= p.length()

    def __ge__(self,p):
        return len(self) >= len(p)

    def __eq__(self,p):
        return self.x == p.x and self.y == p.y

    #  def __float__(self,p):
    #      return abs(self.x == p.x and self.y == p.y)

    def __str__(self):
        return "(" + str(self.x) + ',' + str(self.y) + ")"



p1 = Point(1,2)
p2 = Point(3,4)
p3 = Point(5,6)

p4 = p1 + p2
p5 = p2 - p1
p7 = p3*p3
p8 = p3/p3
print(p4 == p5)
print(p4 > p5)
print(p4)
#class and static method

class Pets:
    dogs = []
    cats = []
    def __init__(self, name):
     self.name = name
     self.dogs.append(self)
     self.cats.append(self)


    @classmethod
    def num_dogs(cls):
      return len(cls.dogs)



    @staticmethod
    def bark(n):
         for _ in range(n):
            print("bark!")



    @classmethod
    def num_cats(cls):
        return len(cls.cats)



    @staticmethod
    def meow(n):
         for _ in range(n):
             print("meow!")




print(Pets.num_dogs())
print(Pets.num_cats())

#private and public classes

class _Private:
    def __init__(self,name):
        self.name = name

class NotPrivate:
    def __init__(self,name):
        self.name = name
        self.priv = _Private(name)


    def _display(self):
        print("Hello")

    def display(self):
        print('Hi')