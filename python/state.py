from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    _state = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State) -> None:
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def request1(self) -> None:
        self._state.handle1()

    def request2(self) -> None:
        self._state.handle2()


class State(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")


class ConcreteStateB(State):
    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change te state of the context.")
        self.context.transition_to(ConcreteStateA())

    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")


if __name__ == "__main__":
    context = Context(ConcreteStateA())
    print()
    context.request1()
    print()
    context.request1()
    print()
    context.request2()
    print()
    context.request2()
