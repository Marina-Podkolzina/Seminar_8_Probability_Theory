#2) Измерены значения IQ выборки студентов,
#обучающихся в местных технических вузах:
#131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
#Известно, что в генеральной совокупности IQ распределен нормально.
#Найдите доверительный интервал для математического ожидания с надежностью 0.95.


#Решение: Из условия задачи нам ничего неизвестно 
#ни о мат. ожидании генеральной совокупности, 
#ни о среднем квадратическом отклонении, то для расчета 
#95%-го доверительного интервала будем использовать t-критерий:


import numpy as np
import scipy.stats as stats



a = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
len(a)
10
x_mean = np.mean(a) # Находим среднее арифметическое 
print(f"Cреднее арифметическое: {np.mean(a)}")
print('_')

x_std = np.std(a, ddof = 1) # Находим стандартное отклонение 
print(f"Cтандартное отклонение:  {x_std}")
print('_')

x_mean_std = x_std / (np.sqrt(len(a))) # Находим стандартную ошибку среднего 
print(f"Cтандартная ошибка среднего:  {x_mean_std }")
print('_')

t=stats.t.ppf(0.975, 9)# Находим табличное значение t критерия для 95% интервала
print(f"Табличное значение t критерия:  {t}")
print('_')

x_mean - t * x_mean_std 
x_mean + t * x_mean_std
print("Доверительный интервал для мат. ожидания с надежностью 0.95")
print(x_mean - t * x_mean_std, x_mean + t * x_mean_std  ) 
print('_')


