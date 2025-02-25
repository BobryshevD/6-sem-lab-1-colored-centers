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




def func(x, Г_1, nu_01, h_01, Г_2, nu_02, h_02):
    return Г_1/((x-nu_01)**2 + h_01**2) + Г_2/((x-nu_02)**2 + h_02**2)  #2 лоренциана


def func1(x, Г_1, nu_01, h_01):
    return Г_1/((x-nu_01)**2 + h_01**2)  #1 лоренциан

def func2(x, a, b):
    return a*x**3 + b

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
            if (497.3 < (c/float(f[i][0])*10**9/10**12) < 499.8): #ограничение по частоте и по
                I.append(float(f[i][1]))
                lamd.append(float(f[i][0]))
                nu.append(c/float(f[i][0])*10**9/10**12) #частота в ТГц

        I_max = max(I)
        for i in range(len(I)):
            I[i] = I[i]/I_max

        popt, pcov = sp.curve_fit(func, nu, I, method='dogbox', bounds=([-np.inf, 497, -np.inf, -np.inf, 497, -np.inf],
                                                                    [np.inf, 500, np.inf, np.inf, 500, np.inf]), maxfev=100000
                                , p0 = [1, 498, 1, 1, 499, 1])
        print(popt)
        # # #print(pcov)

        plt.scatter(nu, I, s=8, color='Black')
        plt.plot(nu, func(nu, *popt))
        plt.xlabel('Частота, ТГц')
        plt.ylabel('Интенсивность, отн. ед.')
        s = float(dir.replace('.csv', ''))+273
        plt.title(f'T = {s} К')
        plt.show()        

        file.close()

        T.append(float(dir.replace('.csv', ''))+273)
        frequence1.append(popt[1])
        frequence2.append(popt[4])
        width1.append(popt[2])
        width2.append(popt[5])
        sigma_width1.append(pcov[2][2]**(0.5))
        sigma_width2.append(pcov[5][5]**(0.5))
    
for dir in dirs:
    if float(dir.replace('.csv', ''))+273 >= 240:
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
            if (496.2 < (c/float(f[i][0])*10**9/10**12) < 500): #ограничение по частоте и по
                I.append(float(f[i][1]))
                lamd.append(float(f[i][0]))
                nu.append(c/float(f[i][0])*10**9/10**12) #частота в ТГц

        I_max = max(I)
        for i in range(len(I)):
            I[i] = I[i]/I_max

        popt, pcov = sp.curve_fit(func1, nu, I, method = 'trf', p0 = [1, 499, 1])
        print(popt)
        # # #print(pcov)

        plt.scatter(nu, I, s=8, color='Black')
        plt.plot(nu, func1(nu, *popt))
        plt.xlabel('Частота, ТГц')
        plt.ylabel('Интенсивность, отн. ед.')
        s = float(dir.replace('.csv', ''))+273
        plt.title(f'T = {s} К')
        plt.show()        

        file.close()

        T.append(float(dir.replace('.csv', ''))+273)
        frequence.append(popt[1])
        width.append(popt[2])
        sigma_width.append(pcov[2][2]**(0.5))
        
    
        
        

frequence_left = []
frequence_right = []
width_left = []
width_right = []
wavelenght_left = []
wavelenght_right = []
sigma_width_left = []
sigma_width_right = []


for i in range(len(frequence1)):
    if (frequence1[i] < frequence2[i]):
        frequence_left.append(frequence1[i])
        wavelenght_left.append(c/frequence1[i]/10**(12)*10**9)
        width_left.append(width1[i])
        sigma_width_left.append(sigma_width1[i])
        frequence_right.append(frequence2[i])
        width_right.append(width2[i])
        wavelenght_right.append(c/frequence2[i]/10**(12)*10**9)
        sigma_width_right.append(sigma_width2[i])
    else:
        wavelenght_left.append(c/frequence2[i]/10**(12)*10**9)
        frequence_left.append(frequence2[i])
        width_left.append(width2[i])
        sigma_width_left.append(sigma_width2[i])
        frequence_right.append(frequence1[i])
        width_right.append(width1[i])
        wavelenght_right.append(c/frequence1[i]/10**(12)*10**9)
        sigma_width_right.append(sigma_width1[i])


for i in range(len(frequence)):
    frequence_left.append(frequence[i])
    frequence_right.append(frequence[i])
    width_left.append(width[i])
    width_right.append(width[i])
    sigma_width_right.append(sigma_width[i])
    sigma_width_left.append(sigma_width[i])
    

# width_right_2 = []
# for i in range(len(width_right)):
#     width_right_2.append(width_right[i]**(1/3))
#plt.scatter(T, width_right)

delta_frequence = []
for i in range(len(frequence_left)):
    delta_frequence.append(frequence_right[i]-frequence_left[i])


x = np.linspace(0, 300, 10000)

p, v = sp.curve_fit(func2, T, width_left)

print(sigma_width_left)
#print(T, width_right)
print(p[0], v[0][0]**(0.5))
#plt.scatter(T, width_right)
plt.errorbar(T, width_left, sigma_width_left, linestyle=' ',color = 'Black')
plt.scatter(T, width_left, color = 'Black', s = 7)
plt.plot(x, func2(x, *p), color='Green')
plt.xlabel('T, К')
plt.ylabel('Ширина пика, ТГц')

plt.show()

