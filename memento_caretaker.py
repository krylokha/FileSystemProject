from __future__ import annotations
from file_folder import Folder
import file_system as FS

class Memento():
    pass

class MementoReal(Memento):
    def __init__(self, root_folder) -> Folder:
        self.root_folder = root_folder

class Caretaker:
    def __init__(self):
        self.__snapshots = []

    def save(self, m: Memento):
        self.__snapshots.append(m)

    def load(self, index: int) -> Memento:
        return self.__snapshots[index]

