
#Wyszukiwanie wzorców w tekście bez użycia wyrażeń regularnych

number = "417-555-901-1"


def is_phone_number(number):

    if len(number) != 12:
        return False
    if number.count("-") != 2:
        return False
    if number[3] == "-" and number[7] == "-":
        for i in number:
            if i != "-":
                if not i.isdecimal():
                    return False
    else:
        return False
    return True


print(is_phone_number(number))



