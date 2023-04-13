import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp

chat_id = 33217853 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы

    threshold = 300

    alpha = 0.1

    t_statistic, p_value = ttest_1samp(x, threshold)

    if p_value < alpha:
        result = True  
    else:
        result = False  

    return result # Ваш ответ, True или False
