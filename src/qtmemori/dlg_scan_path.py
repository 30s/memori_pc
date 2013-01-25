import os
import sys

from PySide.QtCore import *
from PySide.QtGui import *

from ui_dlg_scan_path import Ui_DlgScanPath

DIR_NAME = os.path.dirname(os.path.abspath(__file__))

sys.path.append(DIR_NAME + '/../djmemori')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djmemori.settings")

from djmemori.models import ScanPath


class DlgScanPath(QDialog, Ui_DlgScanPath):
    def __init__(self, parent=None):
        super(DlgScanPath, self).__init__(parent)
        self.setupUi(self)
        paths = ScanPath.objects.all()
        self.tbl_scan_path.setRowCount(len(paths))
        for idx, i in enumerate(paths):
            item_path = QTableWidgetItem(i.path)
            self.tbl_scan_path.setItem(idx, 0, item_path)
            item_cnt = QTableWidgetItem("%d" % i.photo_set.count())
            self.tbl_scan_path.setItem(idx, 1, item_cnt)
        self.tbl_scan_path.resizeColumnsToContents()


if __name__=='__main__':
    app = QApplication(sys.argv)
    form = DlgScanPath()
    form.show()
    app.exec_()
