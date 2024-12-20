from enum import Enum
from src.iface.window import *
from src.iface.widgets.leftpanedevice import *
from src.iface.widgets.rightpanestats import *


class DeviceType(Enum):
    BloodPressureMonitor = "Blood Pressure Monitor"
    BloodGlucoseMonitor = "Blood Glucose Monitor"
    CTScanner = "Computer Tomographer"
    MRIMachine = "Magnetic Resonance Imager"


class Device:
    def __init__(self, type, name):
        self.device_name = name
        self.device_type = type
        self.device_health_score = 0
        self.device_service_date = None

        self.w_lpane = LeftPaneDevice(Window.lpane_scr_frame)
        Window.lpane_scr_layout.addWidget(self.w_lpane)

        self.w_lpane.setDeviceType(self.device_type.value)
        self.w_lpane.setDeviceName(self.device_name)

        self.w_rpane = RightPaneStats(Window.rpane_frame)
        Window.rpane_layout.addWidget(self.w_rpane)

        self.w_rpane.setDeviceType(self.device_type.value)
        self.w_rpane.setDeviceName(self.device_name)
        self.w_rpane.setDeviceScore(10) # PLACEHOLDER
        self.w_rpane.setDeviceService("6 months") # PLACEHOLDER

        # Map the button of the device entry.
        self.w_lpane.view_button.clicked.connect(
            self.w_rpane.applyToStackedLayout)
