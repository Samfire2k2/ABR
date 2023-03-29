
import time
import csv
import sys
sys.setrecursionlimit(10000)

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

def RechercherABR(A: ABR, x: int) -> bool:
    if A is None:
        return False
    elif A.val == x:
        return True
    elif x < A.val:
        return RechercherABR(A.sag, x)
    else:
        return RechercherABR(A.sad, x)

def SupprimerABR(A: ABR, x: int) -> ABR:
    if A is None:
        return A
    if A.val == x:
        if A.sag is None:
            return A.sad
        if A.sad is None:
            return A.sag
        min_droit = A.sad
        while min_droit.sag is not None:
            min_droit = min_droit.sag
        A.val = min_droit.val
        A.sad = SupprimerABR(A.sad, min_droit.val)
        return A
    elif x < A.val: 
        A.sag = SupprimerABR(A.sag, x) 
        return A
    else: 
        A.sad = SupprimerABR(A.sad, x) 
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

def creer_ABR_complet(n):
    T=[]
    k=2

    for i in range(0,n+1):
        T.append(0)

    T[1]=(n+1)//2

    for i in range ((n+1)//2 - 1, -1, -1):
        T[k]=i+1
        k+=1

    for i in range(1, (n+1)//2):
        T[k]=n//2+i+1
        k+=1

    tpsCompletDebut = time.time() # Début de la durée à mesurer

    a = ABR(T[1])
    for i in range(2, len(T)):
        time.sleep(0.1)
        InsererABR(a, T[i])
    
    tpsCompletFin = time.time() # Fin de la durée à mesurer
    
    return tpsCompletFin - tpsCompletDebut

def creer_ABR_filiforme(n):
    T=[]
    for i in range(0,n):
        T.append(i + 1)

    tpsFiliformeDebut = time.time() # Début de la durée à mesurer

    a = ABR(T[0])
    for i in range(1, len(T)):
        time.sleep(0.1)
        InsererABR(a, T[i])
    
    tpsFiliformeFin = time.time() # Fin de la durée à mesurer
    
    return tpsFiliformeFin - tpsFiliformeDebut

def Manipuler_ABR_complet(A: ABR, n: int) -> ABR:
    A_prime = A
    
    for i in range(2, n):
        val_a_suppr = (n + 1) // 2 ** i
        A_prime = SupprimerABR(A_prime, val_a_suppr)
        A_prime = InsererABR(A_prime, val_a_suppr)
    
    return A_prime

## TESTS DES FONCTIONS
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

n = 10 # Exemple avec n=10

tpsComplet = creer_ABR_complet(n)
print("Temps d'exécution ABR complet pour n = {}: ".format(n), tpsComplet)

tpsFiliforme = creer_ABR_filiforme(n)
print("Temps d'exécution ABR filiforme pour n = {}: ".format(n), tpsFiliforme)

A_complet = ABR() # On crée un arbre binaire de recherche complet
for i in range(1, n+1):
    InsererABR(A_complet, i)

A_filiforme = ABR() # On crée un arbre binaire de recherche filiforme
for i in range(1, n+1):
    InsererABR(A_filiforme, i)

tpsRecherche1_A = time.time()
RechercherABR(A_complet, 1)
tpsRecherche1_A_fin = time.time()
print("Temps de recherche de 1 dans A pour n = {}: ".format(n), tpsRecherche1_A_fin - tpsRecherche1_A)

tpsRecherche1_A_prime = time.time()
A_prime = Manipuler_ABR_complet(A_complet, n)
RechercherABR(A_prime, 1)
tpsRecherche1_A_prime_fin = time.time()
print("Temps de recherche de 1 dans A' pour n = {}: ".format(n), tpsRecherche1_A_prime_fin - tpsRecherche1_A_prime)

#On peut ensuite écrire les valeurs des temps d'exécution pour différentes valeurs de n dans un fichier CSV avec la fonction `csv.writer()` :

import csv

n_values = [10, 20, 50, 100, 200] # Exemples de valeurs de n
with open('temps_execution.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['n', 'temps_creer_ABR_complet', 'temps_creer_ABR_filiforme', 'temps_recherche_1_A', 'temps_recherche_1_A_prime'])
    for n in n_values:
        tpsComplet = creer_ABR_complet(n)
        tpsFiliforme = creer_ABR_filiforme(n)
        tpsRecherche1_A = time.time()
        RechercherABR(A_complet, 1)
        tpsRecherche1_A_fin = time.time()
        tpsRecherche1_A_prime = time.time()
        A_prime = Manipuler_ABR_complet(A_complet, n)
        RechercherABR(A_prime, 1)
        tpsRecherche1_A_prime_fin = time.time()
        row = [n, tpsComplet, tpsFiliforme, tpsRecherche1_A_fin - tpsRecherche1_A, tpsRecherche1_A_prime_fin - tpsRecherche1_A_prime]
        writer.writerow(row)