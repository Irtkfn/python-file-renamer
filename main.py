import os
from pathlib import Path

# 1. ОПРЕДЕЛЕНИЕ ФУНКЦИИ
def rename_files(folder_path, prefix):
    path_obj = Path(folder_path)
    
    # Получаем список файлов
    files = sorted([f for f in path_obj.iterdir() if f.is_file()])
    
    # Берем первые 100
    files_to_rename = files[:100]

    for index, file in enumerate(files_to_rename, start=1):
        extension = file.suffix # расширение (например, .jpg)
        
        # Создаем новое имя
        new_name = f"{prefix}_{index:03d}{extension}"
        
        # Создаем полный путь к новому файлу
        new_path = path_obj / new_name
        
        # Переименовываем
        file.rename(new_path)
        print(f"Готово: {file.name} -> {new_name}")

# 2. ОСНОВНОЙ БЛОК
if __name__ == "__main__":
    print("--- Программа массового переименования ---")
    
    # Путь спрашивается у пользователя:
    user_path = input("Введите путь к папке (или перетащите её сюда): ").strip()
    user_prefix = input("Введите название для шаблона (например, 'vacation'): ")

    # Проверяем, существует ли такая папка
    if os.path.exists(user_path):
        # Передаем то, что ввел пользователь (user_path), 
        # внутрь функции, где оно станет называться (folder_path)
        rename_files(user_path, user_prefix)
        print("\nВсе задачи выполнены!")
    else:
        print("Ошибка: Указанный путь не существует.")