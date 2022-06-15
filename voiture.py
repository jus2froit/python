from vehicule import Vehicule

class Voiture(Vehicule):
    """
    cette classe represente une voiture
    c'est une classe concréte qui étend (ou herite de ) la classe Vehicule
    Cette classe est destiné a etre instancier
    """

    #redéfinir une variable/methode de classe mere dans une classe enfant s'appelle surcharger un variable de classe
    _acceleration = 20

    def __init__(self, marque: str, modele: str, carburant: str, vitesse: int,  type_carosserie: str):
        super().__init__(marque, modele, carburant, vitesse)
        self._type_carosserie = type_carosserie

    def __str__(self):
        return f"{super().__str__()} {self._type_carosserie}"

    def get_type_carosserie(self):
        return self._type_carosserie

