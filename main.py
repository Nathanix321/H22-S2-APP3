#Loic Jolicoeur-Pomerleau, Nathaniel Létourneau

import numpy as np
import matplotlib.pyplot as plt
TABMAX = 38167
ERRMAX = 0.01
RUNTIME = 93842428.589/2

def coincidence(array1, array2, coincidence, noncoincidence):
    j = 0
    i = 0
    while i < TABMAX:
        diff = array1[i][1]-array2[j][1]
        if abs(diff) < 0.01:
            coincidence.append(array1[i][2])
            noncoincidence[i][2] = 0
            j += 1
        if diff < 0:
            i += 1
            continue
        if diff>0:
            j += 1
            i -= 1
        i += 1

def plot_loghist(x, bins, factor, histtype, colors, label):

  hist, bins = np.histogram(x, bins=bins)
  logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
  plt.hist(x, bins=logbins, weights=factor*np.ones_like(x), histtype=histtype, edgecolor=colors, stacked=True, fill=False, label=label)
  plt.xscale('log')

def tauxmuons(x):
    t = RUNTIME/1000
    tm = 0
    for i in range(TABMAX-1):
        tm += x[i][3]/1000
    taux = 1/(t-tm)
    return taux

def main():
    f1 = open("S2GE_APP3_Problematique_Detecteur_Primaire.csv", "r")
    f2 = open("S2GE_APP3_Problematique_Detecteur_Secondaire.csv", "r")
    detect_prim = np.loadtxt(f1, dtype=None, delimiter=',', skiprows=1)
    detect_sec = np.loadtxt(f2, dtype=None, delimiter=',', skiprows=1)
    f1.close()
    f2.close()

    mVc = []
    mVn = np.copy(detect_prim)
    coincidence(detect_prim, detect_sec, mVc, mVn)
    mVc = np.array(mVc)
    mVn = mVn[:, 2]

    n_bin=25
    plt.figure(num=1)
    plt.title("Histogramme des distributions d'analyse de détection de muons")
    plot_loghist(detect_prim[:, 2], n_bin, 1/(RUNTIME/1000), 'step', 'grey', "Tous les évènements")
    plot_loghist(mVc, n_bin, 1/(RUNTIME/1000), 'step', 'red', "Évènements coincidents")
    plot_loghist(mVn[mVn != 0], n_bin, 1/(RUNTIME/1000), 'step', 'lime', "Évènments non-coincidents")
    plt.xlabel("Voltage PMSi calculé [mV]")
    plt.ylabel("Taux/classe [$s^-1$]")
    plt.legend(loc="upper right")
    plt.savefig("letn1102-joll1702(non-corrigé)")

    plt.figure(num=2)
    plt.title("Histogramme des distributions d'analyse de détection de muons (corrigé pour temps mort)")
    plot_loghist(detect_prim[:, 2], n_bin, tauxmuons(detect_prim), 'step', 'grey', "Tous les évènements")
    plot_loghist(mVc, n_bin, tauxmuons(detect_prim), 'step', 'red', "Évènements coincidents")
    plot_loghist(mVn[mVn != 0], n_bin, tauxmuons(detect_prim), 'step', 'lime', "Évènments non-coincidents")
    plt.xlabel("Voltage PMSi calculé [mV]")
    plt.ylabel("Taux/classe [$s^-1$]")
    plt.legend(loc="upper right")
    plt.savefig("letn1102-joll1702(corrigé)")
    plt.show()





if __name__ == '__main__':
    main()

