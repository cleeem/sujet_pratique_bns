#exercice 1

def moyenne(liste: list)->float :
    somme_note = 0
    nombre_notes = 0

    for couple in liste :
        note = couple[0]
        coefficient = couple[1]

        somme_note += note * coefficient
        nombre_notes += 20 * coefficient

    moyenne_note = somme_note / nombre_notes
    moyenne_note = moyenne_note * 20
    return moyenne_note

assert(moyenne([(15,2),(9,1),(12,3)]) == 12.5)


#exercice 2

def pascal(n):
    C= [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i] )
        Ck.append(1)
        C.append(Ck)
    return C

assert(pascal(4)==[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])
assert(pascal(5)==[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]])