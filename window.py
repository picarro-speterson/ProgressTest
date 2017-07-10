from PyQt4 import QtGui

class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):
        self.layout = QtGui.QVBoxLayout(self)
        self.button = QtGui.QPushButton("Push to start")
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

        self.show()
