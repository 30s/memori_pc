import os
from datetime import datetime
from dateutil import tz
from django.core.management.base import BaseCommand
from djmemori.models import ScanPath, Photo
from djmemori.utils import get_exif, dms2dd


LCL_TZ = tz.tzlocal()

class Command(BaseCommand):
    help = "Scan photos from ScanPath, extract photos' exif info and save them in DB."

    def save_photo(self, root, path):
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

    def handle(self, *args, **options):
        for i in ScanPath.objects.all():
            self.stdout.write("Scanning path: %s ...\n" % i.path)
            for p in os.listdir(i.path):
                self.stdout.write("\n\t%s ... " % p)
                if not p.endswith('.jpg'):
                    self.stdout.write("Ignored!")
                    continue
                try:
                    self.save_photo(i, p)
                    self.stdout.write("Saved!")
                except Exception, e:
                    self.stdout.write("Extract photo info failed!")
                    self.stdout.write(str(e))
