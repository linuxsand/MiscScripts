import os
from os.path import join, normpath

def main():
    folders = []
    parent = os.getcwd()

    for root, dirs, files in os.walk('.'):
        for _dir in dirs:
            if _dir == ".git":
                folders.append(
                    normpath(join(parent, root))
                    )

    print 'Total git repos: %d\n' % len(folders)
    for repo in folders:
        print repo

if __name__ == '__main__':
    main()
    raw_input()

