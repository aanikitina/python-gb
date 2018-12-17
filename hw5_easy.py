import os
import shutil

files = os.listdir(os.getcwd())

def create_dir(name):
    dir_path = os.path.join(os.getcwd(), '{}'.format(name))
    print('Директория {} создана.'.format(dir_path))
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует.')

def create_dirs():
    for i in range(1,10):
        create_dir('dir_{}'.format(i))

def show_dirs(path):
    #files = os.listdir(path)
    dirs = [os.path.join(path, o) for o in os.listdir(path)
            if os.path.isdir(os.path.join(path, o))]
    if dirs:
        print('Данная директория сождержит {} вложенных директорий:'.format(len(dirs)))
        for dir in dirs:
            print(dir)
        return(dirs)
    else:
        print("Данная директория не содержит вложенных директорий.")
        return False

def drop_dir(name):
    try:
        shutil.rmtree(name)
        print('Директория {} удалена.'.format(name))
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))

def drop_dirs(names):
    print('Удаление {} директорий:'.format(len(names)))
    for name in names:
        drop_dir(name)


def copy_skript_file():
    shutil.copy2(r'{}'.format(__file__), r'copy_{}'.format(__file__))
    print('Скопирован файл {}'.format(__file__))

def run_examples():
    # Создаем и показываем директории
    create_dirs()
    show_dirs(os.getcwd())

    # Создаем копию исполняемого скрипта
    print('Работаем с файлом {}'.format(__file__))
    copy_skript_file()

    # Удаляем директории
    dirs_to_drop = []
    for i in range(1, 10):
        dirs_to_drop.append('dir_{}'.format(i))

    drop_dirs(dirs_to_drop)


run_examples()

