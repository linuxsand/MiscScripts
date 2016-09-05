import os, random, string
from PIL import Image # Pillow
import shutil
import sys

QUALITY = 95

def new_dir_name(l):
    s = string.ascii_letters + string.digits
    return ''.join(random.sample(s, l))

def do_zip(filename):
    shutil.make_archive(filename, 'zip', root_dir='.', base_dir=filename)
    shutil.rmtree(filename)

def main(size, length, img_path=None, mkdir=False):
    if mkdir:
        dir_ = new_dir_name(length)
        os.mkdir(dir_)
        raw_input('put images in, then press <ENTER>')
        os.chdir(dir_)
        for img in os.listdir('.'):
            print 'processing %s...' % img
            im = Image.open(img)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save('c_'+img, quality=QUALITY)
            im.close()
            os.remove(img)
        ans = raw_input('press <ENTER> to zip, press `n` to exit.')
        if ans.lower().strip() == 'n':
            return
        os.chdir('..')
        do_zip(dir_)
    else:
        print 'processing %s...' % img_path
        im = Image.open(img_path)
        im.thumbnail(size, Image.ANTIALIAS)
        par, img = os.path.split(img_path)
        final_img = os.path.join(par, 'c_'+img)
        im.save(final_img, quality=QUALITY)
        im.close()
        os.remove(img_path)

if __name__ == '__main__':
    try:
        l = int(sys.argv[1].strip())
        img_path = sys.argv[2]
        main((l, l), 8, img_path, False)
    except IndexError:
        l = raw_input('input min length that you want: ')
        l = int(l.strip())
        main((l, l), 8, None, True)
       
