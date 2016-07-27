import os, sys, random, string, shutil
from PIL import Image # Pillow

def new_dir_name(length):
    s = string.ascii_letters + string.digits
    return ''.join(random.sample(s, length))

def do_zip(filename):
    shutil.make_archive(filename, 'zip', root_dir='.', base_dir=filename)
    shutil.rmtree(filename)

def main(size, length, img_path=None, mkdir=False):
    if mkdir:
        dir_ = new_dir_name(length)
        os.mkdir(dir_)
        raw_input('put images in, then press ENTER.')
        os.chdir(dir_)
        for img in os.listdir('.'):
            print 'processing %s...' % img
            im = Image.open(img)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(img, quality=95)
        raw_input('press ENTER to zip, press CTRL-C to exit.')
        os.chdir('..')
        do_zip(dir_)
    else:
        print 'processing %s...' % img_path
        im = Image.open(img_path)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(img_path, quality=95)

if __name__ == '__main__':
    try:
        length = int(sys.argv[1].strip())
        img_path = sys.argv[2]
        main(
                (length, length),
                8,
                img_path,
                False
            )
    except IndexError:
        _length = raw_input('input min length that you want: ')
        length = int(_length.strip())
        main(
                (length, length),
                8,
                None,
                True
            )
       
