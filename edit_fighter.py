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

    def delete_fighter(self, name, surname):
        fighters = self.fighter_cls.load()
        matching_fighters = [
            (index, fighter) for index, fighter in enumerate(fighters)
            if fighter.name == name and fighter.surname == surname
        ]

        if matching_fighters:
            print("Znaleziono następujących zawodników:")
            k = 1
            for i, fighter in matching_fighters:
                print(f"Zawodnik: {k} Name: {fighter.name}, Surname: {fighter.surname}, Weight Class: {fighter.weight_class}, Position: {fighter.position_in_ranking}")
                k += 1
            fighter_index = int(input("Którego zawodnika chcesz usunąć? Podaj numer: "))

            if 1 <= fighter_index <= len(matching_fighters):
                index, _ = matching_fighters[fighter_index-1]
                self.fighter_cls.delete_fighter(index)
                print(f"Pomyślnie usunięto zawodnika o imieniu {name} i nazwisku {surname}")
            else:
                print("Podano nieprawidłowy numer zawodnika.")
        else:
            print("Nie znaleziono takiego zawodnika")
    
    
    def show_fighters(self):
        fighters = self.fighter_cls.load()
        if fighters:
            for fighter in fighters:
                print(f"Name: {fighter.name}, Surname: {fighter.surname}, Weight Class: {fighter.weight_class}, Position: {fighter.position_in_ranking}")
        else:
            print("Brak zawodników")
