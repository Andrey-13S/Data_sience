"Игра *угадай число*"
"PC загадывает и угадывает число"

import numpy as np
import random

def game_core_v3(number: int = 1) -> int:
    # переменная - кол-во попыток поиска
    count = 0
    # значение, начало поиска
    start = 1 
    # значение, конец поиска +1
    stop = 101  

    while True:
        # вычислим середину заданного диапазона поиска
        average_number = (start + stop)//2
        # при очередном использовании вычисления average_number увеличиваем count на +1
        count += 1
        if average_number == number:
            # окончание работы цикла, если число угадано
            break 
        # если блок if не выполнен, присваиваем началу диапазона поиска значение number (уменьшаем область поиска)
        elif number > average_number:
            start = average_number 
        # если блок elif не выполнен, присваиваем концу диапазона поиска значение average_number (уменьшаем область поиска)
        else:
            stop = average_number
    # возвращаем значение кол-ва попыток поиска
    return count

def score_game(game_core_v3) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] #список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))
    score = int(np.mean(count_ls))

    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")

    return score

if __name__ == "__main__":
    #RUN
    score_game(game_core_v3)