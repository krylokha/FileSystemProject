from __future__ import annotations
from file_folder import Folder
import file_system as FS

class Memento():
    pass

class MementoReal(Memento):
    def __init__(self, root_folder) -> Folder:
        self.root_folder = root_folder

class Caretaker:
    __snapshots: list[Memento]

    def __init__(self):
        self.__snapshots = []

    def save(self, m: Memento):
        self.__snapshots.append(m)

    def load(self, index: int) -> Memento:
        return self.__snapshots[index]

def main():
    fs = FS.FileSystem()
    root = fs.get_root()
    pictures = root.create_folder("Фотографии")
    work = root.create_file("Курсовая.txt")
    cats = pictures.create_folder("Котики")
    vasya = pictures.create_file("Вася.jpg")
    print(fs)

if __name__ == "main":
    main()