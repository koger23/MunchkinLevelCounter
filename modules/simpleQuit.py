from PySide2.QtWidgets import QMessageBox


class SimpleQuit(QMessageBox):

    def __init__(self):
        super(SimpleQuit, self).__init__()

