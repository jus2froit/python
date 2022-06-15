from voiture import Voiture
from camion import Camion

v1 = Voiture("BMW", "Serie 5", "diesel", 0,  "berline")
print (v1.get_marque(), v1.get_modele(), v1.get_carburant(), v1.get_type_carosserie(), v1.get_vitesse())

print (v1.get_marque())
print (v1.get_modele())
print (v1.get_carburant())
print (v1.get_type_carosserie())
print (v1.get_vitesse())

v1.set_vitesse(10)

print(v1.get_vitesse())

v2 = Voiture("Ford", "Mustang 68", "essence", 0, " muscle car")

print(v2)

v2.vitesse = 100

print(v2.get_vitesse())

# v2.set_vitesse("vite")

#camion

c1 = Camion("Scania", "?", "diesel", 0, 19.0)
print(c1)
c2 = Camion("Mercedes", "?", "diesel" , 0, 19.0)
print(c2)

my_list=[]

my_list.append(v1)
my_list.append(v2)
my_list.append(c1)
my_list.append(c2)

for item in my_list:
    print(item.get_marque())
    print(item.get_vitesse())
    print(item.get_modele())
    print(item.get_carburant())

    if type(item) is Voiture:
        print(item.get_type_carosserie())
    elif type(item) is Camion:
        print(item.get_ptac())


for item in range (len(my_list)):
    print(my_list[item].get_marque())
    print(my_list[item].get_vitesse())
    print(my_list[item].get_modele())
    print(my_list[item].get_carburant())

    if type (my_list[item]) is Voiture:
        print(my_list[item].get_type_carosserie())
    elif type(my_list[item]) is Camion:
        print(my_list[item].get_ptac())