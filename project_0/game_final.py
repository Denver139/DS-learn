"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
import numpy as np

def random_predict(number:int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict_number = np.random.randint(1, 101) #Предполагаемое число

    while True:
        count += 1 
        if predict_number > number:
            predict_number = predict_number // 2
        elif predict_number < number:
            predict_number = predict_number + (100 - predict_number) // 2 
        elif number == predict_number:
            break #выход из цикла, если угадали 
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


