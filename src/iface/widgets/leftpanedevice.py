from PySide6.QtWidgets import QFrame, QLabel, QHBoxLayout, QPushButton, \
                               QSizePolicy, QVBoxLayout, QHBoxLayout, QIcon
from PySide6.QtGui import QPixmap

class LeftPaneDevice(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        self.wlayout = QHBoxLayout()
        self.setLayout(self.wlayout)

        self.devinfo_frame = QFrame(self)
        self.devinfo_layout = QVBoxLayout(self.devinfo_frame)
        self.wlayout.addWidget(self.devinfo_frame, 90)

        # Create a horizontal layout for button and image
        self.button_layout = QHBoxLayout()

        # Create the button
        self.view_button = QPushButton("→", self)

        # Set an image/icon for the button (example with an image file)
        icon = QIcon("path/to/your/image.png")  # Replace with the actual image path
        self.view_button.setIcon(icon)
        self.view_button.setIconSize(QSize(24, 24))  # Set the icon size as needed

        # Add the button to the layout
        self.button_layout.addWidget(self.view_button)

        # Optionally, you can add a QLabel with text or image next to the button
        self.button_label = QLabel("Click Here", self)
        self.button_layout.addWidget(self.button_label)

        # Add button layout to the main layout
        self.wlayout.addLayout(self.button_layout, 10)

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
