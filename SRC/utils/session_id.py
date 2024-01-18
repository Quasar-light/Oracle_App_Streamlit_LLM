import random #generates random variables
from datetime import datetime #from dt module call dt class out of the 6 others avaiable in dt 
from string import ascii_lowercase #make string characters lowercase


def date_id(now=None):
#Create and name function, define parameter, nullify now
    now = now or datetime.utcnow() #redefine now to include dt.utcnow() function
    return now.strftime("%Y%m%d%H") + "".join(random.choices(ascii_lowercase, k=7))

print(date_id(now=None))
