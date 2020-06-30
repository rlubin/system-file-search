import re
from pathlib import Path
import os

def save_paths(data):
    """write the indexing to a text file"""
    with open('file.txt', 'w', encoding='utf-8') as f:
        for x in data:
            f.write(x + '\n')
 
def index_dir(path):
    """recursive function that indexes a directory"""
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

def get_root():
    """return path of root of file system"""
    return Path.home().parts[0]

def save_to_file():
    """save all of the filepaths"""
    root_dir = get_root()
    p = Path('.')
    p = p.resolve()
    system_filepaths = index_dir(root_dir)
    save_paths(system_filepaths)