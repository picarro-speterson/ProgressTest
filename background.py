from PyQt4 import QtCore
from dialog import Dialog

from time import sleep

def doBackgroundThing():
    Dialog.openProgressDialog("Doing the thing", "Cancel", 0, 10)

    for i in range(10):
        if not Dialog.checkProgressCanceled():
            sleep(1)
            Dialog.incrementProgressDialogValue()
            print i
            QtCore.QCoreApplication.processEvents()
