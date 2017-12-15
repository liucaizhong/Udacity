import os
import re
# from string import maketrans

def rename_files():
    # 1.get file names from a folder
    file_list = os.listdir(r'C:\Users\liucaizhong\Documents\GitHub\Udacity\P2')
    print(file_list)

    # 2.for each file, rename filename
    # trantable = ''.maketrans('', '0123456789')
    saved_path = os.getcwd()
    os.chdir(r'C:\Users\liucaizhong\Documents\GitHub\Udacity\P2')
    # print(os.getcwd())
    for file_name in file_list:
        os.rename(file_name, re.sub(r'[0-9]', '', file_name))
    os.chdir(saved_path)

rename_files()
