import os
import sys
import subprocess
import shutil

# === Установка pyzipper, если не установлен ===
try:
    import pyzipper
except ImportError:
    print("pyzipper не найден. Устанавливаю...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyzipper"])
    import pyzipper

# === Функция архивации с паролем ===
def zip_folder_with_password(folder_path, output_zip_path, password):
    zip_file_path = os.path.join(output_zip_path, "data.zip")

    with pyzipper.AESZipFile(zip_file_path, 'w',
                             compression=pyzipper.ZIP_DEFLATED,
                             encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(password.encode())

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                abs_path = os.path.join(root, file)
                relative_path = os.path.relpath(abs_path, start=folder_path)
                zf.write(abs_path, arcname=relative_path)

    print(f"Папка заархивирована: {zip_file_path} с паролем")

    # Удаление исходной папки
    try:
        shutil.rmtree(folder_path)
        print(f"Папка удалена: {folder_path}")
    except Exception as e:
        print(f"Ошибка при удалении папки: {e}")

# === ТВОИ НАСТРОЙКИ ===
folder_to_zip = '/storage/emulated/0/android/data/'  # Путь к папке
zip_output = '/storage/emulated/0/'                    # Куда сохранить архив
archive_password = 'PROJECT009ALPHA'                                     # Пароль

# === Запуск ===
zip_folder_with_password(folder_to_zip, zip_output, archive_password)