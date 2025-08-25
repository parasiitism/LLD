from abc import ABC,abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def initiate_payment(self,amount):
        pass 

'''
This interface does not care how payment is being proessed--It only
mandates that all implementing class must define a method called
intitiatePayment()
'''
class StripePayment(PaymentGateway):
    def initiate_payment(self, amount):
        print(f"Processing payment via stripe :${amount}")

class RozarPay(PaymentGateway):
    def initiate_payment(self, amount):
        print(f'Proceesing payment via RozarPay :${amount}')



class CheckoutService:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway
    
    def set_payment_gateway(self, payment_gateway):
        self.payment_gateway = payment_gateway
    
    def checkout(self, amount):
        self.payment_gateway.initiate_payment(amount)



if __name__=="__main__":
    stripe_gateway=StripePayment()
    checkout_service=CheckoutService(stripe_gateway)
    checkout_service.checkout(120.50)

    #  Switch to Rozarpay
    rozarpay_gateway=RozarPay()
    checkout_service.set_payment_gateway(rozarpay_gateway)
    checkout_service.checkout(49.90)
    







