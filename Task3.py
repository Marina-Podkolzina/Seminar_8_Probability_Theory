#3) Известно, что рост футболистов в сборной распределен нормально 
#с дисперсией генеральной совокупности, равной 25 кв.см. Объем выборки равен 27, 
#среднее выборочное составляет 174.2. 
#Найдите доверительный интервал для математического ожидания с надежностью 0.95.

#Решение: Нам известнa дисперсия генеральной совокупности,значит 
#для расчета 95%-го доверительного интервала, будем использовать z-критерий

import numpy as np
import scipy.stats as stats

x_mean = 174.2 #  среднее арифметическое 
x_std = np.sqrt(25) # дисперсия ген. совокупности
x_mean_std = x_std / np.sqrt(27) # находим стандартную ошибку среднего
print(f"Стандартная ошибка среднего - {x_mean_std}")
print('_')
z= stats.norm.ppf(0.975)# Находим табличное значение z критерия для 95% интервала 
print(f"Табличное значение z критерия для 95% интервала - {z}")
print('_')

x_mean - z * x_mean_std 
x_mean + z * x_mean_std
print("Доверительный интервал для мат. ожидания с надежностью 0.95% ")
print(x_mean - z * x_mean_std, x_mean + z * x_mean_std) 
print('_')
