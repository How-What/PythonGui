import sys
import random
from typing import _SpecialForm
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QCursor, QPixmap
from PySide6.QtWidgets import QGridLayout, QLabel, QPushButton

class ArtHiest(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup()
    
    def setup(self):
        self.setWindowTitle("Art Hiest")
        grid = QGridLayout()

        # Logo Display
        image = QPixmap("arthiesttransp.png")
        logo = QLabel( objectName = 'logo')
        logo.setPixmap(image)
        logo.setAlignment(QtCore.Qt.AlignCenter)
        grid.addWidget(logo, 1, 0)

        #button widget
        btn = QPushButton("Button", objectName="btn")
        btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        grid.addWidget(btn, 2, 0)

        
        self.setLayout(grid)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    stylesheet = "./style.css"
    #set the stylesheet
    with open(stylesheet, 'r') as fh:
        app.setStyleSheet(fh.read())

    widget = ArtHiest()
    widget.resize(600, 500)
    widget.show()

    sys.exit(app.exec())