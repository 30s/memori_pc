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
