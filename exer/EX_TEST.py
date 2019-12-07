

site_company = []

x = None

while x != "0":

    site = input("Wprowadź stronę www firmy: ")
    if site not in site_company:
        site_company.append(site)
    else:
        print(f"Strona {site} istnieje już w zbiorze!")

    x = input("Aby zakończyć wpisz '0', w przeciwnym razie naciśnij 'enter'!")

print(site_company)