


import random

# Tworzę listę która będzie zawierała liczby wybrane przez użytkownika.
my_numbers = []
# Wywołuję pętlę "while" która będzie wykonywała się dopuki użytkownik nie wprowadzi 6 liczb.
while len(my_numbers) != 6:
    # Robię odrazu "rzutowanie typów", tzn zmieniam string pobrany od użytkownika na liczbę
    number = int(input("Podaj liczbę od 1 do 50: "))
    # Instrukcja "if" sprawdza czy podana przez użytkownika liczba znajduje się już w jego zbiorze
    # jeśli nie, dodaje ją do zbioru.
    if number not in my_numbers:
        my_numbers.append(number)
    else:
        print("Podana liczba została już skreślona, wybierz inną liczbę!")

# Tworzę listę która będzie zawierała liczby losowe wybrane przez komputer.
lotto_numbers = []
# Wywołuję pętlę "while" która będzie wykonywała się dopuki w zbiorze "lotto_numbers" nie będzię 6 liczb.
while len(lotto_numbers) != 6:
    # losuję liczbę
    individual_number = random.randint(1,50)
    # Jeśli wylosowana liczba nie znajduje sie w "lotto_numbers" zostaje do niego dodana.
    if individual_number not in lotto_numbers:
        lotto_numbers.append(individual_number)

# Tworzę listę zawierającą moje liczby które wygrały.
score = []

# iteruję po liczbach które wprowadził użytkownik
for element in my_numbers:
    # jeśli liczba znajduje się w zbiorze wylosowanym przez komputer zostaje dodana do moich wyników
    if element in lotto_numbers:
        score.append(element)


print("Liczby wybrane przez ciebie: {}".format(my_numbers))
print("Liczby wylosowane przez komputer {}".format(lotto_numbers))

# Jeśli "score" jest "True" tzn nie równa się zero, wyświetlam wygrane liczby.
if score:
    print("Twoje liczby, które zostały wylosowane {}".format(score))
else:
    print("Niestety nie trafiłeś ani jedniej liczby!")






