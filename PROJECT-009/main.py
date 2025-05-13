import os
import time

# === Цвета (ANSI)
COLORS = {
    "green": "\033[92m",
    "red": "\033[91m",
    "cyan": "\033[96m",
    "yellow": "\033[93m",
    "reset": "\033[0m"
}

# === Укажи пути к своим скриптам ===
scripts = {
    "datavirus": "/storage/emulated/0/projects/viruses/PROJECT-ALPHA-009/res/dataadder.py",
    "editorvirus": "/storage/emulated/0/projects/viruses/PROJECT-ALPHA-009/res/dataeditor.py",
    "deletevirus": "/storage/emulated/0/projects/viruses/PROJECT-ALPHA-009/res/deletedata.py",
    "keyvirus": "/storage/emulated/0/projects/viruses/PROJECT-ALPHA-009/res/keylocker.py",
    "renamevirus": "/storage/emulated/0/projects/viruses/PROJECT-ALPHA-009/res/renamefiles.py"
}

def print_menu(color="cyan"):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(COLORS[color] + """
====== ВИРУС-МЕНЮ ======
1. datavirus
2. editorvirus
3. deletevirus
4. keyvirus
5. renamevirus
6. Изменить цвет
7. Выход
""" + COLORS["reset"])

def run_script(script_path):
    try:
        os.system(f'python "{script_path}"')
    except Exception as e:
        print(f"Ошибка запуска: {e}")
        time.sleep(2)

def main():
    color = "cyan"

    while True:
        print_menu(color)
        choice = input("Выбери номер функции: ").strip()

        if choice == "1":
            run_script(scripts["datavirus"])
        elif choice == "2":
            run_script(scripts["editorvirus"])
        elif choice == "3":
            run_script(scripts["deletevirus"])
        elif choice == "4":
            run_script(scripts["keyvirus"])
        elif choice == "5":
            run_script(scripts["renamevirus"])
        elif choice == "6":
            print("Доступные цвета: green, red, cyan, yellow")
            color_input = input("Введи цвет: ").strip().lower()
            if color_input in COLORS:
                color = color_input
            else:
                print("Нет такого цвета.")
                time.sleep(1)
        elif choice == "7":
            print("Выход...")
            break
        else:
            print("Неверный ввод.")
            time.sleep(1)

if __name__ == "__main__":
    main()