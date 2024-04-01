class ZeroCountError(Exception):
    """Класс ошибки нулевого количества проудкта"""

    def __init__(self, *args):
        """Конструктор класса ZeroCountError"""

        self.message = args[0] if args else "Количество продукта не может быть нулевым!"

    def __str__(self):
        """Возвращает строковое представление объектов класса ZeroCountError"""

        return self.message
