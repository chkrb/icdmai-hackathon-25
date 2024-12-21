import os
from PySide6.QtCore import Qt
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QApplication, QFrame, QHBoxLayout, QScrollArea, \
                              QStackedLayout, QVBoxLayout, QWidget
from src.iface.widgets.leftpanedevice import *
from src.iface.widgets.rightpanestats import *


class WindowWidget(QWidget):
    def __init__(self):
        # The Qt application handler.
        self.handler = QApplication([])

        super().__init__()

        # Load all fonts.
        for fontfile in os.listdir("res/fonts/"):
            QFontDatabase.addApplicationFont(f"res/fonts/{fontfile}")

        # Load the stylesheet.
        with open("src/iface/styling/main.qss") as qss:
            self.setStyleSheet(qss.read())

        # The primary layout of the base widget.
        self.wlayout = QHBoxLayout(self)

        # Initialize sub-widgets.
        self.initUiLeftPane()
        self.initUiRightPane()

    def initUiLeftPane(self):
        # A scrollable area for the left pane.
        self.lpane_scr = QScrollArea(self)
        self.lpane_scr.setWidgetResizable(True)
        self.wlayout.addWidget(self.lpane_scr, 25)

        self.lpane_frame = QFrame(self.lpane_scr)
        self.lpane_frame.setObjectName("left-pane")
        self.lpane_scr.setWidget(self.lpane_frame)
        self.lpane_layout = QVBoxLayout(self.lpane_frame)

    def initUiRightPane(self):
        # The right pane contains the information about the selected
        # medical device.
        self.rpane_frame = QFrame(self)
        self.rpane_frame.setObjectName("right-pane")
        self.rpane_layout = QStackedLayout(self.rpane_frame)
        self.wlayout.addWidget(self.rpane_frame, 75)

        # This is the default view (acting as a placeholder) of the right pane.
        self.rpane_label = QLabel("<h1>Select a device in the left pane to view its information.</h1>",
                                  self.rpane_frame)
        self.rpane_label.setObjectName("rpane-placeholder")
        self.rpane_label.setAlignment(Qt.AlignCenter)
        self.rpane_label.setWordWrap(True)
        self.rpane_layout.addWidget(self.rpane_label)

    def createNewDevice(self):
        lpane = LeftPaneDevice(self)
        rpane = RightPaneStats(self)
        self.lpane_layout.addWidget(lpane)
        self.rpane_layout.addWidget(rpane)

        return lpane, rpane

    def displayWindow(self):
        return self.handler.exec()


Window = WindowWidget()
