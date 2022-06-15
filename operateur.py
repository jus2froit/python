# arrondi
import random

import decimal
from decimal import Decimal
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
print(Decimal(0.5).quantize(Decimal("0.00")))
print(Decimal("1.5").quantize(Decimal("1")))

#encadrement

