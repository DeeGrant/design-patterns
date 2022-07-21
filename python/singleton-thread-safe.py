from threading import Lock, Thread


class SingletonMeta(type):
    _instances = {}

    """
    Use lock object to synchronize threads during first access to the Singleton.
    """
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance

        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self):
        pass


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == "__main__":
    """
    If you see the same value, then the singleton was reused - Good.
    If you see different values, then two singletons were created - Bad.
    """
    # test_singleton("FOO")
    # test_singleton("BAR")
    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()
