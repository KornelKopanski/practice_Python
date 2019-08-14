# Program symuluje gre "lotto"


import random


my_numbers = []

while len(my_numbers) != 6:
    number = int(input("Podaj liczbę od 1 do 50: "))
    if number not in my_numbers:
        my_numbers.append(number)
    else:
        print("Podana liczba została już skreślona, wybierz inną liczbę!")


lotto_numbers = []

while len(lotto_numbers) != 6:

    individual_number = random.randint(1,50)
    if individual_number not in lotto_numbers:
        lotto_numbers.append(individual_number)


score = []


for element in my_numbers:

    if element in lotto_numbers:
        score.append(element)


print("Liczby wybrane przez ciebie: {}".format(my_numbers))
print("Liczby wylosowane przez komputer {}".format(lotto_numbers))


if score:
    print("Twoje liczby, które zostały wylosowane {}".format(score))
else:
    print("Niestety nie trafiłeś ani jedniej liczby!")






