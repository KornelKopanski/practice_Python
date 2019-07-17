
# ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n.
# NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE.


collection = [12,14,13,17,19,18]


def check_the_collection(first_element,last_element,collection):
    missing_elements = []
    element = first_element

    while element != last_element+1:
        if element not in collection:
            missing_elements.append(element)
        element += 1

    print(f"Brakujące elementy to: {missing_elements}")

check_the_collection(10,20,collection)