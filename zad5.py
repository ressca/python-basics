from collections import Counter

def analizuj_tekst():
    dict = {}

    tekst = input("Podaj tekst do analizy: ")
    formatted_text = tekst.strip().lower().replace("python", "PYTHON")

    dict['tekst_sformatowany'] = formatted_text

    reversed_text = tekst = ''.join(" " + word[::-1] for word in tekst.split())
    dict['tekst_odwrocony'] = reversed_text

    litery = [char for char in tekst if char.isalpha()]
    counts = Counter(litery)

    dict['licznik_liter'] = counts

    return dict

print(analizuj_tekst())