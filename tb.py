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
    while 2 * i <= n and not fini:
        j = 2 * i
        if j < n and TB[j+1] > TB[j]:
            j += 1
        if TB[j] > TB[i]:
            TB[i], TB[j] = TB[j], TB[i]
            i = j
        else:
            fini = True

def Creer_TB(T):
    n = len(T)
    TB = [0] + T.copy() # on commence à 1 au lieu de 0
    for i in range(n+1, n+11):
        TB.append(random.randint(1, n))
        Sift_Down(TB, i, n)
    return TB[1:]

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
    with open("temps_CreerTB.txt", "w") as fp:
        for p in range(1, 10):
            T_arrays = generate_T_arrays(p)
            best_time, worst_time = best_worst_times(T_arrays)
            pire_temps_recherche = 0
            while pire_temps_recherche < worst_time:
                T = random.choice(T_arrays)
                TB = Creer_TB(T)
                pire_temps_recherche = max(pire_temps_recherche, test_recherche_pire(TB))
            fp.write("n = {} p = {}\n".format(len(T), p))
            fp.write("Temps construction TB : {:.5f} s\n".format(test_Creer_TB(T)))
            fp.write("Temps recherche pire : {:.5f} s\n".format(pire_temps_recherche))
            fp.write("\n")

if __name__ == '__main__':
    main()