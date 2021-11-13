import sys
import random
from typing import _SpecialForm
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QCursor, QPixmap
from PySide6.QtWidgets import QGridLayout, QLabel, QPushButton
from shiboken6.Shiboken import Object

class ArtHiest(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup()
    
    def setup(self):
        self.setWindowTitle("Art Hiest")
        grid = QGridLayout()

        # Logo Display
        logo = self.logo("arthiesttransp.png", "logo")
        grid.addWidget(logo, 0, 0)

        #button widget
        btn = self.btn("Browse", "btn")
        grid.addWidget(btn, 0, 1)
        
        grid.setRowStretch(1,1)

        self.setLayout(grid)
    
    # quick logo creation
    def logo(self, imagelink, objectname = ""):
        image = QPixmap(imagelink)
        image = image.scaledToHeight(100)
        logo = QLabel(objectname, objectName = objectname) if objectname else QLabel(objectname)
        logo.setPixmap(image)
        logo.setAlignment(QtCore.Qt.AlignCenter)
        return logo

    # quick button creation
    def btn(self, text, objectname = "None"):
        btn = QPushButton(text, ObjectName = objectname) if objectname else QPushButton(text)
        btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        return btn

    def label(self, text):
        label = QLabel(text)
        return label
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    stylesheet = "./style.css"
    #set the stylesheet
    with open(stylesheet, 'r') as fh:
        app.setStyleSheet(fh.read())

    widget = ArtHiest()
    # widget.resize(600, 500)
    widget.show()

    sys.exit(app.exec())