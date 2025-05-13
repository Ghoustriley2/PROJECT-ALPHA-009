import os
import shutil

def delete_folder_if_exists(folder_path):
    if os.path.exists(folder_path):
        if os.path.isdir(folder_path):
            try:
                shutil.rmtree(folder_path)  # Удаляет папку и всё её содержимое
                print(f"Папка '{folder_path}' успешно удалена.")
            except Exception as e:
                print(f"Ошибка при удалении папки: {e}")
        else:
            print(f"Путь '{folder_path}' существует, но это не папка.")
    else:
        print(f"Папка '{folder_path}' не найдена.")

# Пример использования
folder_path = '/storage/emulated/0/android/data'  # Замените на нужный путь
delete_folder_if_exists(folder_path)