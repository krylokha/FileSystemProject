from __future__ import annotations

class FSObject():
    def get_name(self) -> str:
        pass

    def get_children(self) -> list[FSObject]:
        pass

    def get_child(self, root, name: str) -> FSObject:
        pass

    def create_folder(self, name: str):
        pass

    def create_file(self, name: str):
        pass

    def delete(self, name: str):
        pass

    def print(self, offset: int):
        pass