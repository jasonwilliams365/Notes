class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def greet(self):
        return f"Hello, my name is {self.name}. I am {self.age} years old." 
    

jason = Person("Jason", 31)
print(jason.greet())


class Student(Person):
    def __init__(self, name, age, student_id):
       super().__init__(name, age)
       self.student_id = student_id
       
jason = Student("Jason", 22, 12345)
print(jason.greet())
print(jason.student_id)
    
