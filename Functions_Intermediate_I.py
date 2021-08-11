import random

def randInt(min=0, max=100):
    if max<0 or min<0 or min>max:
        return "Your inputs values are not correct! Please select positive numbers in which max is greater than min. Remember that the defaults values for min and max are 0 and 100 respectivetly!"
    else:
        random_range = max-min
        num = round(random.random()*random_range+min)
        return num


print(randInt()) # should print a random integer between 0 to 100
print(randInt(max=50)) # should print a random integer between 0 to 50
print(randInt(min=50)) # should print a random integer between 50 to 100
print(randInt(min=50, max=500)) # should print a random integer between 50 and 500
print(randInt(min=150, max=100)) # should print a Message Stating that the argument is not valid  
print(randInt(max=-100)) # should print a Message Stating that the argument is not valid
print(randInt(max=-500)) # should print a Message Stating that the argument is not valid
print(randInt(min=150)) # should print a Message Stating that the argument is not valid
 
