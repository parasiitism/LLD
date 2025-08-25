#Enum can have additional data aeven behavior. this makes them morepowerful

from enum import Enum 

class Coin(Enum):
    PENNY=1
    NIKCLE=5
    DIME=10
    QUARTER=25

    def __init__(self,value):
        self.coin_value=value
    
    def get_value(self):
        return self.coin_value
total = Coin.DIME.get_value() + Coin.QUARTER.get_value()

print(total)