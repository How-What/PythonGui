import sys
import time
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QCursor, QPixmap
from PySide6.QtWidgets import QFileDialog, QGridLayout, QLabel, QLineEdit, QProgressBar, QPushButton
from PySide6.QtCore import QObject, QThread, QTimer, Slot, Signal
from hiest import Hiest

class Worker (QThread):
    change_value = Signal(QPixmap)
    changed = Signal(int)
    complete = Signal(str)
    
    def run(self):
        i = 0
        images = ['./test/Mon, 19 Nov 2018 15-52-39 GMT','./test/Mon, 19 Nov 2018 16-42-47 GMT','./test/Fri, 05 Nov 2021 04-06-43 GMT','./test/Tue, 20 Nov 2018 13-36-15 GMT','./test/Wed, 10 Nov 2021 01-54-57 GMT']
        for image in images:
            i += 20
            img = QPixmap(image)
            img = img.scaledToHeight(100)
            img = img.scaledToWidth(50)
            time.sleep(2)
            print(i)
            self.change_value.emit(img)
            self.changed.emit(i)

class ArtHiest(QtWidgets.QWidget):
    widgets = {
        'folder_path_textbox': None,
        'user_id': None,
        'progress_bar':None,
        'progress_label': None
    }
    def __init__(self):
        super().__init__()
        self.setup()
    
    def setup(self):
        self.setWindowTitle("Art Hiest")
        self.resize(600,500)
        self.grid = QGridLayout()

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
        download_gallery_btn.clicked.connect(self.start_hiest)
        download_gallery_btn.setFixedWidth(250)

        # Text box
        folder_path_textbox = self.textbox()
        self.widgets['folder_path_textbox'] = folder_path_textbox

        userid_textbox = self.textbox()
        self.widgets['user_id'] = userid_textbox
        
        # Progress stuff
        pgbar = QProgressBar()
        self.widgets['progress_bar'] = pgbar
        progress_label = self.label('Extracted {0}'.format(""))
        self.widgets['progress_label'] = progress_label
        #add the widgets on screen
        #Column 1
        self.grid.addWidget(logo, 0, 0, 6, 1)
        self.grid.addWidget(download_gallery_btn, 6, 0, 1, 2, QtCore.Qt.AlignCenter)
        # self.grid.addWidget(self.widgets['progress_label'], 7, 0)
        
        #column2
        self.grid.addWidget(step1_label, 0,1)
        self.grid.addWidget(userid_textbox, 1, 1)
        self.grid.addWidget(step2_label, 2,1)
        self.grid.addWidget(browse, 3, 1)
        self.grid.addWidget(folder_path_textbox, 4, 1)
        self.grid.addWidget(step3_label, 5,1)
        self.grid.addWidget(pgbar,7, 1)

        # grid streching
        self.grid.setRowStretch(8, 1)
        self.grid.setColumnStretch(3,1)
        self.setLayout(self.grid)

    #Button Events:
    @Slot()
    def open_file_explorer(self):
        file_dialog = QFileDialog()
        self.widgets['folder_path_textbox'].setText(str(file_dialog.getExistingDirectory(self, 'Select output Directroy')))
        print(self.widgets['folder_path_textbox'].text())
    
    @Slot()
    def start_hiest(self):
        # self.widgets['progress_label'].setParent(None)
        # worker = Worker(parent = self)
        # worker.change_value.connect(self.change_label)
        # worker.changed.connect(self.set_progressval)
        # worker.start()
        # worker.finished.connect(self.add)
        # worker.finished.connect(self.evt_worker_finished)
        # worker.change_value.connect(self.set_progressval)
        userid = self.widgets['user_id'].text()
        output_path = self.widgets['folder_path_textbox'].text()
        heister = Hiest(userid, output_path, self.widgets['progress_bar'], self.widgets['progress_label'])
        print(heister.fullpath())

        heister.extract_and_download()

    def change_label(self, msg):
        self.displayimage = QLabel()
        self.displayimage.setPixmap(msg)
        
        self.grid.addWidget(self.displayimage, 7 , 0, 1, 2)

    def set_progressval(self, val):
        self.widgets['progress_bar'].setValue(val)

    def add(self):
        self.grid.addWidget(self.widgets['progress_label'], 7, 0)

    def imagedisplay(self,images):
        for image in images:
            print(image)
            img = QPixmap(image)
            img = img.scaledToHeight(50)
            self.widgets['progress_label'].setPixmap(img)
            self.widgets['progress_label'].adjustSize()
            time.sleep(10)

    # Builder Functions
    def logo(self, imagelink, objectname = ""):
        image = QPixmap(imagelink)
        image = image.scaledToHeight(100)
        logo = QLabel(objectname, objectName = objectname)
        if objectname:
            logo.setObjectName(objectname)
        logo.setPixmap(image)
        logo.setAlignment(QtCore.Qt.AlignCenter)
        return logo

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