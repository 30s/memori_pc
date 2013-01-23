import os
import sys

import Image

from PySide.QtCore import *
from PySide.QtGui import *

from ui_dlg_local_memori import Ui_DlgLocalMemori

DIR_NAME = os.path.dirname(os.path.abspath(__file__))

sys.path.append(DIR_NAME + '/../djmemori')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djmemori.settings")

from djmemori.models import Photo
from djmemori.views import event_generator


class DlgLocalMemori(QDialog, Ui_DlgLocalMemori):
    def __init__(self, parent=None):
        super(DlgLocalMemori, self).__init__(parent)
        self.setupUi(self)
        self.events = [i for i in event_generator()]
        for i in self.events:
            item = QListWidgetItem(str(i[0].date_taken) + ' %d photos' % len(i))
            self.lst_memori.addItem(item)
        self.lst_memori.itemClicked.connect(self.on_lst_memori_item_clicked)
        self.lst_photos.itemClicked.connect(self.on_lst_photos_item_clicked)

    def on_lst_memori_item_clicked(self, item):
        self.lst_photos.clear()
        for i in self.events[self.lst_memori.indexFromItem(item).row()]:
            item = QListWidgetItem(i.root.path + i.path)
            self.lst_photos.addItem(item)

    def on_lst_photos_item_clicked(self, item):
        photo = self.events[self.lst_memori.currentRow()][self.lst_photos.indexFromItem(item).row()]
        im = Image.open(photo.root.path + photo.path)
        im.show()

if __name__=='__main__':
    import sys
    app = QApplication(sys.argv)
    form = DlgLocalMemori()
    form.show()
    app.exec_()
    
