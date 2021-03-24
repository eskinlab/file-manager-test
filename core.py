# ----------------------------------
# Program by Michael Eskin
#
# Version   Date         Info
#   1.0     2021    Initial Version
# ----------------------------------

import os
import shutil
import datetime


# File creation
def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        f.write(text) if text else None


def create_dir(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print(f'{name} dir is already exist')


def delete(name):
    try:
        if os.path.isdir(name):
            os.rmdir(name)
        else:
            os.remove(name)
    except FileNotFoundError:
        print(f'{name} is not exist')


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print(f'{new_name} already exist')
    else:
        shutil.copy(name, new_name)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def get_list(dirs_only=False):
    result = os.listdir()
    if dirs_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def change_dir(name):
    os.chdir(name)
    print(os.getcwd())


if __name__ == "__main__":
    copy_file('fle.txt', 'cp_fle.txt')
    save_info('message')
