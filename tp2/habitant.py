from multipledispatch import dispatch
from abc import ABC, abstractmethod


class Habitant(ABC):
    def __init__(self, nom, age, adresse, animaux=None): #initialise un nouvel objet Habitant
        self.__nom = nom
        self.__age = age
        self.__adresse = adresse
        self.__animaux = {} if animaux is None else animaux

    @abstractmethod
    def calcul_nombre_annee_avant_retraite(self):
        pass

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

    #exo6
    @dispatch(object, str) #surchage pour string
    def set_info(habitant, nom):
        habitant._Habitant__nom = nom

    @dispatch(object, str, int) #surcharge pour string + int
    def set_info(habitant, nom, age):
        habitant._Habitant__nom = nom
        habitant._Habitant__age = age

    def __str__(self):
        return f"{self.get_nom()}, {self.age} ans, habite a {self.get_adresse()}"

class Adulte(Habitant):
    def __init__(self, nom, prenom, age,adresse):
        if age < 18:
            raise ValueError("Un adulte doit avoir au moins 18 ans")

        nom_complet = f"{nom} {prenom}" #fusionne le nom et le prénom pour la class habitant

        super().__init__(nom_complet, age, adresse)

    def calcul_nombre_annee_avant_retraite(self):
        age_retraite = 62
        if self.age >= age_retraite:
            return "Deja a la retraite"
        else:
            return age_retraite - self.age

class Enfant(Habitant):
    def __init__(self, nom, prenom, age, adresse):
        if age >= 18:
            raise ValueError("Un enfant doit avoir moins de 18 ans")

        nom_complet = f"{nom} {prenom}" #fusionne le nom et le prénom pour la class habitant


        super().__init__(nom_complet, age, adresse)

    def calcul_nombre_annee_avant_retraite(self):
        return "Erreur: Un enfant ne peut pas calculer sa retraite"

#h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})

# Tests de validation
#assert h1.get_nom() == "Aldric"
#assert h1.compte_animal("vaches") == 3
#assert h1.compte_animal("moutons") == 0
#h1.affichage_adresse() # affiche "Aldric habite a Rue A"

#test pour l'exo 7
adulte = Adulte("Dupont","Marie", 35, "Rue A")
enfant = Enfant("Martin","Lucas", 12, "Rue B")

assert isinstance(adulte, Habitant)
assert adulte.calcul_nombre_annee_avant_retraite() == 27
assert "enfant" in enfant.calcul_nombre_annee_avant_retraite()

try:
    Enfant("Oups", "Inconnu", 25, "Rue C")
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass

#Tests pour la 4.2
#h1.age = 26
#assert h1.age == 26
#try:
    #h1.age = -5
    #assert False,"une ValueError aurait du etre levee"
#except ValueError:
    #pass