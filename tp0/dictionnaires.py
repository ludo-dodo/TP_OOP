#Q1
pieces_stock = {
"ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
"ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
}

def quantite_piece(stock,modele,piece):
    return stock[modele][piece]

assert quantite_piece(pieces_stock, "ModeleA","moteurs") == 10

#Q2

def consommer_piece(stock,modele,piece,nombre):
    stock[modele][piece]-=nombre

def ajouter_modele(stock,nv_modele,nv_piece):
    stock[nv_modele] = nv_piece


def total_pieces (stock):
    
    nb_m=0
    nb_c=0
    nb_r=0
    for modele, piece in stock.items():
        nb_m+=piece["moteurs"]
        nb_c+=piece["capteurs"]
        nb_r+=piece["roues"]
    return {
        "moteurs": nb_m,
        "capteurs": nb_c,
        "roues": nb_r,
    }

consommer_piece(pieces_stock, "ModeleA","moteurs", 3)
assert pieces_stock["ModeleA"]["moteurs"] == 7

ajouter_modele(pieces_stock, "ModeleC", {"moteurs": 4, "capteurs": 10, "roues": 16})

assert pieces_stock["ModeleC"] == \
    {"moteurs": 4, "capteurs": 10, "roues": 16}

totaux = total_pieces(pieces_stock)
assert totaux == {"moteurs": 17, "capteurs": 50, "roues": 80}