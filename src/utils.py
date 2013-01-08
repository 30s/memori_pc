from PIL import Image
from PIL.ExifTags import TAGS


def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    if info is None:
        return None
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret


if __name__=='__main__':
    get_exif("../memori/upload.jpg")
