# ----------------------------------
# Program by Michael Eskin
#
# Version   Date         Info
#   1.0     2021    Initial Version
# ----------------------------------

from core import create_file, create_dir, delete, copy_file, save_info, get_list, change_dir

import sys

save_info('[Start]')

try:
    command = sys.argv[1]
except:
    print('Need to chose the command. Use help.')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except:
            print('No name of file')
        else:
            create_file(name)
    elif command == 'create_dir':
        try:
            name = sys.argv[2]
        except:
            print('No name of dir')
        else:
            create_dir(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except:
            print('No name of dir/file')
        else:
            delete(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except:
            print('No name new_name of file')
        else:
            copy_file(name, new_name)
    elif command == 'ch':
        try:
            name = sys.argv[2]
        except:
            print('No name of path')
        else:
            change_dir(name)
    elif command == 'help':
        print('list - show all dirs ans files\n'
              'create_file - file creation\n'
              'create_dir - dir creation\n'
              'delete - delete file or dir\n'
              'copy - copy file or dir\n'
              'save_info - save logs to log.txt')
    else:
        print('Unknown command')

save_info('[End]')
