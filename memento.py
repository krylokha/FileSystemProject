from __future__ import annotations
from abc import ABC
from file_system import FileSystem


class Memento:
    pass


class MementoReal(Memento):
    def __init__(self, saves):
        self.saves = saves


class System:
    def __init__(self):
        self.__saves = FileSystem()

    def create_memento(self) -> Memento:
        return MementoReal(self.__saves)

    def restore(self, savepoint: Memento):
        self.__saves = savepoint.saves

    def change_state(self):
        self.__saves = 0

    def __str__(self):
        return f"Meaning of life: {self.__saves}"


class Caretaker:
    def __init__(self):
        self.savepoints = []

    def save(self, savepoint: Memento):
        self.savepoints.append(savepoint)
        return len(self.savepoints) - 1

    def get_save(self, n: int) -> Memento:
        return self.savepoints[n]


def main():
    system = System()
    caretaker = Caretaker()
    n = caretaker.save(system.create_memento())
    print(system)
    system.change_state()
    print(system)
    system.restore(caretaker.get_save(n))
    print(system)


if __name__ == "__main__":
    main()