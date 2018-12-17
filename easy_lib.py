import os
import shutil

files = os.listdir(os.getcwd())

def create_dir(name):
    dir_path = os.path.join(os.getcwd(), '{}'.format(name))
    print('Dir {} created.'.format(dir_path))
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Dir already exists.')

def create_dirs():
    for i in range(1,10):
        create_dir('dir_{}'.format(i))

def show_dirs(path):
    #files = os.listdir(path)
    dirs = [os.path.join(path, o) for o in os.listdir(path)
            if os.path.isdir(os.path.join(path, o))]
    if dirs:
        print('Dir has {} subdirs:'.format(len(dirs)))
        for dir in dirs:
            print(dir)
        return(dirs)
    else:
        print("There is no subdirs in this dir.")
        return None

def show_cur_subdirs():
    show_dirs(os.getcwd())

def show_all(path):
    files = os.listdir(path)
    if files:
        print('Dir has {} files and subdirs:'.format(len(files)))
        for f in files:
            print(f)
        return(files)
    else:
        print("There is no files or subdirs in this dir.")
        return None

def show_cur_all():
    show_all(os.getcwd())

def drop_dir(name):
    try:
        shutil.rmtree(name)
        print('Dir {} was deleted.'.format(name))
    except OSError as e:
        print ("Error: {} - {}".format(e.filename, e.strerror))

def drop_dirs(names):
    print('Deleting {} dirs:'.format(len(names)))
    for name in names:
        drop_dir(name)


def copy_skript_file():
    shutil.copy2(r'{}'.format(__file__), r'copy_{}'.format(__file__))
    print('File {} copied'.format(__file__))