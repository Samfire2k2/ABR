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
    n = len(T)
    TB = [[T[i]] for i in range(n)]
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            TB[i][j] = [k for k in range(i, j+1)]
            for p in range(i, j):
                QL = TB[i][p]
                QR = TB[p+1][j]
                if len(QL) < len(QR):
                    TB[i][j] = QL + QR
                else:
                    TB[i][j] = Q
