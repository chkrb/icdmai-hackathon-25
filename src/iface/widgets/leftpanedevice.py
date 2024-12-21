from PySide6.QtWidgets import QFrame, QLabel, QHBoxLayout, QPushButton, \
                               QSizePolicy, QVBoxLayout

class LeftPaneDevice(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        self.l_base = QHBoxLayout(self)

        self.initUiEntry()

    def initUiEntry(self):
        dev_layout = QVBoxLayout()

        devname_label = QLabel(self)
        devtype_label = QLabel(self)
        dev_button = QPushButton("→", self)

        dev_layout.addWidget(devname_label)
        dev_layout.addWidget(devtype_label)

        self.l_base.addLayout(dev_layout, 90)
        self.l_base.addWidget(dev_button, 10)

        # These widgets are important.
        self.w_device_name = devname_label
        self.w_device_type = devtype_label
        self.w_device_open = dev_button
        self.w_device_name.setObjectName("lpane-device-name")
        self.w_device_type.setObjectName("lpane-device-type")
        self.w_device_open.setObjectName("lpane-device-open")

    def setDeviceName(self, name):
        self.w_device_name.setText(name)

    def setDeviceType(self, type):
        self.w_device_type.setText(type)

    def connectDeviceButton(self, slot):
        self.w_device_open.clicked.connect(slot)
