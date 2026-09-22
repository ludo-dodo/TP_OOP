from habitant import Habitant, Adulte, Enfant

class Village:
    def __init__(self, nom):
        self.__nom = nom
        self.__habitants = []
    
    def ajouter_habitant_composition(self, nom, age, adresse, animaux=None):
        if age >= 18:
            habitant = Adulte(nom, "", age, adresse, animaux)
        else:
            habitant = Enfant(nom, "", age, adresse, animaux)
        self.__habitants.append(habitant)
        #composition : le village crée et possède l'habitant

    def ajouter_habitant_agregation(self, habitant):
        self.__habitants.append(habitant)
        #agregation : le village utilise un habitant existant
    
    def get_habitants(self):
        return self.__habitants

    def afficher_habitants(self):
        for habitant in self.__habitants:
            print(f"{habitant.get_nom()} habite à {habitant.get_adresse()}.")

if __name__ == "__main__":
    pytown = Village("PyTown")
    pytown.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})

    elise = Adulte("Elise", "", 28, "Rue B", {"poules": 10})
    pytown.ajouter_habitant_agregation(elise)

    autre_village = Village("VillageVoisin")
    autre_village.ajouter_habitant_agregation(elise) # meme habitant dans 2 villages

    assert len(pytown.get_habitants()) == 2
    assert elise in autre_village.get_habitants()


    # 5.3 : ajouter_habitant_composition illustre une relation de composition, car on crée habitant à l'intérieur de la méthode et donc il est dépendant du village. Si le village est détruit, l'habitant l'est aussi.
    # alors que ajouter_habitant_agregation illustre une relation d'agrégation, le village reçoit un objet Habitant déjà existant, l'habitant peut exister indépendamment