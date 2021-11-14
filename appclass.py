import sys
import random
from tkinter import Label
from typing import _SpecialForm
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QCursor, QPixmap
from PySide6.QtWidgets import QFileDialog, QGridLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Slot
from shiboken6.Shiboken import Object

class ArtHiest(QtWidgets.QWidget):
    widgets = {
        'folder_path_textbox': None, 
    }
    def __init__(self):
        super().__init__()
        self.setup()
    
    def setup(self):
        self.setWindowTitle("Art Hiest")
        self.resize(500,400)
        grid = QGridLayout()

        #Step Labels
        step1_label = self.label("Step 1: enter your user id")
        step2_label = self.label("Step 2: Select Where you want to store the art")
        step3_label = self.label("Step 3: Get Hiesting")
        
        # Logo Display
        logo = self.logo("arthiesttransp.png", "logo")
        
        #button widgets
        #browse
        browse = self.btn("Browse", "browse")
        browse.setFixedWidth(125)
        browse.clicked.connect(self.open_file_explorer)
        #Hiest
        download_gallery_btn = self.btn("Download Gallery")
        download_gallery_btn.setFixedWidth(250)

        # Add Text box
        folder_path_textbox = self.textbox()
        self.widgets['folder_path_textbox'] = folder_path_textbox

        userid_textbox = self.textbox()
        
        #add the widgets on screen
        #Column 1
        grid.addWidget(logo, 0, 0, 6, 1)
        #column2
        grid.addWidget(step1_label, 0,1)
        grid.addWidget(userid_textbox, 1, 1)
        grid.addWidget(step2_label, 2,1)
        grid.addWidget(browse, 3, 1)
        grid.addWidget(self.widgets['folder_path_textbox'], 4, 1)
        grid.addWidget(step3_label, 5,1)
        grid.addWidget(download_gallery_btn, 6, 0, 1, 2, QtCore.Qt.AlignCenter)
        

        # grid streching
        grid.setRowStretch(7, 1)
        grid.setColumnStretch(3,1)
        self.setLayout(grid)

        

    #Button Events:
    @Slot()
    def open_file_explorer(self):
        file_dialog = QFileDialog()
        self.widgets['folder_path_textbox'].setText(str(file_dialog.getExistingDirectory(self, 'Select output Directroy')))

    # Builder Functions
    # quick logo creation
    def logo(self, imagelink, objectname = ""):
        image = QPixmap(imagelink)
        image = image.scaledToHeight(100)
        logo = QLabel(objectname, objectName = objectname)
        if objectname:
            logo.setObjectName(objectname)
        logo.setPixmap(image)
        logo.setAlignment(QtCore.Qt.AlignCenter)
        return logo

    # quick button creation
    def btn(self, text, objectname = "None"):
        btn = QPushButton(text)
        if objectname:
            btn.setObjectName(objectname)
        btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        return btn

    def label(self, text):
        label = QLabel(text)
        label.setWordWrap(True)
        return label
    
    def textbox(self):
        textbox = QLineEdit(self, objectName = 'textBox')
        textbox.setFixedWidth(300)
        return textbox

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