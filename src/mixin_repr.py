class MixinRepr:
    def __init__(self):
        """Конструктор класса, выводит в консоль результат метода __repr__()"""

        print(self.__repr__())

    def __repr__(self):
        """Возвращает строку в виде: НазваниеКласса(аргумент1, аргумент2, ...)"""

        values = [value for value in self.__dict__.values()]

        return f"{self.__class__.__name__}{tuple(values)}"
