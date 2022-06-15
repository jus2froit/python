
import sys
from timeit import default_timer as timer

# start benchmark
start = timer()

# votre code ici


tableau = [1, 2 , 8 ,9 , 15]
total = 0

numpy.sum(tableau)
# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)
print("")


0.09887541800071631
0.08483525899919186