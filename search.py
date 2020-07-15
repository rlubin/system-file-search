import re
from pathlib import Path
import os

def find_matches(path, matches, regex):
    """recursive function that crawls through directories and appends filenames to matches array that match the regular expression"""
    for x in os.listdir(path):
        p = os.path.join(path, x)
        if os.path.isdir(p):
            try:
                a = find_matches(p, matches, regex)
                paths.extend(a)
            except:
                pass
        if os.path.isfile(p):
            if re.search(regex, x):
                matches.append(path + '\\' + x)

def system_search(matches, regex):
    """populate matches array with regex filename matches"""
    root_dir = Path.home().parts[0]
    p = Path('.')
    p = p.resolve()
    find_matches(root_dir, matches, regex)