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


def dms2dd(gpsinfo)
    lat = [float(x)/float(y) for x, y in gpsinfo['GPSInfo'][2]]
    latref = gpsinfo['GPSInfo'][1]
    lon = [float(x)/float(y) for x, y in gpsinfo['GPSInfo'][4]]
    lonref = gpsinfo['GPSInfo'][3]

    lat = lat[0] + lat[1]/60 + lat[2]/3600
    lon = lon[0] + lon[1]/60 + lon[2]/3600
    if latref == 'S':
        lat = -lat
    if lonref == 'W':
        lon = -lon    

    return (lat, lon)


if __name__=='__main__':
    get_exif("../memori/upload.jpg")
