#Exercice 1

def recherche(caractere:str , mot : str)->int :
    if  len(mot) == 0 : #on verifie que le mot contienne des caracteres
        return 0

    occurence : int = 0 #le nombre d'occurence de la lettre dans le mot en entrée

    for lettre in mot : #parcours de chaque lettres du mot en entrée
        if lettre == caractere : #comparaison de la lettre et du caractere en entrée
            occurence += 1 #incrémentation du nombre d'occurences
    
    return occurence

assert(recherche('e', "sciences")==2)     ######################
assert(recherche('i',"mississippi")==4)   # liste d'assertions #
assert(recherche('a',"mississippi")==0)   ######################



#Exercice 2

Pieces = [100,50,20,10,5,2,1]
def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:
        return solution
    p = Pieces[i]
    if p <= arendre :
        solution.append(p)
        return rendu_glouton(arendre - p, solution, i)
    else :
        return rendu_glouton(arendre, solution, i+1)

assert(rendu_glouton(68,[],0)==[50, 10, 5, 2, 1])
assert(rendu_glouton(291,[],0)==[100, 100, 50, 20, 20, 1])