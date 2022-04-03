#Exercice 1

def maxi(liste: list)->tuple :
    couple = (liste[0],0)
    
    for i in range(len(liste)) :
        if liste[i]>couple[0] :

            couple = (liste[i],i)
    
    return couple
assert(maxi([1,5,6,9,1,2,3,7,9,8])==(9,3))


#Exercice 2

def recherche(gene, seq_adn)->bool:

    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False

    while i < len(seq_adn) and trouve == False :
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            j+=1
        if j == g:
            trouve = True
        i+=1

    return trouve

print(recherche("AATC", "GTACAAATCTTGCC"))
print(recherche("AGTC", "GTACAAATCTTGCC"))