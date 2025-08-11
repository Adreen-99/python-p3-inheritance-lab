#!/usr/bin/env python

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

user1 = User("Alex", "Kamuhu")
print(user1.first_name)
print(user1.last_name)        