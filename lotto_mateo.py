# Wersja mateusza

import random

liczby = ["drugą","trzecią","czwartą","piątą","szóstą","siódmą","ósmą","dziewiątą","dziesiątą"]
lotto = []
lotto_wygrane = []
total = 0
i = 0

print("Podaj liczby z zakresu od 1 do 49")

cyfra = input("podaj liczbę pierwszą: ")
lotto.append(cyfra)

while len(lotto) < 10:
    cyfra = input("podaj liczbę {}: ".format(liczby[i]))
    if cyfra in lotto:
        print("Podałeś już taką liczbę, podaj inną!")
    else:
        lotto.append(cyfra)
        i += 1


cyfra = random.randint(1,49)
lotto_wygrane.append(cyfra)


for l in range(1,10):
    cyfra = random.randint(1,49)
    lotto_wygrane.append(cyfra)


print(lotto)
print(lotto_wygrane)

for i in lotto:
    for j in lotto_wygrane:
        if int(i) == int(j):
            print("Trafiłeś liczbę: {}".format(i))
            total = total+1
        else:
            pass



if total == 0 or total >=5:
    print("Trafiłeś: {} liczb".format(total))
elif total == 1:
    print("Trafiłeś: {} liczbę".format(total))
else:
    print("Trafiłeś {} liczby".format(total))
