# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
import shutil

def make_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('Директория {} создана'.format(dir_name))
    except FileExistsError:
        print('Директория {} уже существует'.format(dir_name))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir():
    for dir in os.listdir():
        if os.path.isdir(dir):
            print(dir)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_current_file():
    file_name = os.path.basename(sys.argv[0])
    shutil.copyfile(file_name, 'copy_of_{}'.format(file_name))

# make_dir("Проверка")
# list_dir()

