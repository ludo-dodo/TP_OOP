import unittest

from habitant import Habitant, Adulte, Enfant
from village import Village

class TestHabitant(unittest.TestCase):
    #Tests pour la classe Habitant et l'encapsulation.

    def test_compte_animal(self):
        #Teste le cas usuel et le cas limite où l'animal n'est pas possédé
        h = Adulte("Aldric", "", 25, "Rue A", {"vaches": 3})
        self.assertEqual(h.compte_animal("vaches"), 3) # Cas usuel
        self.assertEqual(h.compte_animal("moutons"), 0) # Cas limite

    def test_age_setter_valide(self):
        #Teste la modification de l'âge avec une valeur valide.
        h = Adulte("Aldric", "", 25, "Rue A")
        h.age = 26
        self.assertEqual(h.age, 26)

    def test_age_setter_invalide(self):
        #Cas limite : âge négatif
        h = Adulte("Aldric", "", 25, "Rue A")
        with self.assertRaises(ValueError):
            h.age = -5


class TestVillage(unittest.TestCase):
    #Tests pour les méthodes du Village.

    def test_ajout_composition(self):
        #Teste l'ajout d'un habitant par composition.
        v = Village("PyTown")
        v.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})
        self.assertEqual(len(v.get_habitants()), 1)
        self.assertEqual(v.get_habitants()[0].get_nom(), "Aldric")

    def test_ajout_agregation_cas_limite(self):
        #Cas limite : le même habitant ajouté par agrégation à deux villages différents
        pytown = Village("PyTown")
        autre_village = Village("VillageVoisin")
        elise = Adulte("Elise", "", 28, "Rue B", {"poules": 10})

        pytown.ajouter_habitant_agregation(elise)
        autre_village.ajouter_habitant_agregation(elise)

        # Vérifie qu'Elise apparaît bien dans les deux listes
        self.assertIn(elise, pytown.get_habitants())
        self.assertIn(elise, autre_village.get_habitants())


class TestHeritage(unittest.TestCase):
    #Tests pour le comportement des classes dérivées Adulte et Enfant

    def test_calcul_retraite_coherent(self):
        #Vérifie le résultat pour un Adulte et un Enfant
        adulte = Adulte("Dupont", "Marie", 35, "Rue A")
        enfant = Enfant("Martin", "Lucas", 12, "Rue B")

        self.assertEqual(adulte.calcul_nombre_annee_avant_retraite(), 27)
        self.assertEqual(enfant.calcul_nombre_annee_avant_retraite(), "Erreur: un enfant ne peut pas calculer sa retraite")

    def test_creation_enfant_limite(self):
        #Cas limite : la création d'un Enfant de 20 ans lève bien une ValueError[cite: 1].
        with self.assertRaises(ValueError):
            Enfant("Oups", "Erreur", 20, "Rue C")


if __name__ == "__main__":
    unittest.main(verbosity=2)