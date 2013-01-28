import math
import os

import Image


DIR_THUMB = 'thumbs/80/'


def get_square_thumb_80(root, path):
    filename = os.path.join(DIR_THUMB, '%d.jpg' % hash(path))
    if os.path.exists(filename):
        return filename

    im = Image.open(os.path.join(root, path))
    size = im.size
    thumb = None
    if size[0] > size[1]:
        # landscape
        off_x = int(math.ceil( (size[0] - size[1]) / 2 ))
        thumb = im.crop((off_x, 0, size[1] + off_x, size[1]))
    else:
        # portrait
        off_y = int(math.ceil( (size[1] - size[0]) / 2 ))
        thumb = im.crop((0, off_y, size[0], off_y + size[0]))
    thumb = thumb.resize((80, 80), Image.ANTIALIAS)
    thumb.convert('RGB').save(filename)
    return filename


def list_android_devices():
    devices = []
    pip = os.popen('adb -d devices')
    pip.readline() # escape first line
    line = pip.readline()
    while len(line) != 0:
        segs = line.split()
        if (len(segs) == 2) and (segs[1] == 'device'):
            devices.append(segs[0])
        line = pip.readline()
    pip.close()
    return devices


def import_photos_from_android(name, path):
    photos = []
    pip = os.popen('adb -s %s shell ls /sdcard/DCIM/Camera/' % name)
    line = pip.readline()
    while len(line) != 0:
        print line
        if line.endswith('.jpg\r\n'):
            os.system('adb -s %s pull /sdcard/DCIM/Camera/%s %s' % (name, line[:-2], path))
            photos.append(line[:-2])
        line = pip.readline()
    return photos


if __name__=='__main__':
    print list_android_devices()
    print import_photos_from_android('a2af63a9',
                                     '/Users/teamx/workspace/memori_pc/src/qtmemori/photos')
