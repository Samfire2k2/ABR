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

def afficherABR(A: ABR, profondeur=0):
    if A is not None:
        # Afficher le sous-arbre droit
        afficherABR(A.sad, profondeur + 1)
        # Afficher le noeud courant avec indentation
        print('   ' * profondeur + str(A.val))
        # Afficher le sous-arbre gauche
        afficherABR(A.sag, profondeur + 1)

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

def Manipuler_ABR_complet(A: ABR, p: int) -> ABR:
    n = 2 ** p + 1 - 1
    A_prime = A
    
    for i in range(2, p + 1):
        val_to_delete = 2 ** i - 1
        A_prime = SupprimerABR(A_prime, val_to_delete)
        A_prime = InsererABR(A_prime, val_to_delete)
    
    return A_prime

##TESTS DES FONCTIONS
arbre = ABR() # On crée un arbre binaire de recherche vide
arbre = InsererABR(arbre, 8)
arbre = InsererABR(arbre, 4)
arbre = InsererABR(arbre, 12)
arbre = InsererABR(arbre, 2)
arbre = InsererABR(arbre, 6)
arbre = InsererABR(arbre, 10)
arbre = InsererABR(arbre, 14)
arbre = InsererABR(arbre, 1)
arbre = InsererABR(arbre, 3)
arbre = InsererABR(arbre, 5)
arbre = InsererABR(arbre, 7)
arbre = InsererABR(arbre, 9)
arbre = InsererABR(arbre, 11)
arbre = InsererABR(arbre, 13)
arbre = InsererABR(arbre, 15)

print("Parcours préfixe :")
afficherABR_A_prefixe(arbre)

print("Parcours infixe :")
afficherABR_A_infixe(arbre)

print("Parcours suffixe :")
afficherABR_A_suffixe(arbre)
afficherABR(arbre)