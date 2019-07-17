
# ZADANIE3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5
# ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.


from decimal import *


def jump(first_number,last_number):
    x = first_number - 0.5
    while x != last_number:
        x += 0.5
        print(Decimal(x))

jump(2,5.5)