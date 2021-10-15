import file_system as FS
import memento_caretaker as MC

def main():
    fs = FS.FileSystem()
    root = fs.get_root()
    pictures = root.create_folder("Фотографии")
    work = root.create_file("Курсовая.тиэксти")
    cats = pictures.create_folder("Котики")
    vasya = pictures.create_file("Вася.жпег")
    root.print(0)
    caretaker = MC.Caretaker()
    n = caretaker.save(fs.create_memento())
    dogs = pictures.create_file("Собачки.жпег")
    fs.print()
    fs.restore(caretaker.load(0))
    fs.print()

if __name__ == "__main__":
    main()
