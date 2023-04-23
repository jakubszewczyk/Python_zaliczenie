import pickle
from prepare_list import Fighter


class Read_Save_Fighter:
    
    def __init__(self):
        self._file_location = "./fighters.pickle"
    
    def save(self, fighter:Fighter) -> None:
        fighters_list = self.load()
        fighters_list.append(fighter)
        
        with open(self._file_location, 'wb') as file:
            pickle.dump(fighters_list,file)
    
    def load(self) -> list:
        try:
            with open(self._file_location, "rb") as file:
                return pickle.load(file)
        except Exception:
            print("Pickle file does not exist...")
            return []
        
    def delete_fighter(self, id):
        fighters_list = self.load()
        fighters_list.pop(id)

        with open(self._file_location, 'wb') as file:
            pickle.dump(fighters_list,file)
        
