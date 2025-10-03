from faker import Faker

class Fake:
    """
    Класс для генерации случайных тестовых данных с использованием Faker.
    """

    def __init__(self, faker: Faker):
        """
        Инициализация класса с экземпляром Faker.
        :param faker: Экземпляр Faker для генерации данных.
        """
        self.faker = faker

    def text(self) -> str:
        """
        Генерирует случайный текст.
        :return: Случайный текст.
        """
        return self.faker.text()

    def uuid4(self) -> str:
        """
        Генерирует уникальный идентификатор UUID4.
        :return: UUID4 в строковом формате.
        """
        return self.faker.uuid4()

    def email(self) -> str:
        """
        Генерирует случайный email.
        :return: Email в строковом формате.
        """
        return self.faker.email()

    def sentence(self) -> str:
        """
        Генерирует случайное предложение.
        :return: Строка с предложением.
        """
        return self.faker.sentence()

    def password(self) -> str:
        """
        Генерирует случайный пароль.
        :return: Пароль в строковом формате.
        """
        return self.faker.password()

    def last_name(self) -> str:
        """
        Генерирует случайную фамилию.
        :return: Фамилия.
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Генерирует случайное имя.
        :return: Имя.
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Генерирует случайное отчество (используется first_name из Faker).
        :return: Отчество.
        """
        return self.faker.first_name()

    def estimated_time(self) -> str:
        """
        Генерирует случайное количество недель в интервале от 1 до 10.
        :return: Строка вида "N weeks".
        """
        return f"{self.integer(1, 10)} weeks"

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        Генерирует случайное целое число в заданном диапазоне.
        :param start: Нижняя граница (включительно).
        :param end: Верхняя граница (включительно).
        :return: Случайное целое число.
        """
        return self.faker.random_int(start, end)

    def max_score(self) -> int:
        """
        Генерирует случайное число от 50 до 100.
        :return: Случайное целое число.
        """
        return self.integer(50, 100)

    def min_score(self) -> int:
        """
        Генерирует случайное число от 1 до 49.
        :return: Случайное целое число.
        """
        return self.integer(1, 49)


fake = Fake(faker=Faker())