import os

def create_note():
    note_title = input("Введите заголовок заметки: ")
    note_content = input("Введите содержание заметки: ")
    filename = f"{note_title}.txt"
    with open(filename, "w") as file:
        file.write(note_content)
    print("Заметка создана успешно.")

def read_notes():
    notes = os.listdir()
    note_files = [note for note in notes if note.endswith(".txt")]
    if not note_files:
        print("Заметок нет.")
        return
    print("Список заметок:")
    for note_file in note_files:
        print(f"- {note_file[:-4]}")

def read_note():
    note_title = input("Введите заголовок заметки, которую хотите прочитать: ")
    filename = f"{note_title}.txt"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            note_content = file.read()
            print(f"Содержание заметки '{note_title}':")
            print(note_content)
    else:
        print("Заметка не найдена.")

def edit_note():
    note_title = input("Введите заголовок заметки, которую хотите отредактировать: ")
    filename = f"{note_title}.txt"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            note_content = file.read()
            print(f"Текущее содержание заметки '{note_title}':")
            print(note_content)
            new_content = input("Введите новое содержание заметки: ")
            with open(filename, "w") as file:
                file.write(new_content)
            print("Заметка успешно отредактирована.")
    else:
        print("Заметка не найдена.")

def delete_note():
    note_title = input("Введите заголовок заметки, которую хотите удалить: ")
    filename = f"{note_title}.txt"
    if os.path.exists(filename):
        os.remove(filename)
        print("Заметка успешно удалена.")
    else:
        print("Заметка не найдена.")

def main():
    while True:
        print("\nДобро пожаловать в приложение заметок!")
        print("1. Создать заметку")
        print("2. Просмотреть список заметок")
        print("3. Просмотреть заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            read_note()
        elif choice == "4":
            edit_note()
        elif choice == "5":
            delete_note()
        elif choice == "6":
            print("Спасибо за использование приложения заметок. До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
