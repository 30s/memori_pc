from PySide.QtCore import *
from PySide.QtGui import *

from ui_dlg_local_memori import Ui_DlgLocalMemori


class DlgLocalMemori(QDialog, Ui_DlgLocalMemori):
    def __init__(self, parent=None):
        super(DlgLocalMemori, self).__init__(parent)
        self.setupUi(self)


if __name__=='__main__':
    import sys
    app = QApplication(sys.argv)
    form = DlgLocalMemori()
    form.show()
    app.exec_()
    
