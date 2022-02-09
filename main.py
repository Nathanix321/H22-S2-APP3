#Loic Jolicoeur-Pomerleau, Nathaniel Létourneau

import numpy as np
import matplotlib.pyplot as plt
TABMAX=38167
ERRMAX=0.01

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



def plot_loghist(x, bins):
  hist, bins = np.histogram(x, bins=bins)
  logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
  plt.hist(x, bins=logbins)
  plt.xscale('log')

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




if __name__ == '__main__':
    main()

