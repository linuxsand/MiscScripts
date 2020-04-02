# wrote this script for my friend LT
#   2020-04-02, Huang Jie
import os

base_url = 'https://www.51halcon.com/down/license/'

def py2_read_url(url, dir_to_store='.'):
    import urllib2
    line = urllib2.urlopen(url + 'licfile.txt').read()
    filename, _ = tuple(line.split(','))

    f = urllib2.urlopen(url + filename)
    path = os.path.join(dir_to_store, filename)
    with open(path, 'wb') as licfile:
        licfile.write(f.read())  # lic file is small
    print('downloaded as ' + path)

def py3_read_url(url, dir_to_store='.'):
    import urllib.request
    line = urllib.request.urlopen(url + 'licfile.txt').read()
    filename, _ = tuple(line.split(b','))
    filename = filename.decode('ascii')

    path = os.path.join(dir_to_store, filename)
    path = os.path.normpath(path)
    f = urllib.request.urlopen(url + filename)
    with open(path, 'wb') as licfile:
        licfile.write(f.read())  # lic file is small
    print('downloaded as ' + path)

if __name__ == '__main__':
    import sys
    dir_to_store = os.path.join(os.environ['userprofile'], 'Desktop')
    if len(sys.argv) > 1:
        dir_to_store = sys.argv[1] if os.path.exists(sys.argv[1]) else '.'
    print('file will store at ' + dir_to_store)
    # sys.exit(0)
    if sys.version_info.major == 2:
        py2_read_url(base_url, dir_to_store)
    else:
        py3_read_url(base_url, dir_to_store)