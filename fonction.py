scores = [ 433 , 562, 574, 800, 953]


def int_average(numbers:list)-> int:
    '''
    cette fonction renvoie un arrondi de la moyenne des nombres passé en parametre

    numbers: list cette liste contient les nombres don il faut calculer la moyenne
    return: int renvoie la moyenne arrondi au format int des nombre de la liste 
    '''
    #nb d'element
    n = len(numbers)
    total = 0
    # total = sum(scores)   existe mais pas pedagogique
    for number in numbers:
        total += number
    average = int(total / n)
    return(average)

a = int_average(scores)
print(a)

