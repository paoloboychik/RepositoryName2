import doctest


class Superhero:
    def __init__(self, power: int, intelligence: int):
        """
        Создание и подготовка к работе объекта "Супергерой"

        :param power: Сила супергероя (в очках 0-500)
        :param intelligence: Интеллект супергероя (в очках 0-500)

        Примеры:
        >>> superhero = Superhero(499, 1) # инициализация экземпляра класса
        """
        if not isinstance(power, int):
            raise TypeError("Очки силы должны быть типа int")
        if power < 0 or power > 500:
            raise ValueError("Очки силы должны лежать в пределах от 0 до 500")
        self.power = power

        if not isinstance(intelligence, int):
            raise TypeError("Очки интеллекта должны быть типа int")
        if intelligence < 0 or intelligence > 500:
            raise ValueError("Очки интеллекта должны лежать в пределах от 0 до 500")
        self.intelligence = intelligence

    def save_people(self) -> None:
        """
        Функция, добавляющая в послужной список героя ещё одного спасённого человека

        Примеры:
        >>> superhero = Superhero(499, 1)
        >>> superhero.save_people()
        """
        ...

    def kill_people(self) -> None:
        """
        Функция, добавляющая в послужной список героя ещё одного случайно убитого человека

        Примеры:
        >>> superhero = Superhero(499, 1)
        >>> superhero.kill_people()
        """
        ...

    def wear_tights(self) -> None:
        """
        Функция, облачающая супергероя в узнаваемое обтягивающее трико

        Примеры:
        >>> superhero = Superhero(499, 1)
        >>> superhero.wear_tights()
        """
        ...


class President:
    def __init__(self, age: int, another_country_citizenship: bool):
        """
         Создание и подготовка к работе объекта "Президент"

         :param age: Возраст президента (от 35 лет)
         :param another_country_citizenship: Наличие гражданства другой страны
         :raise TypeError: Гражданство другой страны либо есть, либо отсутствует
         :raise ValueError: У президента не должно быть иностранного гражданства

         Примеры:
         >>> president = President(39, False) # инициализация экземпляра класса
         """
        if not isinstance(age, int):
            raise TypeError("Президент должен иметь возраст типа int")
        if age < 35:
            raise ValueError("Президентом не может стать гражданин моложе 35 лет")
        self.age = age

        if not isinstance(another_country_citizenship, bool):
            raise TypeError("Наличие иностранного гражданства должно быть типа bool")
        if another_country_citizenship is True:
            raise ValueError("Наличие иностранного гражданства должно иметь значение False")
        self.another_country_citizenship = another_country_citizenship

    def new_years_address(self) -> None:
        """
        Президент выступает с новогодним обращением

        Примеры:
        >>> president = President(39, False)
        >>> president.new_years_address()
        """
        ...

    def sign_decree(self) -> None:
        """
        Президент подписывает указ

        Примеры:
        >>> president = President(39, False)
        >>> president.sign_decree()
        """
        ...

    def read_from_prompter(self) -> None:
        """
        Президент читает с суфлёра

        Примеры:
        >>> president = President(39, False)
        >>> president.read_from_prompter()
        """
        ...


class Shaverma:
    def __init__(self, name: str, hours_of_existence: int):
        """
        Создание и подготовка к работе объекта "Шаверма"

        :param name: Наименования шавермы
        :raise ValueError: Если шаверма лежит более 48 часов, то она испорчена; также шаверма
            не может существовать отрицательное количество часов
        :param hours_of_existence: количество часов с момента изготовления шавермы

        Примеры:
        >>> shaverma = Shaverma("Шаверма с сыром", 47) # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название шавермы должно быть str")
        self.name = name

        if not isinstance(hours_of_existence, int):
            raise TypeError("Значение времени существования шавермы должно быть типа int")
        if hours_of_existence > 48 or hours_of_existence < 40:
            raise ValueError("Значение времени существования шавермы должно быть от 0 до 48")
        self.hours_of_existence = hours_of_existence

    def fall_apart(self) -> None:
        """
        Шаверма разваливается в руках

        Примеры:
        >>> shaverma = Shaverma("Шаверма с сыром", 47)
        >>> shaverma.fall_apart()
        """
        ...

    def cause_heartburn(self, consumer_name: str) -> bool:
        """
        Шаверма вызывает изжогу у потребителя, если у него нет закалки

        :param consumer_name: Имя потребителя шавермы
        :raise TypeError: Если имя потребителя не является строкой, то возвращается ошибка

        :return: Получилось ли вызвать изжогу (зависит от иммунитета)

        Примеры:
        >>> shaverma = Shaverma("Шаверма с сыром", 47)
        >>> shaverma.cause_heartburn("Bob")
        """
        if not isinstance(consumer_name, str):
            raise TypeError("Имя потребителя должно быть строкой")
        ...


if __name__ == "__main__":

    doctest.testmod()  # тестирование примеров, которые находятся в документации
