import os

from datetime import datetime
from dateutil import tz
from PIL import Image
from PIL.ExifTags import TAGS

from djmemori.models import Photo


LCL_TZ = tz.tzlocal()


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


def dms2dd(gpsinfo):
    lat = [float(x)/float(y) for x, y in gpsinfo[2]]
    latref = gpsinfo[1]
    lon = [float(x)/float(y) for x, y in gpsinfo[4]]
    lonref = gpsinfo[3]

    lat = lat[0] + lat[1]/60 + lat[2]/3600
    lon = lon[0] + lon[1]/60 + lon[2]/3600
    if latref == 'S':
        lat = -lat
    if lonref == 'W':
        lon = -lon    

    return (lat, lon)


def save_photo(root, path):
    exif  = get_exif(os.path.join(root.path, path))
    photo = Photo(root=root, path=path)
    if exif is None:
        p.save()
        return

    if exif.has_key('DateTimeOriginal'):
        date_taken = datetime.strptime(exif['DateTimeOriginal'], '%Y:%m:%d %H:%M:%S')
        date_taken.replace(tzinfo=LCL_TZ)
        photo.date_taken = date_taken
    if exif.has_key('ExifImageWidth'):
        photo.width = int(exif['ExifImageWidth'])
    if exif.has_key('ExifImageHeight'):
        photo.height = int(exif['ExifImageHeight'])
    if exif.has_key('Make'):
        photo.make = exif['Make']
    if exif.has_key('Model'):
        photo.model = exif['Model']
    if exif.has_key('GPSInfo') and len(exif['GPSInfo']) > 0:
        photo.latitude, photo.longitude = dms2dd(exif['GPSInfo'])
    photo.save()
        

if __name__=='__main__':
    get_exif("../memori/upload.jpg")
