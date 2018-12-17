import os
import sys
sys.path.append(os.getcwd())
#print('sys.argv = ', sys.argv)
import easy_lib as e_lib


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
    print('q -- to exit')
    print()

do = {
    'cd': change_dir,
    'ls': e_lib.show_cur_all,
    'rd': e_lib.drop_dir,
    'crd': e_lib.create_dir,
    'help': give_help
}

give_help()
while True:
    command = input("Ready for command: ")
    keys = command.split(' ')

    if keys[0] == 'q':
        print('Bye')
        sys.exit()
    elif keys[0] in do.keys():
        try:
            param = keys[1]
        except IndexError:
            param = None

        if param:
            do[keys[0]](param)
        else:
            do[keys[0]]()
    else:
        print('Wrong key was given. Try \'help\' key for examples')
