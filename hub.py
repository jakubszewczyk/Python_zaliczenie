from edit_fighter import Edit_Fighters


class Hub:
    def __init__(self):
        self.fighters = Edit_Fighters()
    
    def Wpisz_dane(self):
        hName = input("Podaj imię: ")
        hSurname = input("Podaj Nazwisko: ")
        hWeight_class = input("Podaj klasę wagową: ")
        hRecordW = [input("Podaj liczbę zwycięstw: "),
                    input("Podaj liczbę porażek: ")
                    ]
        hPosition_in_ranking = input("podaj pozycję w rankingu: ")
        
        self.fighters.new_fighter(hName,hSurname,hWeight_class,hRecordW,hPosition_in_ranking)
        print("Dodano nowego zawodnika")