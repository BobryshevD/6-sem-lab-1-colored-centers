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


def func(x, Г_1, nu_01, h_01, Г_2, nu_02, h_02):
    return Г_1/((x-nu_01)**2 + h_01**2) + Г_2/((x-nu_02)**2 + h_02**2)


for dir in dirs:
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
        if 497 < (c/float(f[i][0])*10**9/10**12) < 502: #ограничение по частоте
            I.append(float(f[i][1]))
            lamd.append(float(f[i][0]))
            nu.append(c/float(f[i][0])*10**9/10**12) #частота в ТГц

    I_max = max(I)
    for i in range(len(I)):
        I[i] = I[i]/I_max

    popt, pcov = sp.curve_fit(func, nu, I, method='dogbox', bounds=([-np.inf, -np.inf, -np.inf, -np.inf, -np.inf, -np.inf],
                                                                 [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf]), maxfev=100000
                              , p0 = [1, 498, 1, 1, 499, 1])
    # print(popt)
    # # #print(pcov)

    # plt.scatter(nu, I, s=8, color='Black')
    # plt.plot(nu, func(nu, *popt))
    # plt.xlabel('Частота, ГГц')
    # plt.ylabel('Интенсивность, отн. ед.')
    # plt.show()        

    file.close()

    T.append(float(dir.replace('.csv', ''))+273)
    frequence1.append(popt[1])
    frequence2.append(popt[4])
    width1.append(popt[2])
    width2.append(popt[5])
    
frequence_left = []
frequence_right = []
width_left = []
width_right = []

for i in range(len(frequence1)):
    if (frequence1[i] < frequence2[i]):
        frequence_left.append(frequence1[i])
        width_left.append(width1[i])
        frequence_right.append(frequence2[i])
        width_right.append(width2[i])
    else:
        frequence_left.append(frequence2[i])
        width_left.append(width2[i])
        frequence_right.append(frequence1[i])
        width_right.append(width1[i])


# width_right_2 = []
# for i in range(len(width_right)):
#     width_right_2.append(width_right[i]**(1/3))
#plt.scatter(T, width_right)

plt.scatter(T, width_right)
plt.scatter(T, width_left)

plt.show()

