import time
import csv
##Algo Python - Conception et analyse d'algorithmes
##TP2 - ABR
class ABR:
    def __init__(self, val=None, sag=None, sad=None):
        self.val = val
        self.sag = sag
        self.sad = sad

def InsererABR(A: ABR, x: int) -> ABR:
    if A is None: 
        A = ABR(x) 
    else: 
        if A.val is None: # Si la valeur du noeud est None
            A.val = x # On la met à jour avec x
        elif x <= A.val: 
            A.sag = InsererABR(A.sag, x) 
        else: 
            A.sad = InsererABR(A.sad, x) 
    return A

def Creer_ABR_complet(p: int) -> ABR:
    n = 2 ** p + 1 - 1
    T = [None] * n
    T[0] = 2 ** p
    k = 1
    
    for i in range(p - 1, -1, -1):
        T[k] = 2 ** i
        k += 1
        for j in range(1, 2 ** (p - i)):
            T[k] = T[k - 1] + 2 ** (i + 1)
            k += 1
    
    A = None
    for val in T:
        A = InsererABR(A, val)
    return A

def afficherABR_A_prefixe(A: ABR):
    if A is not None:
        print(A.val)
        afficherABR_A_prefixe(A.sag)
        afficherABR_A_prefixe(A.sad)

def afficherABR_A_infixe(A: ABR):
    if A is not None:
        afficherABR_A_infixe(A.sag)
        print(A.val)
        afficherABR_A_infixe(A.sad)

def afficherABR_A_suffixe(A: ABR):
    if A is not None:
        afficherABR_A_suffixe(A.sag)
        afficherABR_A_suffixe(A.sad)
        print(A.val)

def Creer_ABR_filiforme(p: int) -> ABR:
    n = 2 ** p + 1 - 1
    T = [None] * n
    
    # Créer le tableau T
    for i in range(n):
        T[i] = i + 1
    
    A = None
    # Insérer les éléments de T dans l'ABR
    for val in T:
        A = InsererABR(A, val)
    
    return A


##TESTS DES FONCTIONS
arbre = ABR() # On crée un arbre binaire de recherche vide
arbre = InsererABR(arbre, 5)
arbre = InsererABR(arbre, 8)
arbre = InsererABR(arbre, 2)
arbre = InsererABR(arbre, 7)
arbre = InsererABR(arbre, 10)

print("Parcours préfixe :")
afficherABR_A_prefixe(arbre)

print("Parcours infixe :")
afficherABR_A_infixe(arbre)

print("Parcours suffixe :")
afficherABR_A_suffixe(arbre)
