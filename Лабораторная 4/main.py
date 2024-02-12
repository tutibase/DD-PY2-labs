import doctest


class TransportVehicle:
    """ Базовый класс транспорта. """
    def __init__(self, speed: float = 0, steering_angle: float = 0):
        """
        Создание и подготовка к работе объекта "Транспорт"

        :param speed: Скорость движения транспорта (отрицательная скорость = движение назад)
        :param steering_angle: Угол поворота руля транспорта

        Примеры:
        >>> transportVehicle = TransportVehicle(80, 0)  # инициализация экземпляра класса
        """
        if not isinstance(speed, (int, float)):
            raise TypeError("Скорость должна быть типа int или float")
        self._speed = speed

        if steering_angle > 360 or steering_angle < -360:
            raise ValueError("Угол поворота руля должен лежать в отрезке [-360; 360] градусов")

        if not isinstance(steering_angle, (int, float)):
            raise TypeError("Угол поворота руля должен быть типа int или float")
        self._steering_angle = steering_angle

    @property
    def speed(self) -> float:
        """
        Возвращает скорость ТС.

        :return: Скорость ТС

        Неизменяемый аттрибут, так как изменяется специальным методом
        (нельзя просто переставить скорость с одного значения на другое)

        Примеры:
        >>> transportVehicle = TransportVehicle(110, 7)
        >>> transportVehicle.speed
        110
        """
        return self._speed

    @property
    def steering_angle(self) -> float:
        """
        Возвращает угол поворота руля ТС.

        :return: Угол поворота руля ТС

        Неизменяемый аттрибут, так как изменяется специальным методом
        (нельзя просто переставить угол поворота с одного значения на другое)

        Примеры:
        >>> transportVehicle = TransportVehicle(110, 7)
        >>> transportVehicle.steering_angle
        7
        """
        return self._steering_angle

    def speed_change(self, change_value: float):
        """
        Изменение скорости движения ТС.
        :param change_value: Значение изменения скорости

        Примеры:
        >>> transportVehicle = TransportVehicle(110, 7)
        >>> transportVehicle.speed_change(3)
        """
        if not isinstance(change_value, (int, float)):
            raise TypeError("Изменение скорости должно быть типа int или float")
        self._speed += change_value

    def steering_angle_change(self, change_value: float):
        """
        Изменение скорости движения ТС.
        :param change_value: Значение изменения скорости

        Примеры:
        >>> transportVehicle = TransportVehicle(110, 7)
        >>> transportVehicle.steering_angle_change(3)
        """
        if not isinstance(change_value, (int, float)):
            raise TypeError("Изменение угла поворота руля должно быть типа int или float")
        self._steering_angle = (self.steering_angle + change_value) % 360

    def __str__(self):
        return f"Транспорт. Угол поворота руля {self.steering_angle}. Скорость движения {self.speed}"

    def __repr__(self):
        return f"{self.__class__.__name__}(steering_angle={self.steering_angle}, speed={self.speed})"


class Car(TransportVehicle):
    """Базовый класс машины."""
    def __init__(self, fuel_consumption: float, fuel_amount: float = 0,
                 speed: float = 0, steering_angle: float = 0):
        """
        Создание и подготовка к работе объекта "Машина"

        :param fuel_consumption: Расход топлива при движении (у каждой машины свой, теоретический параметр)
        :param fuel_amount: Количества топлива в машине
        :param speed: Скорость движения машины (отрицательная скорость = движение назад)
        :param steering_angle: Угол поворота руля машины

        Примеры:
        >>> car = Car(2, 50, 110, 7)  # инициализация экземпляра класса
        """
        super().__init__(speed, steering_angle)

        if fuel_consumption <= 0:
            raise ValueError("Расход топлива должен быть не меньше нуля.")
        if not isinstance(fuel_consumption, (int, float)):
            raise TypeError("Расход топлива должен быть типа int или float")
        self._fuel_consumption = fuel_consumption

        self.fuel_amount = fuel_amount

        # current_fuel_consumption: Расход топлива в настоящий момент (зависит от скорости)
        if speed != 0:
            self._current_fuel_consumption = fuel_consumption
        else:
            self._current_fuel_consumption = 0

    def speed_change(self, change_value: float):
        """
        Изменение скорости движения машины.
        :param change_value: Значение изменения скорости

        Метод перегружен, так как появился параметр расход топлива
        Примеры:
        >>> car = Car(2, 50, 110, 7)
        >>> car.speed_change(3)
        """
        if not isinstance(change_value, (int, float)):
            raise TypeError("Изменение скорости должно быть типа int или float")
        self._speed += change_value

        if self.speed == 0:
            self._current_fuel_consumption = 0
        else:
            self._current_fuel_consumption = self.fuel_consumption

    @property
    def current_fuel_consumption(self) -> float:
        """
        Возвращает текущий расход топлива машины.

        :return: Текущий расход топлива машины

        Неизменяемый аттрибут, так как должен изменяться только при изменении скорости
        (ненулевая скорость и нулевой расход приведут к ошибкам)

        Примеры:
        >>> car = Car(2, 50, 110, 7)
        >>> car.current_fuel_consumption
        2
        """
        return self._current_fuel_consumption

    @property
    def fuel_consumption(self) -> float:
        """
        Возвращает расход топлива машины при движении.

        :return: Расход топлива машины при движении

        Неизменяемый аттрибут, так как является характеристикой машины

        Примеры:
        >>> car = Car(2, 50, 110, 7)
        >>> car.fuel_consumption
        2
        """
        return self._fuel_consumption

    @property
    def fuel_amount(self):
        """
        Возвращает количество топлива в машине.

        :return: Количество топлива в машине

        Примеры:
        >>> car = Car(2, 50, 110, 7)
        >>> car.fuel_amount
        50
        """
        return self._fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_fuel_amount: float):
        """
        Устанавливает количество топлива в машине.

        Примеры:
        >>> car = Car(2, 50, 110, 7)
        >>> car.fuel_amount = 51
        """
        if new_fuel_amount < 0:
            raise ValueError("Количество топлива должно быть не меньше нуля.")
        if not isinstance(new_fuel_amount, (int, float)):
            raise TypeError("Количество топлива должно быть типа int или float")

        self._fuel_amount = new_fuel_amount

    def __str__(self):
        return f"Машина. Расход топлива в движении {self.fuel_consumption}. Количество топлива {self.fuel_amount}. " \
               f"Угол поворота руля {self.steering_angle}. Скорость движения {self.speed}"

    def __repr__(self):
        return f"{self.__class__.__name__}(fuel_consumption={self.fuel_consumption}, fuel_amount={self.fuel_amount}, " \
               f"steering_angle={self.steering_angle}, speed={self.speed})"


if __name__ == "__main__":
    doctest.testmod()
    pass
