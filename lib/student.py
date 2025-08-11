#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
    
    def learn(self,info):
        self.knowledge.append(info)

s = Student("Ada", "Lovelace")
s.learn("Python basics")
s.learn("Data structures")
print(s.knowledge)  
# ['Python basics', 'Data structures']
