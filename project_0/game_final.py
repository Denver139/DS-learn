"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
import numpy as np


def random_predict(number:int = 1) -> int:
    
    """Рандомно угадываем число
    Args:
        number (int, optional): Загаданное число
    Returns:
        int: Число попыток
    """
    
    number = np.random.randint(1, 101) #Компьютер загадывает рандомное число
    count = 0
    mn, mx = 1, 100 #Диапазон загаданного числа 
    
    while True:
        count += 1 
        predict_number = (mn + mx)//2 #Предполагаемое число
        if predict_number > number:
            mx = predict_number - 1
        elif predict_number < number:
            mn = predict_number + 1
        elif number == predict_number:
            break #выход из цикла, когда угадали 
    return(count)

    
def score_game(random_predict) -> int:
    
    """За какое количство попыток в среднем за 1000 подходов угадываем
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадываем

    for number in random_array:
        count_ls.append(random_predict())

    score = int(np.mean(count_ls))
    print(f"Этот алгоритм угадывает число в среднем за:{score} попыток")
    return score

if __name__ == "__main__":
    # RUN
    score_game(random_predict)

