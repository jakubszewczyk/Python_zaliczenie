from fighter_save import Read_Save_Fighter
from prepare_list import Fighter
from pydantic import ValidationError


class Edit_Fighters:
    
    def __init__(self):
        self.fighter_cls = Read_Save_Fighter()
    
    def new_fighter(self, name_, surname_, weight_class_, record_, position_in_ranking_):
        try:
            fighter =  Fighter(name = name_,
                            surname = surname_,
                            weight_class = weight_class_,
                            record = record_,
                            position_in_ranking= position_in_ranking_
                            )
            self.fighter_cls.save(fighter)
        except ValidationError as e:
            print(e)

    def delete_fighter(self):
        self.show_fighters()
        imie = input("podaj imie: ")
        nazwisko = input("podaj nazwisko: ")
        indeks = 1

        for fighter in self.fighter_cls.load():
            if fighter.name == imie and fighter.surname == nazwisko:
                print(f"Zawodnik: {indeks} Name: {fighter.name}, Surname: {fighter.surname}, Weight Class: {fighter.weight_class}, Position: {fighter.position_in_ranking}")
                indeks = indeks + 1
                
        ktory_zawodnik = int(input("Chcę usunąć zawodnika: "))
        indeks = 1
        
        for id, fighter in enumerate(self.fighter_cls.load()):
            if fighter.name == imie and fighter.surname == nazwisko:
                if indeks == ktory_zawodnik:
                    self.fighter_cls.delete_fighter(id)
                    print(f"Pomyślnie usunięto zawodnika o imieniu {imie} i nazwisku {nazwisko}")
                    return
                elif indeks < ktory_zawodnik:
                    indeks = indeks + 1
        
        print("Nie znaleziono takiego zawodnika")
    
    
    def show_fighters(self):
        for fighter in self.fighter_cls.load():
            print(f"Name: {fighter.name}, Surname: {fighter.surname}, Weight Class: {fighter.weight_class}, Position: {fighter.position_in_ranking}")
            
