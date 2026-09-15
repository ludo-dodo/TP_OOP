releve1 = ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]


def afficher_releve(releve):
    return f"Capteur {releve[0]} : {releve[1]} {releve[2]}"


# Tests question 1
assert len(releves) == 3
assert releves[0][0] == "laser_avant"
assert afficher_releve(releve1) == "Capteur laser_avant : 2.35 m"


def recalibrer(releves,nom_capteur,valeur_change):
    nouveaux_releves=[]
    for i in range(len(releves)):
        if(releves[i][0]==nom_capteur):
            nouveau_releve=(nom_capteur,valeur_change,releves[i][2])
            nouveaux_releves.append(nouveau_releve)
        else:
            nouveaux_releves.append(releves[i])
    return nouveaux_releves


# Tests question 2
nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)
assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
assert nouveaux_releves[1] == releve2
assert nouveaux_releves[2] == releve3

