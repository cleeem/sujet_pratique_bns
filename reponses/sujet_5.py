#Exercice 1

def rechercheMinMax(liste:list)->dict :

    if len(liste)==0 :
        dico = {
            "min": None,
            "max": None,
        }
        return dico

    mini = liste[0]
    maxi = liste[0]

    for elt in liste :
        if elt<mini :
            mini = elt
        if elt>maxi :
            maxi = elt
    
    dico = {
        "min" : mini,
        "max" : maxi,
    }
    return dico

tableau = [0, 1, 4, 2, -2, 9, 3, 1, 7, 1]
print(rechercheMinMax(tableau))



class Carte:
    """Initialise Couleur (entre 1 a 4), et Valeur (entre 1 a 13)"""
    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur = v

    """Renvoie le nom de la Carte As, 2, ... 10, 
       Valet, Dame, Roi"""
    def getNom(self):
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle' ][self.Couleur - 1]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    """Remplit le paquet de cartes"""
    def remplir(self):
	    self.contenu = [ Carte(couleur,valeur) for couleur in range(1, 5) for valeur in range( 1, 14)]
    
    """Renvoie la Carte qui se trouve a� la position donnee"""
    def getCarteAt(self, pos):
        if 0 <= pos < 52-1 :
            return f"{self.contenu[int(pos/4)].getNom()} de {self.contenu[int(pos/4)].getCouleur()} "

    

unPaquet = PaquetDeCarte()
unPaquet.remplir()
uneCarte = unPaquet.getCarteAt(51)
print(uneCarte)