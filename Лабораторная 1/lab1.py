# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from datetime import datetime

class Tree:
    """Класс для описания дерева"""
    def __init__(self, height: float, tree_type: str = "unknown"):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param height: Высота дерева
        :param tree_type: Вид дерева

        Примеры:
        >>> tree = Tree(15, "oak")  # инициализация экземпляра класса
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        self.height = height

    def get_height(self) -> float:
        """
        Функция возвращает высоту дерева

        :return: Высота дерева

        Примеры:
        >>> tree = Tree(15, "oak")
        >>> tree.get_height()
        15
        """
        return self.height

    def is_cut_down(self) -> bool:
        """
        Функция которая проверяет является ли дерево срубленным

        :return: Является ли дерево срубленным

        Примеры:
        >>> tree = Tree(15, "oak")
        >>> tree.is_cut_down()
        False
        """
        return True if self.height == 0 else False

    def cut_down(self) -> None:
        """
        Срубание дерева.

         :raise ValueError: Если дерево высоты 0, то вызываем ошибку

        Примеры:
        >>> tree = Tree(15, "oak")
        >>> tree.cut_down()
        """
        if self.height == 0:
            raise ValueError("Дерево уже срублено")

        self.height = 0

class Flat:
    """Класс для описания кваритры"""

    def __init__(self, area: float, floor: int, tenants: int = 0):
        """
        Создание и подготовка к работе объекта "Квартира"

        :param area: Площадь квартиры
        :param floor: Этаж, на котором находится квартира
        :param tenants: Количество жильцов квартиры

        Примеры:
        >>> flat = Flat(110, 7)  # инициализация экземпляра класса
        """
        if not isinstance(area, (int, float)):
            raise TypeError("Площадь квартиры должна быть типа int или float")
        if area <= 0:
            raise ValueError("Площадь квартиры должна быть положительным числом")
        self.area = area

        if not isinstance(floor, int):
            raise TypeError("Этаж должен быть типа int")
        if floor < 1:
            raise ValueError("Этаж не может быть меньше первого")
        self.floor = floor

        if not isinstance(tenants, int):
            raise TypeError("Количество жильцов должно быть типа int")
        self.tenants = tenants

    def is_flat_occupied(self) -> bool:
        """
        Функция которая проверяет является ли квартира заселенной

        :return: Является ли квартира заселенной

        Примеры:
        >>> flat = Flat(110, 7)
        >>> flat.is_flat_occupied()
        False
        """
        return True if self.tenants > 0 else False

    def add_tenants(self, tenants_count: int) -> None:
        """
        Добавление жильцов в квартиру.
        :param tenants_count: Количество добавляемых жильцов

        Примеры:
        >>> flat = Flat(110, 7)
        >>> flat.add_tenants(3)
        """
        if not isinstance(tenants_count, int):
            raise TypeError("Количество жильцов должно быть типа int")

        self.tenants += tenants_count


class Smartphone:
    """Класс для описания смартфона"""

    def __init__(self, model: str, year: int):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param model: Модель смартфона
        :param year: Год выпуска смартфона

        Примеры:
        >>> smartphone = Smartphone("IPhone 13", 2021)  # инициализация экземпляра класса
        """

        if not isinstance(year, int):
            raise TypeError("Год выпуска должен быть типа int")
        if year > datetime.now().year:
            raise ValueError("Год выпуска не может быть больше текущего года")
        self.year = year

        self.model = model

    def get_year(self) -> int:
        """
        Функция возвращает год выпуска смартфона

        :return: Год выпуска смартфона

        Примеры:
        >>> smartphone = Smartphone("IPhone 13", 2021)
        >>> smartphone.get_year()
        2021
        """
        return self.year

    def is_released_this_year(self) -> bool:
        """
        Функция, которая проверяет, в этом ли году выпустили смартфон

        :return: Выпущен ли смартфон в этом году

        Примеры:
        >>> smartphone = Smartphone("IPhone 13", 2021)
        >>> smartphone.is_released_this_year()
        False
        """
        return True if self.year == datetime.now().year else False


if __name__ == "__main__":
    doctest.testmod()  # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
