import datetime
import os
import sys

print(sys.argv)

x = datetime.datetime.now()
mkdir_ok = False
for i in range(1, 20):
    name = '{0}{1:02d}{2:02d}-{3}'.format(x.year, x.month, x.day, i)
    if os.path.exists(name): continue
    print('dir name is', name)
    os.mkdir(name)
    os.chdir(name)
    print('current dir is', os.getcwd())
    mkdir_ok = True
    break

if mkdir_ok:
    os.system('ftp -s:..\\ftp.txt %s' % sys.argv[1])