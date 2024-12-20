from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QFrame, QHBoxLayout, QScrollArea, \
                              QStackedLayout, QVBoxLayout, QWidget
from src.iface.widgets.leftpanedevice import *
from src.iface.widgets.rightpanestats import *


class WindowWidget(QWidget):
    def __init__(self):
        # The Qt application handler.
        self.handler = QApplication([])

        super().__init__()

        with open("src/iface/qss/main.qss") as qss:
            self.setStyleSheet(qss.read())

        self.wlayout = QHBoxLayout(self)

        # The left pane contains the list of all medical devices.
        self.lpane_frame = QFrame(self)
        self.lpane_frame.setObjectName("left-pane")
        self.lpane_layout = QHBoxLayout(self.lpane_frame)
        self.wlayout.addWidget(self.lpane_frame, 30)

        # A scrollable area for the left pane.
        self.lpane_scr = QScrollArea(self.lpane_frame)
        self.lpane_layout.addWidget(self.lpane_scr)
        self.lpane_scr_frame = QFrame(self.lpane_scr)
        self.lpane_scr.setWidget(self.lpane_scr_frame)
        self.lpane_scr_layout = QVBoxLayout(self.lpane_scr_frame)
        self.lpane_scr.setWidgetResizable(True)

        # The right pane contains the information about the selected
        # medical device.
        self.rpane_frame = QFrame(self)
        self.rpane_frame.setObjectName("right-pane")
        self.rpane_layout = QStackedLayout(self.rpane_frame)
        self.wlayout.addWidget(self.rpane_frame, 70)

        # This is the default view (acting as a placeholder) of the right pane.
        self.rpane_label = QLabel("<h1>Select a device in the left pane to view its information.</h1>",
                                  self.rpane_frame)
        self.rpane_label.setObjectName("rpane-placeholder")
        self.rpane_label.setAlignment(Qt.AlignCenter)
        self.rpane_label.setWordWrap(True)
        self.rpane_layout.addWidget(self.rpane_label)

    def display(self):
        return self.handler.exec()


Window = WindowWidget()
