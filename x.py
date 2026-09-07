a=[1,2,3,4,5,6,7,8,9]
print (a[0])
print (list.pop(a))
a=list.pop(a)
print (a)



users = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Carol', 'age': 28},
]
# 用 sorted 配合 lambda 按 age 升序排序，赋给 sorted_users
# 再用 for 循环依次打印每个人的 name 和 age
sorted_users = sorted (users, key=lambda u:u['age'])
for u in sorted_users:
    print (u['name'], u['age'])


class Animal:
    def sound(self):
        print ('某种声音')
a=Animal()
a.sound()

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def greet(self):
        print (f'我叫{self.name}，今年{self.age}岁了。')

class Student(Person):
    def __init__(self, name, age, habbit):
        super(). __init__(name, age) # 调父类的 __init__
        self.habbit=habbit
    def activity(self):
        print (f'我喜欢{self.habbit}')
p=Student('林启骏',21,'看漫画。')
p.greet()
p.activity()

class Otaku(Person):
    def __init__ (self, name, age):
        super(). __init__ (name, age)
    def greet(self):
        print (f'老子是{self.name}，当死肥宅已经{self.age}年了！')
p=Otaku('林启骏',21)
p.greet()


class Animal:
    def sound(self):
        print('一些声音')

# 定义 Dog 和 Cat 继承 Animal，各自重写 sound 方法
# 用 for 循环遍历两个实例并依次调用 sound
class Dog(Animal):
    def sound(self):
        print ('汪汪')

class Cat(Animal):
    def sound (self):
        print ('喵喵')
animals=[Dog(), Cat()]
for a in animals:
    a.sound()

