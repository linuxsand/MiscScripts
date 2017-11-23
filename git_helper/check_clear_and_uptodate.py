#coding: utf-8
import os, sys
nogit = False
try:
    from git import Repo
except ImportError:
    nogit = True

if nogit:
    print 'please: `pip install gitpython`'
    sys.exit(-1)


def get_last_commit_sha(repo):
    # repo maybe local or remote
    try:
        # only check master branch
        return repo.refs.master.commit.hexsha
    except AttributeError as e:
        print "\t", repo, "error:", e
        return None


repos_parent = "./repos_parent.txt"
if not os.path.exists(repos_parent):
    print repos_parent, "does not exist. abort"
    sys.exit(-1)
dirs = []
with open(repos_parent, "r") as f:
    for line in f:
        if not str.isspace(line) and os.path.exists(line.rstrip()):
            dirs.append(line.rstrip())
print dirs, "\n"

dirty_counter = 0
for _dir in dirs:
    for fo in os.listdir(_dir):
        repo_path = os.path.join(_dir, fo)
        if not os.path.isdir(repo_path): continue
        repo = None
        try:
            repo = Repo(repo_path)
            # print repo_path
        except Exception:
            # print 'err at', repo_path
            continue

        # check if repo has uncommitted changes
        if repo.is_dirty():
            print "[dirty repo]:", repo_path
            dirty_counter += 1

        if len(repo.remotes) == 0:
            print repo_path, "has no remote"
            continue
        # check if remote is up-to-date
        local_sha = get_last_commit_sha(repo)
        for remote_repo in repo.remotes:
            remote_sha = get_last_commit_sha(remote_repo)
            if remote_sha is None: print "\tget sha err ---->", repo_path
            elif remote_sha != local_sha:
                print repo_path, "->", remote_repo.name, "is not same as local"

if (dirty_counter == 0): print "\nall clear"
else: print "\nexists dirty repo(s), num:", dirty_counter

input("press ENTER to exit")
