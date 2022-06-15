
class Vehicule:
    """
    cette classe represente un vehicile 
    ATTENTION c'est une classe abstraite
    elle est destinée à etre étendue à des classes enfants
    """
    #les variables déclaré directement declarer dans la classe sont "des variables de classe "
    #le _ permert d'indiquer que la variable est privé
    #ATTENTIOn elle reste tout de meme accessible de l'exterieur
    _acceleration = 10

    def __init__(self, marque: str, modele: str, carburant: str, vitesse: int):
        self._marque = marque
        self._modele = modele
        self._carburant = carburant
        self.set_vitesse(vitesse)

    def __str__(self):
        return f"{self._marque} {self._modele} {self._carburant} {self._vitesse}"


    def get_vitesse(self) -> int:
        return self._vitesse

        #il faut utiliser le setter s'il y a une procedure speciale de verification
        # des donnees avant l'affectation

    def set_vitesse(self, vitesse: int):
        if type(vitesse) is not int:
            raise Exception("la vitesse doit être un nombre entier")
        self._vitesse = vitesse

    def get_marque(self):
        return self._marque

    def get_modele(self):
        return self._modele

    def get_carburant(self):
        return self._carburant

    def accelerer(self):
        vitesse = self.get_vitesse()
        vitesse += self._acceleration
        self.set_vitesse(vitesse)

    def ralentir(self):
        vitesse = self.get_vitesse()
        vitesse -= self._acceleration
        self.set_vitesse(vitesse)
