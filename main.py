from PyQt4 import QtGui, QtCore
import sys

from window import Window
from background import doBackgroundThing

def main():
    # Enable X11 not being awful
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_X11InitThreads)

    app = QtGui.QApplication(sys.argv)

    # Initialize components
    window = Window()
    window.button.clicked.connect(doBackgroundThing)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
