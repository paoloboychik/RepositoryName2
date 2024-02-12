import doctest


class Car:
    def __init__(self, velocity: int, brand: str) -> None:
        """
        Creation and preparation of the "Car" object

        :param velocity: Velocity of car (mph)
        :param brand: Brand that design this car

        Example:
        >>> car = Car(150, 'Porsche')  # init of instance
        """
        self.velocity = velocity
        self.brand = brand

    @property
    def velocity(self) -> int:
        return self._velocity

    @velocity.setter
    def velocity(self, velocity: int) -> None:
        """
        Checking for datatype and value range before assignment
        (encapsulation)
        """
        if not isinstance(velocity, int):
            raise TypeError("Velocity should be integer")
        if velocity < 0:
            raise ValueError("Velocity should be positive number")
        self._velocity = velocity

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, brand: str) -> None:
        """
        Checking for datatype before assignment
        (encapsulation)
        """
        if not isinstance(brand, str):
            raise TypeError("Brand should be string")
        self._brand = brand

    def __str__(self) -> str:
        return self.car_type() + f' "{self.brand}"'

    def __repr__(self) -> str:
        return self.car_type() + f'({self.velocity}, {self.brand!r})'

    def car_type(self) -> str:
        """
        To find out the type of car

        :return: Name of the class

        Example:
        >>> car = Car(150, 'Porsche')
        >>> print(car.car_type())
        Car
        """
        return f'{self.__class__.__name__}'

    def drive(self) -> None:
        """
        Car is driving

        Example:
        >>> car = Car(150, 'Porsche')
        >>> car.drive()
        Car "Porsche" is driving
        """
        print(self.__str__() + ' is driving')

    def stop(self) -> None:
        """
        Car is not driving

        Example:
        >>> car = Car(150, 'Porsche')
        >>> car.stop()
        Car "Porsche" is NOT driving
        """
        print(self.__str__() + ' is NOT driving')


class PassengerCar(Car):
    def __init__(self, velocity: int, brand: str, passenger_num: int) -> None:
        """
        Creation and preparation of the "PassengerCar" object

        :param velocity: Velocity of passenger car (mph)
        :param brand: Brand that design this passenger car
        :param passenger_num: Number of seats for passengers

        Example:
        >>> passenger_car = PassengerCar(150, 'Porsche', 2)  # init of instance
        """
        super().__init__(velocity, brand)
        self.passenger_num = passenger_num

    @property
    def passenger_num(self) -> int:
        return self._passenger_num

    @passenger_num.setter
    def passenger_num(self, passenger_num: int) -> None:
        """
        Checking for datatype and value range before assignment
        (encapsulation)
        """
        if not isinstance(passenger_num, int):
            raise TypeError("Number of passenger should be integer")
        if passenger_num < 0:
            raise ValueError("Number of passenger should be positive number")
        self._passenger_num = passenger_num

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.velocity}, {self.brand!r}, {self.passenger_num})'

    def drive(self, if_age_over_18=True):
        """
        Passenger car drive if driver is over 18

        :param if_age_over_18: Driving permit

        Example:
        >>> passenger_car = PassengerCar(150, 'Porsche', 2)
        >>> passenger_car.drive(False)
        PassengerCar "Porsche" is NOT driving
        """
        if if_age_over_18:
            super().drive()
        else:
            super().stop()


class Truck(Car):
    def __init__(self, velocity: int, brand: str, payload: int) -> None:
        """
        Creation and preparation of the "Truck" object

        :param velocity: Velocity of truck (mph)
        :param brand: Brand that design this truck
        :param payload: Max payload of the truck (t)

        Example:
        >>> truck = Truck(90, 'MAN', 10)  # init of instance
        """
        super().__init__(velocity, brand)
        self.payload = payload

    @property
    def payload(self) -> int:
        return self._payload

    @payload.setter
    def payload(self, payload: int) -> None:
        """
        Checking for datatype and value range before assignment
        (encapsulation)
        """
        if not isinstance(payload, int):
            raise TypeError("Payload should be integer")
        if payload < 0:
            raise ValueError("Payload should be positive number")
        self._payload = payload

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.velocity}, {self.brand!r}, {self.payload})'

    def drive(self, if_age_over_21=True):
        """
        Passenger car drive if driver is over 21

        :param if_age_over_21: Driving permit

        Example:
        >>> truck = Truck(90, 'MAN', 10)
        >>> truck.drive(True)
        Truck "MAN" is driving
        """
        if if_age_over_21:
            super().drive()
        else:
            super().stop()


if __name__ == "__main__":
    doctest.testmod()
