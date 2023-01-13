class InfoMessage:
    """Информационное сообщение о тренировке."""
    pass

    def __init__(self,
                 training_type: object,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        result: str = (f'Тип тренировки: {self.training_type}; '
                         f'Длительность: {self.duration:.3f} ч.; '
                         f'Дистанция: {self.distance:.3f} км; '
                         f'Ср. скорость: {self.speed:.3f} км/ч; '
                         f'Потрачено ккал: {self.calories:.3f}.')
        return result


M_IN_KM = 1000


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self, step: bool = True) -> float:
        """Получить дистанцию в км."""
        LEN_STEP: float = 0
        if step:
            LEN_STEP = 0.65
        else:
            LEN_STEP = 1.38
        return self.action * LEN_STEP / M_IN_KM

    def get_mean_speed(self,
                       distance_training: float = 0,
                       time_training: float = 0
                       ) -> float:
        """Получить среднюю скорость движения."""
        return distance_training / time_training

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""


class Running(Training):
    """Тренировка: бег."""
    CALORIES_MEAN_SPEED_MULTIPLIER: int = 18
    CALORIES_MEAN_SPEED_SHIFT: float = 1.79

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        result: float = ((self.CALORIES_MEAN_SPEED_MULTIPLIER *
                          super.get_mean_speed() + self.CALORIES_MEAN_SPEED_SHIFT)
                         * self.weight / M_IN_KM * self.duration)
        return result


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    CALORIES_MEAN_WEIGHT_MULTIPLIER1: float = 0.035
    CALORIES_MEAN_WEIGHT_MULTIPLIER2: float = 0.029

    def get_spent_calories(self, height) -> float:
        """Получить количество затраченных калорий."""
        result: float = (((self.CALORIES_MEAN_WEIGHT_MULTIPLIER1 * self.weight +
                           (super.get_mean_speed() ** 2 / height)
                           * self.CALORIES_MEAN_WEIGHT_MULTIPLIER2 * self.weight
                           * self.duration)))
        return result


class Swimming(Training):
    """Тренировка: плавание."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: int
                 ) -> None:
        super.__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return (get_mean_speed() + 1.1) * 2 * self.weight * self.duration

    def get_distance(self) -> float:
        super.get_distance(0)

    def get_mean_speed(self,
                       distance_training: float = 0,
                       time_training: float = 0
                       ) -> float:
        """Получить среднюю скорость движения."""
        return self.length_pool * self.count_pool / M_IN_KM / time_training


comand: list = ()


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    if workout_type == 'SWM':

        return Swimming(data)
    elif workout_type == 'RUN':

        return Running(data)
    elif workout_type == 'WLK':
        camand = (get_spent_calories)
        return SportsWalking(data)


def main(training: Training) -> None:
    """Главная функция."""
    info: str = training.show_training_info()


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

