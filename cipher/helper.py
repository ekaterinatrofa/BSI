"""
Author: Kateryna Trofymenko
"""

import os


def make_folder(folder):
    os.makedirs(folder, exist_ok=True)
    for item in range(10):
        with open(folder + "/" + "hello_world_{}.txt".format(item), "w") as f:
            f.write("This is my first line of code")
            f.write("\nThis is my second line of code with {} the first item in my list".format(item))
            f.write("\nAnd this is my last line of code")
    list_dir = []
    for dirpath, _, filenames in os.walk(folder):
        for f in filenames:
            list_dir.append(os.path.abspath(os.path.join(dirpath, f)))

    return list_dir



