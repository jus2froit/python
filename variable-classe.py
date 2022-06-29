class Chaise:
    #variable de class
    nombre_pieds = 4

    def __init__(self, couleur: str):
        #variable d'isntance
        self.couleur = couleur
    
    def get_couleur(self) -> str:
        return self.couleur
    
    def set_couleur(self, couleur: str):
        self.couleur = couleur

    @classmethod
    def get_nombre_pieds(cls):
        return cls.nombre_pieds

    @classmethod
    def set_nombre_pieds(cls, nombre_pieds: int):
        cls.nombre_pieds = nombre_pieds

chaise1 = Chaise("noir")
chaise2 = Chaise("noir")

#modif de la variable de class
Chaise.nombre_pieds = 3

#modif de la variable d'instance
chaise1.couleur = "blanc"

#creation d'une variable d'instance
chaise1.nombre_pieds = 5

#lecture d'une variable de class

print("Chaise.nombre_pieds: ", Chaise.nombre_pieds)

print("chaise1.nombres_pieds: ", chaise1.nombre_pieds)
print("chaise1.couleur: ", chaise1.couleur)

print("chaise.nombre_pied: ", chaise2.nombre_pieds)
print("chaise2.couleur: ", chaise2.couleur)