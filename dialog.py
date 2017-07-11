from PyQt4 import QtGui, QtCore

# _Dialog should not be accessible to the outside world. Instead, just import
# the instance Dialog and use it as a singleton.

class _Dialog:
    # Opens progress dialog as its own window
    def openProgressDialog(self, text, cancelText, minimum, maximum):
        self.dialog = QtGui.QProgressDialog(text, cancelText, minimum, maximum)
        self.dialog.setWindowTitle("Progress")
        self.dialogVal = 0
        self.dialog.setValue(self.dialogVal)
        self.dialog.show()

    # Direct set progress
    def setProgressDialogValue(self, val):
        self.dialog.setValue(val)

    # Increment progress by 1 and finish if necessary
    def incrementProgressDialogValue(self):
        if self.dialog:
            self.dialogVal = self.dialogVal + 1
            self.dialog.setValue(self.dialogVal)
            if self.dialogVal >= self.dialog.maximum:
                self.finishProgressDialog()

    # Finish dialog and clean up
    def finishProgressDialog(self):
        self.dialog.reset()
        self.dialog.deleteLater()
        self.dialog = None
        self.dialogVal = None

    # Check if the dialog was canceled
    def checkProgressCanceled(self):
        return self.dialog.wasCanceled()

Dialog = _Dialog()
