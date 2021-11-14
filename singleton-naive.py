class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python.
    Some possible methods include: base class, decorator, metaclass.
    We will use the metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, variables contain the same instance.")
    else:
        print("Singleton failed, variable contain different instances.")
