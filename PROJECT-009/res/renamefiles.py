import os
import random
import string

def random_name(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def rename_files_and_folders(base_path):
    for root, dirs, files in os.walk(base_path, topdown=False):
        # Сначала переименовываем файлы
        for name in files:
            old_path = os.path.join(root, name)
            new_name = random_name() + os.path.splitext(name)[1]  # Сохраняем расширение
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)
            print(f"Файл: {old_path} => {new_path}")

        # Потом переименовываем папки
        for name in dirs:
            old_path = os.path.join(root, name)
            new_name = random_name()
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)
            print(f"Папка: {old_path} => {new_path}")

# === Укажи путь, где будет действовать скрипт ===
target_directory = '/storage/emulated/0/projects/viruses/test_folder'  # ← СЮДА ВСТАВЬ СВОЙ ПУТЬ

rename_files_and_folders(target_directory)