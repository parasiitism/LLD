'''
In programming,Encapsulation is typically achived using
Access Modifiers(private,protected,public)
Getter and Setters
'''

'''
It helps you build systems that are robust, secure, and easy to maintain. Here's why it's essential:

Data Hiding: By restricting direct access to internal fields, encapsulation shields sensitive data from unintended interference or misuse.
Controlled Access and Security: : It ensures that data can only be accessed or modified through well-defined methods, allowing you to enforce rules, validation, or logging when needed.
Improved Maintainability: Because internal implementation details are hidden, you can refactor or optimize them without affecting the external code that depends on the class.
'''

class BankAccount:
    def __init__(self):
        self.__balance=0.0
    
    def deposit(self,amount):
        if amount<=0:
            raise ValueError("Deposite amount must be +ve")
        self.__balance+=amount
    def withdraw(self,amount):
        if amount<0:
            raise ValueError("Withdrawal amount must be +ve")
        elif amount>self.__balance:
            raise ValueError("Insufficient Fund")
        self.__balance-=amount
    
    def get_balance(self):
        return self.__balance