import os
import time
import random
import string
import shutil

def create_random_file(file_path, size_in_bytes):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        symbols = string.ascii_letters + string.digits + string.punctuation
        chunk = ''.join(random.choices(symbols, k=size_in_bytes))
        f.write(chunk)
    print(f"Создан файл размером ~1 МБ: {file_path}")

def copy_for_30_seconds(source_file, target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    start_time = time.time()
    count = 0
    while time.time() - start_time < 300:
        new_file_path = os.path.join(target_folder, f'copy_{count}.txt')
        shutil.copy2(source_file, new_file_path)
        count += 1
        print(f"Скопирован: {new_file_path}")
    print(f"Готово. Создано {count} копий за 30 секунд.")

# Параметры
original_file = '/storage/emulated/0/error404.txt'  # Путь, где создаётся исходный файл
destination_folder = '/storage/emulated/0/target_folder'  # Папка, куда будут копии
size_in_bytes = 1024 * 1024  # 1 МБ

# Шаг 1: Создание 1 МБ файла
create_random_file(original_file, size_in_bytes)

# Шаг 2: Копирование файла 30 секунд
copy_for_30_seconds(original_file, destination_folder)