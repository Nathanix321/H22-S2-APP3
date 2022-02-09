#Loic Jolicoeur-Pomerleau, Nathaniel Létourneau

import numpy as np
import matplotlib.pyplot as plt

def main():
    f1 = open("S2GE_APP3_Problematique_Detecteur_Primaire.csv", "r")
    f2 = open("S2GE_APP3_Problematique_Detecteur_Secondaire.csv", "r")
    detect_prim = np.loadtxt(f1, dtype=None, delimiter=',', skiprows=1)
    detect_sec = np.loadtxt(f2, dtype=None, delimiter=',', skiprows=1)
    print(detect_prim[:,2])

    plt.figure(num=1)
    plt.title("Primaire")
    plt.plot(detect_prim[:, 1], detect_prim[:, 2])
    plt.xlabel("Temps (ms)")
    plt.ylabel("Voltage (meV)")

    plt.figure(num=2)
    plt.title("Secondaire")
    plt.plot(detect_sec[:, 1], detect_sec[:, 2])
    plt.xlabel("Temps (ms)")
    plt.ylabel("Voltage (meV)")

    coincid = np.copy(detect_prim)
    for i in range(0, 38167):
        coincid[i][2]=0
    for i in range(0, 38167):
        pos=detect_prim[i][2]+0.1*detect_prim[i][2]
        neg=detect_prim[i][2]-0.1*detect_prim[i][2]
        for j in range(-5, 5):
            index=i+j
            index=np.clip(index, 0, 38166)
            if neg<detect_sec[index][2] and detect_sec[index][2]<pos:
                coincid[i][2]=detect_prim[i][2]

    plt.figure(num=3)
    plt.title("Plot coincidence")
    plt.plot(coincid[:, 1], coincid[:, 2])
    plt.xlabel("Temps (ms)")
    plt.ylabel("Voltage (meV)")

    print(detect_prim[0][2])
    plt.show()
    f1.close()
    f2.close()
if __name__ == '__main__':
    main()

