
###GENERATOR KODÓW POCZTOWYCH###

code_one = "79-900"

code_one = code_one.split("-")# Używam metody "split" aby podzielić string na listy, jako separator występuje "-"
code_one = int("".join(code_one))# Używam metody "join" aby połączyć dwie listy, separator to spacja, zmieniam typ na int


code_two = "80-155"

code_two = code_two.split("-")# Używam metody "split" aby podzielić string na listy, jako separator występuje "-"
code_two = int("".join(code_two))# Używam metody "join" aby połączyć dwie listy, separator to spacja, zmieniam typ na int


elements = []# Tworze listę wszystkich kodów bez znaku "-"
while code_one != code_two + 1:
    elements.append(code_one)
    code_one += 1


all_code = []# Tworze listę wszystkich kodów ze znakiem "-"
for element in elements:

    t = []# Lista robocza, będzie ona przydatna w dodaniu "-" do naszych elementów
    for i in str(element):# KOnieczna jest zmiana typu na str
        t.append(i)
        if len(t) == 2:
            t.append("-")

    single_code = "".join(t)# Łączę element w jeden string, jako separator spacja, dodaje element do listy all_code
    all_code.append(single_code)


print(all_code)
print(f"Wszystkich kodów jest: {len(all_code)}")




