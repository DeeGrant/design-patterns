from __future__ import annotations


class Facade:
    def __init__(self, subsystem1: SubSystem1, subsystem2: SubSystem2) -> None:
        self._subsystem1 = subsystem1 or SubSystem1()
        self._subsystem2 = subsystem2 or SubSystem2()

    def operation(self) -> str:
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


class SubSystem1:
    def operation1(self) -> str:
        return "SybSystem1: Ready!"

    def operation_n(self) -> str:
        return "SubSystem1: Go!"


class SubSystem2:
    def operation1(self) -> str:
        return "SubSystem2: Get ready!"

    def operation_z(self) -> str:
        return "SubSystem2: Fire!"


def client_code(facade: Facade) -> None:
    print(facade.operation(), end="")


if __name__ == "__main__":
    subsystems1 = SubSystem1()
    subsystems2 = SubSystem2()
    facade = Facade(subsystems1, subsystems2)
    client_code(facade)
