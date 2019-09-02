# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
#from os import listdir
import shutil

dir_name = ''

for i in range(1, 10):
    #dir_name = 'dir_' + str(i)
    dir_path = os.path.join(os.getcwd(), 'dir_'+str(i))
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')

for i in range(1, 10):
    if os.path.isdir('dir_'+str(i)):
        shutil.rmtree('dir_'+str(i))  # remove dir and all contains
    else:
        raise ValueError("file {} is not a file or dir.".format('dir_'+str(i)))



# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print(os.listdir())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
dir_path = os.path.join(os.getcwd(), 'New_dir')
try:
    os.mkdir(dir_path)
except FileExistsError:
    print('Такая директория уже существует')

shutil.copyfile(r'hw5_e.py', r'New_dir/hw5_e.py')
