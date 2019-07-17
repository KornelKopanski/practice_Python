
# ZADANIE 1. GENERATOR KODÓW POCZTOWYCH

code_one = "79-900"

code_two = "80-155"

def separator(code):

    x = code.split("-")
    new_code = int("".join(x))
    return new_code

code_one = separator(code_one)
code_two = separator(code_two)

all_code = []# Tworze listę wszystkich kodów ze znakiem "-"

def generator(code_one,code_two):

    elements = []# Tworze listę wszystkich kodów bez znaku "-"
    code = code_one
    while code != code_two + 1:
        elements.append(code)
        code += 1

    for element in elements:
        t = []# Lista robocza, będzie ona przydatna w dodaniu "-" do naszych elementów
        for i in str(element):
            t.append(i)
            if len(t) == 2:
                t.append("-")

        single_code = "".join(t)
        all_code.append(single_code)

generator(code_one,code_two)

print(all_code)
print(f"Wszystkich kodów jest: {len(all_code)}")




