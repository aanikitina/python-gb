import os
import sys
sys.path.append(os.getcwd())
#print('sys.argv = ', sys.argv)
import easy_lib as e_lib
#
# while True:
#     key = input("press 'q' to Exit")
#
#     if key == 'q':
#         sys.exit()


def change_dir(new_path):
    if new_path[0] != '/':
        new_path = os.getcwd()+'/'+new_path
        print('Search in working directory')
    else: print('Absolute path detected')

    try:
        os.chdir(new_path)
        print('Dir was changed. Current dir is {}'.format(new_path))
    except: #FileNotExistsError
        print('There is no dir like : {}'.format(new_path))

def give_help():
    print('\n\n______________HELP______________\nHere is a list of available keywords:\n')
    print('help -- for help')
    print('cd <new_path> -- to move to desired directory')
    print('ls -- to get list of contents: files and subdirectories')
    print('rd <dir_name> -- to remove directory from current directory')
    print('crd <dir_name> -- to create new directory in current directory')
    print()

do = {
    'cd': change_dir,
    'ls': e_lib.show_cur_all,
    'rd': e_lib.drop_dir,
    'crd': e_lib.create_dir,
    'help': give_help
}


try:
    key = sys.argv[1]
except IndexError:
    key = None
    print('Empty key was given. Try \'help\' key for examples')


try:
    param = sys.argv[2]
except IndexError:
    param = None


if key:
    if do.get(key):
        if param:
            do[key](param)
        else: do[key]()
    else:
        print('Wrong key was given. Try \'help\' key for examples')



