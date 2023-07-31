# single inheritence
#################################
class Parent:
    def pdisplay(self):
        print("Parent")
class Child(Parent):
    def cdisplay(self):
        print("Child")

C1=Child()
C1.cdisplay()
C1.pdisplay()

# using class in other python files 
##################################
from class_objects import student 
S1=student()
S1.read()

# multi level inheritence
####################
class Grandparent:
    def gdisplay(self):
        print("Grandparent")
class Parent(Grandparent):
    def pdisplay(self):
        print("Parent")
class Child(Parent):
    def cdisplay(self):
        print("child")

C2=Child()
C2.gdisplay()
C2.pdisplay()
C2.cdisplay()


