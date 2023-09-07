# Inicjalizacja pustej bazy danych pojazdów jako lista zagnieżdżona.
# Każdy wpis w bazie danych to lista zawierająca dane pojazdu: marka, model, rocznik, silnik, moc, waga.
car_catalog = []

# Funkcja addCar dodaje nowy pojazd do bazy danych car_catalog.
# Sprawdzamy typ każdego argumentu, aby upewnić się, że są poprawnego typu.
def addCar(marka: str, model: str, rocznik: int, silnik: str, moc: int, waga: int):
    if not isinstance(marka, str):
        print("Marka musi być typem STRING")
        return
    if not isinstance(model, str):
        print("Model musi być typem STRING")
        return
    if not isinstance(rocznik, int):
        print("Rocznik musi być typem INT")
        return
    if not isinstance(silnik, str):
        print("Silnik musi być typem STRING")
        return
    if not isinstance(moc, int):
        print("Moc musi być typem INT")
        return
    if not isinstance(waga, int):
        print("Waga musi być typem INT")
        return
    
    # Dodajemy dane pojazdu (po przekształceniu marki na wielkie litery) do bazy danych.
    car_catalog.append([marka.upper(), model, rocznik, silnik, moc, waga])
    print("Pomyślnie dodano ", marka, " ", model, " do bazy danych!")

# Funkcja calcPowerToMassRatio oblicza stosunek mocy do wagi dla pojazdów w bazie danych,
# które pasują do przekazanych argumentów (np. moc) i wyświetla wyniki.
def calcPowerToMassRatio(*args):
    if len(args) > 0:
        found_list = {}
        
        # Tworzymy słownik, w którym klucze to ilość dopasowanych argumentów,
        # a wartości to listy pasujących pojazdów.
        for i in range(6):
            found_list[i] = []
        
        # Iterujemy przez bazę danych pojazdów i liczymy ilość dopasowań.
        for car_entry in range(len(car_catalog)):
            match_amount = 0
            for argument in args:
                if argument in car_catalog[car_entry]:
                    match_amount += 1
            if match_amount > 0:
                found_list[match_amount].append(car_catalog[car_entry])
        
        # Znajdujemy największą ilość dopasowań.
        biggest_matches = 0
        for matches in found_list:
            if len(found_list[matches]) > biggest_matches:
                biggest_matches = matches
        
        # Wyświetlamy informację o ilości znalezionych pasujących pojazdów.
        print("Najwięcej dopasowań", biggest_matches, "argumentów, znaleziono:", len(found_list[biggest_matches]), "aut pasujących do wprowadzonych argumentów")
        
        # Wyświetlamy szczegóły pojazdów pasujących do największej ilości argumentów.
        for car in found_list[biggest_matches]:
            power_to_mass_ratio = round(car[4] / car[5], 3)
            print(f"Pojazd:{car[0]} ||Model:{car[1]} ||Rocznik:{car[2]} ||Silnik:{car[3]} ||Stosunek mocy do wagi:{power_to_mass_ratio}")

# Dodajemy kilka pojazdów do bazy danych za pomocą funkcji addCar.
addCar("BMW", "E46", 1999, "M52B28TU", 193, 1350)
addCar("BMW", "E46", 1999, "M52B28TU", 193, 1330)
addCar("BMW", "E46", 1999, "M52B28TU", 193, 1300)
addCar("BMW", "E46", 1999, "M52B28TU", 194, 1400)

# Wywołujemy funkcję calcPowerToMassRatio, przekazując jako argument moc. Wszystkie auta z mocą 194 koni będą wyświetlone
calcPowerToMassRatio(194)
