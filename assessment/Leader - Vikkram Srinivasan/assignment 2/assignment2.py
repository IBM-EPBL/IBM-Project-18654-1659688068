import random
import time
a=random.random()
while True:
    temperature=random.randint(0, 100 )
    if(temperature > 50):
        print("The Temperature is greater than 50")
    else:
        print("The Temperature is less than 50")
    humidity =random.randint(10, 100)
    if(humidity > 50):
        print("The Humidity is greater than 50")
    else:
        print("The Humidity is lesser than 50")
    time.sleep(1.5)