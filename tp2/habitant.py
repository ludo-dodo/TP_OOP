class Habitant:
    def __init__(self, nom, age, adresse, animaux=None): #initialise un nouvel objet Habitant
        self.__nom = nom
        self.__age = age
        self.__adresse = adresse
        self.__animaux = {} if animaux is None else animaux

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, valeur):
        if valeur < 0 or valeur > 130:
            raise ValueError("L'âge doit être compris entre 0 et 130.")
        self.__age = valeur
    
    #Accesseurs (getters)
    def get_nom(self):
        return self.__nom

    def get_adresse(self):
        return self.__adresse

    def get_animaux(self):
        return self.__animaux
    
    #Mutateurs (setters)
    def set_nom(self, nom):
        self.__nom = nom

    def set_adresse(self, adresse):
        self.__adresse = adresse

    def set_animaux(self, animaux):
        self.__animaux = animaux
        

    def affichage_adresse(self):
        print(f"{self.get_nom()} habite à {self.get_adresse()}.") #affiche l'adresse de l'habitant
    
    def compte_animal(self, animal):
        return self.get_animaux().get(animal, 0) #Renvoie le nombre d'animaux, ou 0 s'il n'est pas dans le dictionnaire

h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})

# Tests de validation
assert h1.get_nom() == "Aldric"
assert h1.compte_animal("vaches") == 3
assert h1.compte_animal("moutons") == 0
h1.affichage_adresse() # affiche "Aldric habite a Rue A"

#Tests pour la 4.2
h1.age = 26
assert h1.age == 26
try:
    h1.age = -5
    assert False,"une ValueError aurait du etre levee"
except ValueError:
    pass