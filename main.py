def display_menu():
    print("1. Просмотреть заметки")
    print("2. Добавить заметку")
    print("3. Удалить заметку")
    print("4. Выйти")


def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            if notes:
                print("Заметки:")
                for i, note in enumerate(notes, start=1):
                    print(f"{i}. {note.strip()}")
            else:
                print("Заметок нет.")
    except FileNotFoundError:
        print("Файл с заметками не найден.")


def add_note():
    note = input("Введите заметку: ")
    try:
        with open("notes.txt", "a") as file:
            file.write(note + "\n")
        print("Заметка добавлена.")
    except Exception as e:
        print(f"Ошибка при добавлении заметки: {e}")


def delete_note():
    view_notes()
    note_number = input("Введите номер заметки, которую хотите удалить: ")
    try:
        note_number = int(note_number)
        with open("notes.txt", "r") as file:
            notes = file.readlines()
        if 1 <= note_number <= len(notes):
            del notes[note_number - 1]
            with open("notes.txt", "w") as file:
                file.writelines(notes)
            print("Заметка удалена.")
        else:
            print("Некорректный номер заметки.")
    except ValueError:
        print("Пожалуйста, введите корректный номер заметки.")
    except Exception as e:
        print(f"Ошибка при удалении заметки: {e}")


def main():
    try:
        while True:
            display_menu()
            choice = input("Выберите пункт меню (1-4): ")
            if choice == "1":
                view_notes()
            elif choice == "2":
                add_note()
            elif choice == "3":
                delete_note()
            elif choice == "4":
                print("До свидания!")
                break
            else:
                print("Некорректный выбор.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
