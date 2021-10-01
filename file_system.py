from __future__ import annotations
from abc import ABC

class FileSystem:
    # раздели на папки и файлы класс ещё
    def __init__(self) -> None:
        self.folders = []
        self.files = []

    def add_folder(self):
        name = str(input('Input folder\'s name: '))
        self.folders.append(name)
        self.files.append(self.add_file())
        print(self.folders)
        print(self.files)

    def add_file(self):
        name = str(input('Input files names. If there is no files just remain this field empty: '))
        return (name.split())

    def delete_folder(self):        
        name = str(input('Input folder\'s name: '))
        for i in range(len(self.folders)):
            if name == self.folders[i]:
                self.folders.remove(self.folders[i])
                self.files.remove(self.files[i])
        print(self.folders)
        print(self.files)        
    
    def delete_file(self):
        name = str(input('Input file\'s name: '))
        for i in range(len(self.files)):
            for j in range(len(self.files[i])):
                if name == self.files[i][j]:
                    self.files.remove(self.files[i][j])
        print(self.folders)
        print(self.files)      


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

    def __str__(self):
        return f"Your saving: {self.__saves}"


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
    system.restore(caretaker.get_save(n))
    print(system)

fs = FileSystem()
fs.add_folder()
# fs.delete_file()
# fs.delete_folder()
main()