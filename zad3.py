wyniki = (45, 67, 82, 90, 55, 74, 100, 61)

avg = sum(wyniki) / len(wyniki)
print("Średnia wyników: ", avg)

max_wynik = max(wyniki)
if max_wynik == 100:
    print("Gratulacje dla najlepszego uczestnika!")

zdali = sum(1 for w in wyniki if w >= 60)
print(f"Liczba uczestników, którzy zdali test: {zdali}")