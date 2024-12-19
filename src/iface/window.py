from PySide6 import QtCore, QtWidgets, QtGui


class WindowWidget(QtWidgets.QWidget):
    def __init__(self):
        # The Qt application handler.
        self.handler = QtWidgets.QApplication([])

        super().__init__()

        self.wlayout = QtWidgets.QVBoxLayout(self)

        # The left pane contains the list of all medical devices.
        self.left_pane = QtWidgets.QFrame()
        self.wlayout.addWidget(self.left_pane)

        # The right pane contains the information about the selected
        # medical device.
        self.right_pane = QtWidgets.QFrame()
        self.wlayout.addWidget(self.right_pane)
        

    def display(self):
        return self.handler.exec()


Window = WindowWidget() 
