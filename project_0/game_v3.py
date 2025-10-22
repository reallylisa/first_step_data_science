def game_core_v3(number: int = 1) -> int:
    
    """Угадываем число от 1 до 100 бинарным поиском.
    На каждом шаге делим диапазон пополам и сужаем его.
        Функция принимает загаданное число и возвращает число попыток
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    left = 1 # левая граница диапазона
    right = 100 # правая граница диапазона
    
    while True:
        count += 1
        predict = (left + right) // 2 # середина текущего диапазона
        if number == predict:
            break # если угадали, выходим из цикла
        elif number > predict:
            left = predict + 1 # загаданное число больше — сдвигаем левую границу вправо
        else:
            right = predict - 1 # загаданное число меньше — сдвигаем правую границу влево
    
    return count

from game_v2 import score_game # импортируем функцию оценки

# Оцениваем эффективность алгоритма
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)