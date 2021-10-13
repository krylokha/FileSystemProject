import file_system as FS

def main():
    fs = FS.FileSystem()
    root = fs.get_root()
    pictures = root.create_folder("Фотографии")
    work = root.create_file("Курсовая.txt")
    cats = pictures.create_folder("Котики")
    vasya = pictures.create_file("Вася.jpg")
    root.print(0)

main()
