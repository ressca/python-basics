produkty = ('mleko', 'chleb', 'jajka', 'masło', 'ser', 'jabłka', 'banany', 'pomarańcze', 'ziemniaki', 'marchew')

koszyk = []

for i in range(3):
    produkt = input(f'Podaj nazwę produktu: ')
    if produkt in produkty:
        print(f'Produkt "{produkt}" zostal dodany do koszyka.')
        koszyk.append(produkt)
    else:
        print(f'Produkt "{produkt}" jest niedostępny.')

koszyk.sort()

print('Zawartość koszyka:')
for item in koszyk:
    print(f'- {item}')