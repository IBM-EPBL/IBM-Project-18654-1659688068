import random
import time

while True:
    temperature=random.randint(0, 100 )
    print("temperature - ",temperature)
    if(temperature > 50):
        
        print("The Temperature is very hot alarm will be on")
        
    else:
        print("The Temperature is less than 50")
    print()
    humidity =random.randint(10, 100)
    
    print("Humidity - ",humidity)
    if(humidity > 50):
        
        print("The Humidity is high the alarm will be on")
        
    else:
        print("The Humidity is lesser than 50")
    print()
    time.sleep(1.5)
