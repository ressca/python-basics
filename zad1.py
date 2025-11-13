from datetime import date

rok_ur = int(input("Podaj rok urodzenia: "))

current_year = date.today().year

wiek = current_year - rok_ur

if wiek >= 18:
    print("Jesteś pełnoletni")
else:
    print("jesteś niepełnoletni")