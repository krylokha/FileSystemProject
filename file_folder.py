from __future__ import annotations
from fs_object import FSObject

class File(FSObject):
    def __init__(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def edit(self, name: str):
        self.__name = name

    def delete(self, name: str):
        pass

    def print(self, offset: int):
        print(f"{' ' * (2 * offset)} - {self.__name}")

    def copy(self):
        copy_file = File(self.__name)
        return copy_file

class Folder(FSObject):
    def __init__(self, name: str):
        self.__name = name
        self.__children = []

    def get_name(self) -> str:
        return self.__name

    def create_folder(self, name: str) -> Folder:
        new_folder = Folder(name)
        self.__children.append(new_folder)
        return new_folder
        # я вообще не уверена, что так можно, не обессудьте))

    def create_file(self, name: str) -> File:
        new_file = File(name)
        self.__children.append(new_file)
        return new_file

    def get_children(self):
        return self.__children

    def get_child(self, root, name: str) -> FSObject:
        for child in self.__children:
            if child.get_name() == name:
                return child
            result = self.get_child(child, name)
            if result is not None:
                return result
        return None

    def delete(self, name: str):
        for child in self.__children:
            if name == child:
                self.__children.remove(child)

    def print(self, offset: int):
        print(f"{' ' * (2 * offset)} - {self.__name}/")
        for child in self.__children:
            child.print(offset + 1)

    def copy(self):
        children_copy = []
        copy_folder = Folder(self.__name)
        for child in self.__children:
            children_copy.append(child.copy())
        copy_folder.__children = children_copy
        return copy_folder