import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp

chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(...) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы

    data = pd.read_csv("/hyp3_historical_data.csv")
    
    d = data.iloc[0].to_list()

    threshold = 300

    alpha = 0.1

    t_statistic, p_value = ttest_1samp(data, threshold)

    if p_value < alpha:
        result = True  
    else:
        result = False  

    return result # Ваш ответ, True или False
