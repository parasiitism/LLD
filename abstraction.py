'''
Abstraction is about creating a simplified view of a system
that highlights only essentail features while suppressing the 
irrelevant details
'''


'''
1: Reduce complexity: users and developer don't need to understand the 
internal machinery- just the interface.

2: Improved Usability: A clean, minimal surface area makes your classes easier 
to learn and use correctly

3: Decoupled the design decision

4: Enable the reusability and substitutability
'''

'''
Although closely related,abstraction and encapsulation serve distinct purposes and work
at different levels

1: Encapsulation hides the internal state of the data of an object while abstraction
hides the internal implementation logic of the class object

2: Encapsulation focuses on how data is stored and protected while Abstraction focuses
on what object does not does
'''

from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start(self):
        pass

    def display_brand(self):
        print("Brand:", self.brand)

# Subclass implementing the abstract method
class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

    def start(self):
        print("Car is starting...")