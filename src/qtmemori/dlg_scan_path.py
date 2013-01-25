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
        self.btn_add.clicked.connect(self.on_btn_add_clicked)
        self.btn_delete.clicked.connect(self.on_btn_delete_clicked)
        self.update_table()

    def on_btn_add_clicked(self):
        path = QFileDialog.getExistingDirectory(self, u'Select Scan Path')
        ScanPath.objects.get_or_create(path=path)
        self.update_table()

    def on_btn_delete_clicked(self):
        items = self.tbl_scan_path.selectedItems()
        for i in items[::2]:
            path = ScanPath.objects.get(path=i.text())
            path.delete()
        self.update_table()

    def update_table(self):
        for i in range(self.tbl_scan_path.rowCount()): 
            self.tbl_scan_path.removeRow(0)
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
