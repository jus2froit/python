from vehicule import Vehicule

class Camion(Vehicule):
    """"
    cette classe represente un camion
    c'est une classe concréte qui étend (ou herite de ) la classe Vehicule
    Cette classe est destiné a etre instancier
    """
    def __init__(self, marque: str, modele: str, carburant: str, vitesse: int, ptac: float):
        super().__init__(marque, modele, carburant, vitesse)
        self.set_ptac(ptac)
        
        
    def set_ptac(self, ptac: float):
        if type(ptac) != float:
            raise Exception("le ptac doit etre un float")
        self._ptac = ptac

    def get_ptac(self):
        return self._ptac

    def __str__(self):
        return f"{super().__str__()} {self._ptac}"
