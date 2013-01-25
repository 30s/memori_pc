import os
from django.core.management.base import BaseCommand
from djmemori.models import ScanPath
from djmemori.utils import save_photo


class Command(BaseCommand):
    help = "Scan photos from ScanPath, extract photos' exif info and save them in DB."

    def handle(self, *args, **options):
        for i in ScanPath.objects.all():
            self.stdout.write("Scanning path: %s ...\n" % i.path)
            for p in os.listdir(i.path):
                self.stdout.write("\n\t%s ... " % p)
                if not p.endswith('.jpg'):
                    self.stdout.write("Ignored!")
                    continue
                try:
                    save_photo(i, p)
                    self.stdout.write("Saved!")
                except Exception, e:
                    self.stdout.write("Extract photo info failed!")
                    self.stdout.write(str(e))
