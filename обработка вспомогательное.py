import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

# Создаем данные для графика
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Создаем основной график
fig, ax = plt.subplots()
ax.plot(x, y)

# Создаем увеличенную часть графика
ax_inset = inset_axes(ax, width="30%", height="30%", loc='upper right')  # Размеры и расположение
ax_inset.plot(x, y)
ax_inset.set_xlim(2, 4)  # Устанавливаем пределы по оси X для увеличенной части
ax_inset.set_ylim(-1, 1)  # Устанавливаем пределы по оси Y для увеличенной части

# Добавляем рамку вокруг увеличенной части
mark_inset(ax, ax_inset, loc1=2, loc2=4, fc="none", ec="black")

# Показываем график
plt.show()