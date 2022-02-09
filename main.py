#Loic Jolicoeur-Pomerleau, Nathaniel Létourneau

import numpy as np
import matplotlib.pyplot as plt
TABMAX=38167
ERRMAX=0.01
RUNTIME=93842428.589/2

def coincidence(array1, array2, coincidence):
    j = 0
    for i in range(0, TABMAX):
        pos = array1[i][1] + ERRMAX
        neg = array1[i][1] - ERRMAX
        if neg > array2[i-j][1] or array2[i-j][1] > pos:
            coincidence[i][2] = 0
            continue
        if array1[i][1] < array2[i - j][1]:
            j += 1

def noncoincidence(array1, array2, noncoincidence):
    j = 0
    for i in range(0, TABMAX):
        pos = array1[i][1] + ERRMAX
        neg = array1[i][1] - ERRMAX
        if neg < array2[i-j][1] and array2[i-j][1] < pos:
            noncoincidence[i][2] = 0
            continue
        if array1[i][1] < array2[i - j][1]:
            j += 1



def plot_loghist(x, bins, factor):
  hist, bins = np.histogram(x, bins=bins)
  logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
  plt.hist(x, bins=logbins, weights=factor*np.ones_like(x))
  plt.xscale('log')

def tauxmuons(x):
    t=RUNTIME/1000
    tm=0
    for i in range(TABMAX*2-1):
        tm+=x[i][3]/1000
    taux=((2*(TABMAX+1))/(t-tm))
    print(tm)
    print(taux)
    return taux

def main():
    f1 = open("S2GE_APP3_Problematique_Detecteur_Primaire.csv", "r")
    f2 = open("S2GE_APP3_Problematique_Detecteur_Secondaire.csv", "r")
    detect_prim = np.loadtxt(f1, dtype=None, delimiter=',', skiprows=1)
    detect_sec = np.loadtxt(f2, dtype=None, delimiter=',', skiprows=1)
    f1.close()
    f2.close()

    coincid = np.copy(detect_prim)
    coincidence(detect_prim, detect_sec, coincid)
    mVc = coincid[:, 2]

    noncoincid = np.copy(detect_prim)
    noncoincidence(detect_prim, detect_sec, noncoincid)
    mVn = noncoincid[:, 2]

    All = np.append(detect_prim, detect_sec, axis=0)

    plt.figure(num=1)
    plt.title("All")
    plot_loghist(All[:, 2], 10, tauxmuons(All))
    plt.show()





if __name__ == '__main__':
    main()

