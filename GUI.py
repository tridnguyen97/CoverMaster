
from PySide2.QtWidgets import QPushButton, QMainWindow, QWidget,QVBoxLayout, QHBoxLayout, QDesktopWidget, QFileDialog, QLineEdit

class cover_widget(QWidget):
    def __init__(self,parent=None):
        super(cover_widget,self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.hbox = QHBoxLayout(self)
        self.downloadBtn = QPushButton("Download")
        self.coverBtn = QPushButton("AddCover")

        self.selFile = QLineEdit(self)
        self.selFileBtn = QPushButton("browse",self)
        self.hbox.addWidget(self.selFile)
        self.hbox.addWidget(self.selFileBtn)

        self.layout.addLayout(self.hbox)
        self.layout.addWidget(self.downloadBtn)
        self.layout.addWidget(self.coverBtn)

        self.setLayout(self.layout)

        self.selFileBtn.clicked.connect(self.onSelectedFile)
        self.downloadBtn.clicked.connect(self.onPressDownloadBtn)
        self.coverBtn.clicked.connect(self.onPressCoverBtn)

    def onSelectedFile(self):
        self.selFile.setText(QFileDialog.getOpenFileName()[0])

    def onPressCoverBtn(self):
        pass

    def onPressDownloadBtn(self):
        pass


class main_window(QMainWindow):
    def __init__(self,parent=None):
        super(main_window,self).__init__(parent)
        self.main_widget = cover_widget(self)
        self.screen = QDesktopWidget().screenGeometry()
        self.setGeometry((self.screen.width()-450) / 2,(self.screen.height() - 300) / 2, 450, 300)

        self.setCentralWidget(self.main_widget)
