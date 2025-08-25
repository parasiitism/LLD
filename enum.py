from enum import Enum

#Simple Enum 
class OrderStatus(Enum):
    PLACED="PLACED"
    CONFIRMED="CONFIRMED"
    SHIPPED="SHIPPED"
    DELIVERED="DELIVERED"
    CANCELLED="CANCELLED"

status=OrderStatus.SHIPPED
if status==OrderStatus.SHIPPED:
    print('Your package is on the way!')