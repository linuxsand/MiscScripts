import os, time
from os.path import join, normpath
from git import Repo

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
        last_commit = Repo(repo).head.commit
        committed_date = last_commit.committed_date
        print 'repo path:', repo
        print 'last commit time:', time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(committed_date)), '\n'

if __name__ == '__main__':
    main()
    raw_input('press <Enter> to exit...')

