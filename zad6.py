def student_info():
    student = {}

    student['imie'] = input("Podaj swoje imię: ")
    student['nazwisko'] = input("Podaj swoje nazwisko: ")
    student['rok_studiow'] = input("Podaj rok studiów: ")
    student['kierunek'] = input("Podaj kierunek studiów: ")

    ile_ocen = int(input("Ile masz ocen? "))
    oceny = []
    for i in range(ile_ocen):
        ocena = float(input(f"Podaj ocenę {i + 1}: "))
        oceny.append(ocena)
    student['oceny'] = oceny

    student['srednia_ocen'] = sum(oceny) / len(oceny)

    bok_a = float(input("Podaj długość boku a prostokąta: "))
    bok_b = float(input("Podaj długość boku b prostokąta: "))
    student['pole_prostokata'] = bok_a * bok_b
    student['obwod_prostokata'] = 2 * (bok_a + bok_b)

    return student

print(student_info())