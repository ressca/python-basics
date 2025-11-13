przejechane_km = float(input("Podaj liczbę przejechanych kilometrów: "))
spalanie_na_100km = float(input("Podaj średnie spalanie na 100 km (w litrach): "))
cena_paliwa_za_litr = float(input("Podaj cenę paliwa za litr: "))
pasazerowie = int(input("Podaj liczbę pasażerów: "))

ilosc_paliwa = (przejechane_km / 100) * spalanie_na_100km
koszt_paliwa = ilosc_paliwa * cena_paliwa_za_litr


print(f"Na trasie zużyje {ilosc_paliwa:.2f} litrów paliwa, a koszt paliwa to: {koszt_paliwa:.2f} zł")  

cena_na_osobe = koszt_paliwa / pasazerowie
print(f"Koszt paliwa na osobę wynosi: {cena_na_osobe:.2f} zł")

if przejechane_km > 500:
    print("ługa trasa - zaplanuj przerwy na odpoczynek!")