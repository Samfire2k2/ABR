##TP2 Conception et analyse d'algorithmes
#Tas binaires  - RAVARD Samuel
import time
import random

def Sift_Up(TB: list, i: int) -> None:
    fini = False
    while i != 1 and not fini:
        if TB[i] > TB[i // 2]:
            TB[i], TB[i // 2] = TB[i // 2], TB[i]
        else:
            fini = True
        i //= 2
        
def Sift_Down(TB: list, i: int, n: int) -> None:
    fini = False
    while 2*i <= n and not fini:
        i *= 2
        if i+1 <= n and TB[i+1] > TB[i]:
            i += 1

def Creer_TB(T):
    # implementation de l'algorithme Creer-TB
    n = len(T)
    TB = [[] for i in range(n)]
    for i in range(n):
        TB[i].append(T[i])
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            TB[i].append([k for k in range(i, j+1)])
            for p in range(i, j):
                QL = TB[i][p-i]
                QR = TB[p+1][j-p-1]
                if isinstance(QL, list) and isinstance(QR, list):
                    if len(QL) < len(QR):
                        TB[i][j-i] += QL
                    else:
                        TB[i][j-i] += QR
    return TB[0][-1]

def test_Creer_TB(T):
    # fonction pour mesurer le temps d'exécution de la fonction Creer_TB
    start_time = time.perf_counter()
    Creer_TB(T)
    end_time = time.perf_counter()
    return end_time - start_time

def generate_T_arrays(p, max_time=180):
    # fonction pour générer un grand échantillon de tableaux T aléatoires
    n = 2**p + 1 - 1
    T_arrays = []
    cumulated_time = 0
    while cumulated_time < max_time:
        T = [random.randint(1,n) for i in range(n)]
        T_arrays.append(T)
        cumulated_time += test_Creer_TB(T)
        recherche_pire_time = test_recherche_pire(Creer_TB(T))
        with open("temps_recherche_pire_TB.txt", "a+") as fp:
            fp.write("n = {} pire temps : {:.5f} s\n".format(n, recherche_pire_time))
    return T_arrays

def best_worst_times(T_arrays):
    # fonction pour calculer les temps les plus courts et les plus longs de Creer-TB
    best_time = float('inf')
    worst_time = 0
    for T in T_arrays:
        time = test_Creer_TB(T)
        best_time = min(best_time, time)
        worst_time = max(worst_time, time)
    return best_time, worst_time

def test_recherche_pire(TB):
    start_time = time.perf_counter()
    n = len(TB) - 1
    i = 1
    while i <= n:
        if TB[i] == 1:
            break
        i += 1
    end_time = time.perf_counter()
    return end_time - start_time

def main():
    # fonction principale pour générer les rapports de performance de Creer_TB
    with open("temps_CreerTB.txt", "w") as fp:
        for p in range(1,10):
            T_arrays = generate_T_arrays(p)
            best_time, worst_time = best_worst_times(T_arrays)
            fp.write("p = {}\n".format(p))
            fp.write("Temps au mieux : {:.5f} s\n".format(best_time))
            fp.write("Temps au pire : {:.5f} s\n".format(worst_time))
            fp.write("\n")

if __name__ == '__main__':
    main()
