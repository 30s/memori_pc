import os
import sys

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
        for i in event_generator():
            item = QListWidgetItem(str(i[0].date_taken) + ' %d photos' % len(i))
            self.lst_memori.addItem(item)


if __name__=='__main__':
    import sys
    app = QApplication(sys.argv)
    form = DlgLocalMemori()
    form.show()
    app.exec_()
    
