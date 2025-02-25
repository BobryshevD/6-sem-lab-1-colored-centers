import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as sp
import os

dirs = os.listdir(path='Спектры')

c = 3*10**8

T = []
frequence1 = []
frequence2 = []
width1 = []
width2 = []
frequence = []
width = []
sigma_width1 = []
sigma_width2 = []
sigma_width = []


for dir in dirs:
    if float(dir.replace('.csv', ''))+273 < 210:
        I = []
        lamd = []
        nu = []

        file = open('Спектры/' + dir)
        f = file.readlines()
        f.remove(f[0])
        f.remove(f[0])
        #print(f)
        for i in range(0, len(f)):
            f[i] = f[i].split()
            if (450 < (c/float(f[i][0])*10**9/10**12) < 550): #ограничение по частоте и по
                I.append(float(f[i][1]))
                lamd.append(float(f[i][0]))
                nu.append(c/float(f[i][0])*10**9/10**12) #частота в ТГц

        I_max = max(I)
        for i in range(len(I)):
            I[i] = I[i]/I_max

        # popt, pcov = sp.curve_fit(func, nu, I, method='dogbox', bounds=([-np.inf, 497, -np.inf, -np.inf, 497, -np.inf],
        #                                                             [np.inf, 500, np.inf, np.inf, 500, np.inf]), maxfev=100000
        #                         , p0 = [1, 498, 1, 1, 499, 1])
        # print(popt)
        # # #print(pcov)

        plt.plot(lamd, I)#, s=8, color='Black')
    #    plt.plot(nu, func(nu, *popt))
        plt.xlabel('Частота, ТГц')
        plt.ylabel('Интенсивность, отн. ед.')
        s = float(dir.replace('.csv', ''))+273
        plt.title(f'T = {s} К')
        plt.show()        

        file.close()

        # T.append(float(dir.replace('.csv', ''))+273)
        # frequence1.append(popt[1])
        # frequence2.append(popt[4])
        # width1.append(popt[2])
        # width2.append(popt[5])
        # sigma_width1.append(pcov[2][2]**(0.5))
        # sigma_width2.append(pcov[5][5]**(0.5))
