from __future__ import annotations
from file_folder import Folder
from memento_caretaker import Memento, MementoReal

class FileSystem():
    __root_folder: Folder

    def __init__(self):
        self.__root_folder = Folder("C:/")

    def get_root(self) -> Folder:
        return self.__root_folder

    def create_memento(self) -> Memento:
        return MementoReal(self.__root_folder.deepcopy())

    def restore(self, m: Memento):
        self.__root_folder = m.root_folder.deepcopy()