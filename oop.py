# def greet(name):
#     print("Hello", name)

# # print(type(greet))
# x=1
# y= "hello"
# print(str(x)+y)

class Math():
    def Add(self,x):
        return x + " is easy"

    def __init__(self, language):
        self.language = language

        print(f"coding in {language} is fun")


# m= Math("python")
# print(m.Add("coding"))
class Animal():
    def __init__(self, language,name):
        self.language = language
        self.name=name

    def Sound(self):
        print("I make sounds")
    def Introduce(self):
        print(f"Hey, i Am {self.name} and i speak {self.language}")

class Dog(Animal):
    pass
class Cat(Animal):
    def __init__(self, language,name,age): 
        super().__init__(language,name)
        self.age=age

    def Sound(self):
        print(f"I meow and i am {self.age}")

d= Dog("Luo","Heith")
c=Cat("MAndarin","via",3)
d.Introduce()
d.Sound()
c.Sound()