# python3
import time
import os
import random
import pathlib
import barcode
from barcode.writer import ImageWriter


ABS_DIR_TO_STORE_IMAGES = 'D:\\c128'
import shutil
shutil.rmtree(ABS_DIR_TO_STORE_IMAGES, ignore_errors=True)
if not os.path.exists(ABS_DIR_TO_STORE_IMAGES):
    os.mkdir(ABS_DIR_TO_STORE_IMAGES)


def rand_prefix():
    return '_' + str(random.randint(100, 119)) + '_' + str(time.time())[:-4]


def gen_single(code='test'):
    # return image path: file:///path/to/image
    C128 = barcode.get_barcode_class('code128')
    ins_c128 = C128(code, writer=ImageWriter())
    path = os.path.join(ABS_DIR_TO_STORE_IMAGES, code + rand_prefix())
    # print(path)
    ins_c128.save(path)
    return pathlib.Path(path).as_uri() + '.png'


def gen_html(image_path_list=list()):
    # call once
    tpl = open('A4_template.html').read()

    s = ''
    for i in range(len(image_path_list)):
        tr = '<th><img src="%s"></th>' % image_path_list[i]
        if i % 2 == 0:
            onerow = '<tr>' + tr
            if i == len(image_path_list) - 1:
                s += onerow + '</tr>'
        else:
            onerow += tr + '</tr>\n\n'
            s += onerow

    newcontent = tpl.replace('{{DUMMY}}', s)
    newname = 'codes_to_print%s.html' % rand_prefix()
    with open(newname, 'w') as f:
        f.write(newcontent)
        print('\n\ngenerated %s' % newname)    
    os.system('explorer %s' % newname)



def test():
    results = list()
    for i in range(30):
        results.append(gen_single(str(i) + rand_prefix()))

    print(results)
    gen_html(results)


def gen_from_csv():
    import csv
    csvfile = open('boxinfo.csv', encoding='utf-8')
    reader = csv.reader(csvfile)
    results = list()
    for row in reader:
        # print(row)
        if row[0].startswith('\ufeff'): continue

        line = '{0},{1},{2},{3}'.format(*row)
        print(line)
        results.append(gen_single(line))

    gen_html(results)


if __name__ == '__main__':
    # test()
    gen_from_csv()