#exercice 1

def recherche(liste: list)->list :
    liste_retour = []
    if len(liste)==0 :
        return liste_retour

    for i in range(len(liste)) :
        if i>1 :
            if (liste[i]-1)==liste[i-1] :
                couple = liste[i-1],liste[i]
                liste_retour.append(couple)

    return liste_retour

print(recherche([0,1,2,3,5,6,-5,-4]))



#Exrecice 2

def propager(M, i, j, val):
    if M[i][j]== 0:
        return M

    M[i][j]=val

    # l'élément en haut fait partie de la composante
    if ((i-1) >= 0 and M[i-1][j] == 1):
        propager(M, i-1, j, val)

    # l'élément en bas fait partie de la composante
    if ((i+1) < len(M) and M[i+1][j] == 1):
        propager(M, i+1, j, val)

    # l'élément à gauche fait partie de la composante
    if ((j-1) >= 0 and M[i][j-1] == 1):
        propager(M, i, j-1, val)

    # l'élément à droite fait partie de la composante
    if ((j+1) < len(M) and M[i][j+1] == 1):
        propager(M, i, j+1, val)


M = [[0,0,1,0],[0,1,0,1],[1,1,1,0],[0,1,1,0]]

propager(M,2,1,3)

print(M)