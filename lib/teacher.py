#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [
            "Python basics",
            "Object-oriented programming",
            "Git version control"
        ]

    def teach(self): 
        if not self.knowledge:  
            return None
        random_index = random.randint(0, len(self.knowledge) - 1)
        return self.knowledge[random_index]  
    
teacher = Teacher("My", "Teacher")
teacher.knowledge.extend(["Python", "OOP", "Inheritance"])
print(teacher.teach())  
