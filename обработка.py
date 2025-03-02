import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as sp
import os
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset


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
sigma_frequence1 = []
sigma_frequence2 = []
sigma_frequence = []


def func(x, Г_1, nu_01, h_01, Г_2, nu_02, h_02):
    return Г_1/((x-nu_01)**2 + h_01**2) + Г_2/((x-nu_02)**2 + h_02**2)  #2 лоренциана


def func1(x, Г_1, nu_01, h_01):
    return Г_1/((x-nu_01)**2 + h_01**2)  #1 лоренциан

def func2(x, a, b): #кубическая зависимость
    return a*x**3 + b

def func3(x, a, b): #квадратичная зависимость
    return a*x**2 + b

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

        # plt.scatter(nu, I, s=8, color='Black')
        # plt.plot(nu, func(nu, *popt))
        # plt.xlabel('Частота, ТГц')
        # plt.ylabel('Интенсивность, отн. ед.')
        # s = float(dir.replace('.csv', ''))+273
        # plt.title(f'T = {s} К')
        # plt.show()        

        file.close()

        T.append(float(dir.replace('.csv', ''))+273)
        frequence1.append(popt[1])
        frequence2.append(popt[4])
        width1.append(popt[2])
        width2.append(popt[5])
        sigma_width1.append(pcov[2][2]**(0.5))
        sigma_width2.append(pcov[5][5]**(0.5))
        sigma_frequence1.append(pcov[1][1]**(0.5))
        sigma_frequence2.append(pcov[5][5]**(0.5))
    
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

        # plt.scatter(nu, I, s=8, color='Black')
        # plt.plot(nu, func1(nu, *popt))
        # plt.xlabel('Частота, ТГц')
        # plt.ylabel('Интенсивность, отн. ед.')
        # s = float(dir.replace('.csv', ''))+273
        # plt.title(f'T = {s} К')
        # plt.show()        

        file.close()

        T.append(float(dir.replace('.csv', ''))+273)
        frequence.append(popt[1])
        width.append(popt[2])
        sigma_width.append(pcov[2][2]**(0.5))
        sigma_frequence.append(pcov[1][1]**(0.5))
    
        
        

frequence_left = []
frequence_right = []
width_left = []
width_right = []
wavelenght_left = []
wavelenght_right = []
sigma_width_left = []
sigma_width_right = []
sigma_frequence_left = []
sigma_frequence_right = []


for i in range(len(frequence1)):
    if (frequence1[i] < frequence2[i]):
        frequence_left.append(frequence1[i])
        wavelenght_left.append(c/frequence1[i]/10**(12)*10**9)
        width_left.append(width1[i])
        sigma_width_left.append(sigma_width1[i])
        sigma_frequence_left.append(sigma_frequence1[i])
        frequence_right.append(frequence2[i])
        width_right.append(width2[i])
        wavelenght_right.append(c/frequence2[i]/10**(12)*10**9)
        sigma_width_right.append(sigma_width2[i])
        sigma_frequence_right.append(sigma_frequence2[i])
    else:
        wavelenght_left.append(c/frequence2[i]/10**(12)*10**9)
        frequence_left.append(frequence2[i])
        width_left.append(width2[i])
        sigma_width_left.append(sigma_width2[i])
        sigma_frequence_left.append(sigma_frequence2[i])
        frequence_right.append(frequence1[i])
        width_right.append(width1[i])
        wavelenght_right.append(c/frequence1[i]/10**(12)*10**9)
        sigma_width_right.append(sigma_width1[i])
        sigma_frequence_right.append(sigma_frequence1[i])


for i in range(len(frequence)):
    frequence_left.append(frequence[i])
    frequence_right.append(frequence[i])
    wavelenght_left.append(c/frequence[i]/10**(12)*10**9)
    wavelenght_right.append(c/frequence[i]/10**(12)*10**9)
    width_left.append(width[i])
    width_right.append(width[i])
    sigma_width_right.append(sigma_width[i])
    sigma_width_left.append(sigma_width[i])
    sigma_frequence_right.append(sigma_frequence[i])
    sigma_frequence_left.append(sigma_frequence[i])
    

# width_right_2 = []
# for i in range(len(width_right)):
#     width_right_2.append(width_right[i]**(1/3))
#plt.scatter(T, width_right)

delta_frequence = []
T_for_delta = []
sigma_delta_frequence = []

for i in range(len(T)):
    if T[i] < 210:
        delta_frequence.append(frequence_right[i] - frequence_left[i])
        T_for_delta.append(T[i])
        sigma_delta_frequence.append(np.sqrt(sigma_frequence_left[i]**2 + sigma_frequence_right[i]**2))


mean_wavelenght = []
sigma_mean_wavelenght = []
for i in range(len(wavelenght_right)):
    mean_wavelenght.append((wavelenght_right[i] + wavelenght_left[i])/2)
#    sigma_mean_wavelenght.append((sigma_frequence_right[i] + sigma_frequence_left[i])*mean_wavelenght[i]**2/c/10**9*10**15/2)

x = np.linspace(0, 300, 10000)

p, v = sp.curve_fit(func2, T, mean_wavelenght)

print(p)
print(mean_wavelenght)
print(sigma_frequence_left, sigma_mean_wavelenght)

#print(sigma_width_left)
#print(T, width_right)
#print(p[0], v[0][0]**(0.5), p[1], v[1][1]**0.5)
#plt.scatter(T, width_right)
#plt.errorbar(T, width_left, sigma_width_left, xerr=1, linestyle=' ',color = 'Black')

fig, ax = plt.subplots()

ax.scatter(T, mean_wavelenght, color = 'Black', s = 7)
ax.plot(x, func2(x, *p), color='Green')
#plt.errorbar(T, mean_wavelenght, sigma_mean_wavelenght, xerr=1, linestyle=' ',color = 'Black')


plt.xlabel('T, К')
plt.ylabel('Средняя длина волны пика, нм')



# ax_inset = inset_axes(ax, width="30%", height="30%", loc='lower left', borderpad = 3)  # Размеры и расположение
# ax_inset.scatter(T_for_delta, delta_frequence, color = 'Black', s = 7)
# ax_inset.plot(x, func3(x, *p), color='Green')
# ax_inset.set_xlim(130, 215)  # Устанавливаем пределы по оси X для увеличенной части
# ax_inset.set_ylim(0.74, 1.1)  # Устанавливаем пределы по оси Y для увеличенной части
# ax_inset.set_xlabel('a')

# mark_inset(ax, ax_inset, loc1=2, loc2=4, fc="none", ec="black", linestyle = '--')


plt.show()

