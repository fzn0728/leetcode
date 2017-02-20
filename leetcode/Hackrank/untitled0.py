# -*- coding: utf-8 -*-
"""
Created on Wed Jun 01 19:01:34 2016

@author: Chandler
"""
### General Class
class Student(object):
    
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    
    def print_score(self):
        print('%s: %s'%(self.__name,self.__score))
    
    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score
        
    def set_score(self,score):
        if 0<=score<=100:
            self.__score = score
        else:
            raise ValueError('bad score')


bart = Student('Bart Simpson2',59)

# Since we add the __ before each variable, then we cannot visit those variable from the outside of the Class.
# Then, we can write a function which help us to visit those variables (get_score)(get_name) etc.

# Need to use Student. or bart. to call the function encapsulated in the class 
Student.get_name(bart)
bart.get_name()

# Also, if we want to change the attribute of the instance, we can def a set function to do this.

### Subclass -

class co_student(Student):
    pass

mike = co_student('Mike',98)
