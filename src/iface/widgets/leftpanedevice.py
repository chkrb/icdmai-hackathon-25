from PySide6.QtWidgets import QFrame, QLabel, QPushButton, QHBoxLayout, \
                              QVBoxLayout, QSizePolicy


class LeftPaneDevice(QFrame):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        self.wlayout = QHBoxLayout()
        self.setLayout(self.wlayout)

        self.devinfo_frame = QFrame(self)
        self.devinfo_layout = QVBoxLayout(self.devinfo_frame)
        self.wlayout.addWidget(self.devinfo_frame, 90)

        self.view_button = QPushButton("→", self)
        self.wlayout.addWidget(self.view_button, 10)

        self.devname_label = QLabel(self.devinfo_frame)
        self.devname_label.setObjectName("device-name")
        self.devinfo_layout.addWidget(self.devname_label)

        self.devtype_label = QLabel(self.devinfo_frame)
        self.devtype_label.setObjectName("device-type")
        self.devinfo_layout.addWidget(self.devtype_label)

    def setDeviceName(self, name):
        self.devname_label.setText(name)

    def setDeviceType(self, type):
        self.devtype_label.setText(type)
