#Noms non explicites : Le nom de la fonction f et les variables d, t, c ne veulent rien dire
#Paramètre inutilisé: L'argument d est déclaré mais n'est jamais utilisé dans la fonction.
#Absence de docstring: aucun commentaire n'explique ce que fait la fonction.

import math

coef_terrain = {
    "R": 1.0,
    "H": 1.5,
    "S": 2.0,
}
cout_terrain_defaut = 3.0


def cout_deplacement_propre(type_terrain, x1, y1, x2, y2):
    distance = math.hypot(x2 - x1, y2 - y1)
    facteur = coef_terrain.get(type_terrain, cout_terrain_defaut)
    return distance * facteur


assert cout_deplacement_propre("R", 0, 0, 3, 4) == 5.0
assert cout_deplacement_propre("H", 0, 0, 3, 4) == 7.5
assert cout_deplacement_propre("S", 0, 0, 3, 4) == 10.0
assert cout_deplacement_propre("inconnu", 0, 0, 3, 4) == 15.0