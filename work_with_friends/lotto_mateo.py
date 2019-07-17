# Wersja mateusza

import random

liczby = ["pierwszą","drugą","trzecią","czwartą","piątą","szóstą","siódmą","ósmą","dziewiątą","dziesiątą"]
lotto = []
lotto_wygrane = []
total = 0
i = 0

while len(lotto) < 10:
    cyfra = input("podaj liczbę {}(zakres od 1 do 49): ".format(liczby[i]))
    if cyfra in lotto:
        print("Podałeś już taką liczbę, podaj inną!")
    else:
        lotto.append(cyfra)
        i += 1


for l in range(10):
    cyfra = random.randint(1,49)
    if cyfra not in lotto_wygrane:
        lotto_wygrane.append(cyfra)


print(lotto)
print(lotto_wygrane)

for i in lotto:
    for j in lotto_wygrane:
        if int(i) == int(j):
            print("Trafiłeś liczbę: {}".format(i))
            total = total+1



if total == 0 or total >=5:
    print("Trafiłeś: {} liczb".format(total))
elif total == 1:
    print("Trafiłeś: {} liczbę".format(total))
else:
    print("Trafiłeś {} liczby".format(total))
