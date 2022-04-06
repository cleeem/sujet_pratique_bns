#Exercice 1
def renverse(chaine:str)->str :
    new_chaine = ""
    for lettre in chaine :
        new_chaine = lettre + new_chaine
    return new_chaine

print(renverse("kayak"))



def crible(N) :
    """renvoie un tableau contenant tous les nombres premiers plus petit que N"""
    premiers = []
    tab = [True] * N
    tab[0], tab[1] = False, False
    for i in range(0, N):
        if tab[i] == True:
            premiers.append(i)
            for multiple in range(2*i, N, i):
                tab[multiple] = False
    return premiers

assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
