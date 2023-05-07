from hub import Hub
from edit_fighter import Edit_Fighters

if __name__ == "__main__":
    h = Hub()
    e = Edit_Fighters()
    
    while True:
        print("1 - wyświetl zawodników, 2 - dodaj zawodnika, 3 - usuń zawodnika, 0 - zakończ")
        opcja = input("podaj liczbę: ")
        if opcja == "1":
            e.show_fighters()
        elif opcja == "2":
            h.Wpisz_dane()
        elif opcja == "3":
            h.Wpisz_imie_nazwisko()
            e.delete_fighter(h.wName,h.wSurname)
        elif opcja == "0":
            break
        else:
            print("Nie znaleziono opcji!")
        
