import doctest
import numpy as np


class Array:

    def __init__(self, size, num=0):
        """
        Создание и подготовка к работе объекта "Массив".
        """

        self.size = None
        self.num = None
        self.create_attr(size, num)

    def create_attr(self, size, num):
        """
        Создание атрибутов экземпляра класса "Массив".

        :param size: размерность массива
        :param num: число, которым нужно заполнить массив

        Примеры:
        >>> arr_a = Array(5) # инициализация экземпляра класса
        >>> arr_b = Array((2, 5), 2) # инициализация экземпляра класса
        >>> arr_c = Array('3') # инициализация экземпляра класса
        Traceback (most recent call last):
        ...
        TypeError: Размерность должна быть целым числом, списком или кортежем.
        >>> arr_d = Array(-6) # инициализация экземпляра класса
        Traceback (most recent call last):
        ...
        ValueError: Размерность не может быть отрицательной.
        """

        if not isinstance(size, (int, tuple, list)):
            raise TypeError('Размерность должна быть целым числом, списком или кортежем.')
        if isinstance(size, (tuple, list)):
            if not any(isinstance(x, int) for x in size):
                raise TypeError('В качесвте размерности могут быть указаны только целые числа.')
            if any(x < 0 for x in size):
                raise ValueError('Все числа размерности должны быть положительными.')
        else:
            if size < 0:
                raise ValueError('Размерность не может быть отрицательной.')

        self.size = size

        if not isinstance(num, int):
            raise TypeError('Задан неверный тип данных для числа.')
        if num < 0:
            raise ValueError('Число должно быть положительным')
        self.num = num

    def __str__(self):
        return (f'Класс для создания numpy массива. Размерность массива = {self.size}. Число {self.num} '
                f'нужно для метода fill_other.')

    def __repr__(self):
        return f'{self.__class__.__name__}({self.size}, {self.num})'

    def fill_zeroes(self):
        """
        Метод для создания numpy массива из нулей заданного размера.

        :return: Массив из нулей.
        """

        return np.zeros(self.size, dtype=int)

    def fill_ones(self):
        """
        Метод для создания numpy массива из единиц заданного размера.

        :return: Массив из единиц.
        """

        return np.ones(self.size, dtype=int)

    def fill_other(self):
        """
        Метод для создания numpy массива определенного размера(size) заданным числом(num).

        :return: Массив из заданного числа.
        """

        return np.full(self.size, self.num, dtype=int)


doctest.testmod()  # тестирование примеров, которые находятся в документации
