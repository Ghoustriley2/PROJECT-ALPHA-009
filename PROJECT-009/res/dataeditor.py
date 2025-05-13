import os
import random
import string

def overwrite_files_with_random_text(folder_path, symbols_count=1000):
    if not os.path.exists(folder_path):
        print("Указанная папка не существует.")
        return

    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            old_path = os.path.join(root, filename)
            new_filename = os.path.splitext(filename)[0] + '.txt'
            new_path = os.path.join(root, new_filename)

            # Переименование файла в .txt (если нужно)
            if not filename.endswith('.txt'):
                os.rename(old_path, new_path)
            else:
                new_path = old_path

            # Перезапись файла случайными символами
            try:
                with open(new_path, 'w') as f:
                    random_text = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=symbols_count))
                    f.write(random_text)
                print(f"Файл перезаписан: {new_path}")
            except Exception as e:
                print(f"Ошибка с файлом {new_path}: {e}")

# ====== ВСТАВЬ СЮДА ПУТЬ К ПАПКЕ ======
target_folder = '/storage/emulated/0/'  # <-- Заменить на нужный путь
overwrite_files_with_random_text(target_folder)