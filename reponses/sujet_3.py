#Exercice 1 
def delta(liste: list)-> list :
    assert len(liste)!=0, "liste vide"
    
    liste_retour = []

    for i in range(len(liste)) :
        
        if i==0 :
            liste_retour.append(liste[i])
        else :
            liste_retour.append(liste[i]-liste[i-1])
    
    return liste_retour

assert(delta([1000, 800, 802, 1000, 1003])==[1000, -200, 2, 198, 3])
assert(delta([42])==[42])



#Exercice 2

class Noeud:
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d
    
    def __str__(self):
        return str(self.valeur)
    
    def est_une_feuille(self):
        '''Renvoie True si et seulement si le noeud est une feuille'''
        return self.gauche is None and self.droit is None


def expression_infixe(e):
    s = ""

    if e.gauche is not None:
        s="(" + s + str(expression_infixe(e.gauche))
    
    s = s + str(e)

    if e.droit is not None:
        s=s+str(expression_infixe(e.droit)) + ")"
    
    if True : # Je pense qu'ils voulaint qu'on utilise est_une_feuille mais bon
        return s
    

e = Noeud(Noeud(Noeud(None, 3, None), '*', Noeud(Noeud(None, 8, None), '+', Noeud(None, 7, None))), '-', Noeud(Noeud(None, 2, None), '+', Noeud(None, 1, None)))

print(expression_infixe(e))