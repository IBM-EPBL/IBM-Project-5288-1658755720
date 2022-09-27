import random
from time import sleep
def generate_values():
    temperature = random.randint(10, 50)
    humidity = random.randint(10, temperature)
    return humidity, temperature

humidity = temperature = 0
i=0
while i<=10:
    humidity, temperature = generate_values()
    print('Humidity:', humidity, 'Temperature:', temperature)
    if  temperature>=40:
        print('Alarm Activated : High Temperature Detected\n-------------------------------------------')
    i=i+1
    sleep(0.50)