import random
from re import A

# if True:
#     print("ce message sera toujours affiché")

# if False:
#     print("ce message ne sera pas affiché")

# if True:
#     print("ce message sera toujours affiché (if True)")
# else:
#     print("ce message ne sera jamais affiché (if True)")

# if False:
#     print("ce message ne sera pas affiché (if False)")
# else: print("ce message ne sera jamais affiché (if False)")

# fruits = ["apples", "bananas", "cherries"]

# if "apples" in fruits:
#     print("il y a des pommes")
# else:
#     print("il n'y a pas de pommes")

# if "oranges" in fruits:
#     print("il y a des oranges")
# else:
#     print("il n'y a pas d'oranges")

# is_authentificated = True

# if is_authentificated:
#     print ("L'utilisateur peut accéder au backoffice")

# user_password = "123"
# user_password_in_db = "abc"

# if user_password == user_password_in_db:
#     print ("L'utilisateur peut accéder au backoffice")
# else:
#     print("le mail ou le mdp est incorrect")

# users = ["toto", "titi", "tata", "tutu"]
# user_password_in_form = "123"
# user_name_in_form = "tutu"
# tutu_password_in_db = "abc"

# if user_name_in_form in users and user_password_in_form == tutu_password_in_db:
#     print ("L'utilisateur peut accéder au backoffice")
# else:
#     print("le mail ou le mdp est incorrect")

# is_authentificated = False
# users = ["toto", "titi", "tata", "tutu"]
# user_password_in_form = "123"
# user_name_in_form = "tutu"
# tutu_password_in_db = "abc"

# if is_authentificated or (user_name_in_form in users and user_password_in_form == tutu_password_in_db):
#     print ("L'utilisateur peut accéder au backoffice")
# else:
#     print("le mail ou le mdp est incorrect")

# electricity_is_off = bool(random.randint(0, 1))
# water_is_off = bool(random.randint(0, 1))
# gas_is_off = bool(random.randint(0, 1))

# print("electricity_is_off: ",electricity_is_off)
# print("water_is_off: ",water_is_off)
# print("gas_is_off: ",gas_is_off)

# if electricity_is_off and water_is_off and gas_is_off:
#     print ("vous pouvez partir en we")
# else:
#     print ("il vous reste des sources à couper")
#     if not electricity_is_off:
#         print ("vous n'avesz pas couper l'électricité")
#     if not water_is_off:
#         print ("vous n'avez pas couper l'eau")
#     if not gas_is_off:
#         print ("vous n'avez pas couper le gaz")

# electricity = bool(random.randint(0, 1))
# water = bool(random.randint(0, 1))
# gas = bool(random.randint(0, 1))

# print("electricity: ",electricity)
# print("water: ",water)
# print("gas: ",gas)

# if not electricity and not water and not gas:
#     print ("vous pouvez partir en we")
# else:
#     print ("il vous reste des sources à couper")
#     if electricity:
#         print ("vous n'avez pas couper l'électricité")
#     if water:
#         print ("vous n'avez pas couper l'eau")
#     if gas:
#         print ("vous n'avez pas couper le gaz")


# has_cash = bool(random.randint(0,1))
# has_card = bool(random.randint(0,1))
# has_check = bool(random.randint(0,1))

# print("liquide :",has_cash)
# print("carte :",has_card)
# print("cheque :",has_check)

# if has_cash or has_card or has_check:
#     print("vous puvez partir faire les courses")
#     if has_cash:
#         print("vous pouvez payer en liquide")
#     if has_card:
#         print("vous pouvez payer par carte")
#     if has_check:
#         print("vous pouvez payer par cheque")
# else:
#     print("vous n'avez aucun moyen de paiement")


age = random.randint(0,100)

# 0-5 bébé
# 6-11 enfant
# 12-25 ado jeune adulte
# 26-59 adulte
# 60+ senior

# print("age :", age)

# if age <= 5:
#     print("bébé")
# elif  6 <= age <= 11:
#     print("enfant")
# elif 12 <= age <= 25:
#     print("ado jeune adulte")
# elif 26 <= age <= 59:
#     print("adulte")
# else:
#     print("senior")






#interchanger les valeurs des variables

# a = 42
# b = 123
# c = b - a
# a = a + c
# b = b - c

#methode classique
# a = 42
# b = 123
# c = a
# a = b
# b = c

# destructured assignement  (python, javascript mais pas php)
# a = 42
# b = 123
# a, b = b, a

#methode arithmetique
# a = 42
# b = 123
# a = a + b
# b = a - b
# a = a - b

# if a == 123 and b == 42:
#     print("vous avez réussi a interchanger les valeurs de variables")


# # arrondi
# import decimal
# from decimal import Decimal
# decimal.getcontext().rounding = decimal.ROUND_HALF_UP
# print(Decimal(0.5).quantize(Decimal("0.00")))
# print(Decimal("1.5").quantize(Decimal("1")))

#encadrement

a = 42
b = 123

c = random.randint(1,150)

result = a < 50 < b
print(result)

print ("c =",c)
result = a < c < b
print(result)