import random

while random.randint(0, 9) < 5:
    print("foo")

while True:
    if random.randint(0, 9) < 5:
        print("foo")
    else: 
        break

##avec une condition d'arret
while True:
    if random.randint(0, 9) >= 5:
        break
    print("foo")


#methode avec un tirage avant la boucle
n = random.randint(0, 9)
#avec une condition de continuation
while n < 5:
    print("foo")