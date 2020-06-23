import re
from pathlib import Path
import os

# write the indexing to a text file
def save_paths(data):
    with open('file.txt', 'w', encoding='utf-8') as f:
        for x in data:
            f.write(x + '\n')

# recursive function that indexes a directory
def index_dir(path):
    paths = []
    for x in os.listdir(path):
        p = os.path.join(path, x)
        if os.path.isdir(p):
            # append return to paths
            # add try block around recursive call
            try:
                a = index_dir(p)
                paths.extend(a)
            except:
                print(p, ' is not a dir')
        if os.path.isfile(p):
            paths.append(p)
    return paths

# return path of root of file system
def get_root():
    return Path.home().parts[0]

def main():
    # save all of the filepaths
    root_dir = get_root()
    # print('root', root_dir, '\n')
    p = Path('.')
    p = p.resolve()
    # print(p)
    system_filepaths = index_dir(root_dir)
    # system_filepaths = index_dir(p)
    # print file paths
    # for x in system_filepaths:
    #     print(x)
    save_paths(system_filepaths)

if __name__=='__main__':
    main()