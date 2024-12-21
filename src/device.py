from datetime import datetime
from dateutil.relativedelta import relativedelta
from enum import Enum
from src.iface.window import *
from src.iface.styling.dynamic import*
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

        self.w_lpane, self.w_rpane = Window.createNewDevice()

        self.w_lpane.setDeviceType(self.device_type.value)
        self.w_lpane.setDeviceName(self.device_name)

        self.w_rpane.setDeviceType(self.device_type.value)
        self.w_rpane.setDeviceName(self.device_name)

        # Map the button of the device entry.
        self.w_lpane.connectDeviceButton(self.w_rpane.applyToStackedLayout)

    def setHealthScore(self, score):
        self.device_health_score = score
        self.w_rpane.setDeviceScore(self.device_health_score)

    def setServiceDate(self, date):
        self.device_service_date = date
        td = relativedelta(date, datetime.now())

        fmt_list = []

        if td.years == 1:
            fmt_list.append(f"{td.years} year")
        elif td.years > 1:
            fmt_list.append(f"{td.years} years")

        if td.months == 1:
            fmt_list.append(f"{td.months} month")
        elif td.months > 1:
            fmt_list.append(f"{td.months} months")

        if td.days == 1:
            fmt_list.append(f"{td.days} day")
        elif td.days > 1:
            fmt_list.append(f"{td.days} days")

        if fmt_list:
            fmt_str = "after " + ", ".join(fmt_list)
        else:
            fmt_str = "now"

        self.w_rpane.setDeviceServiceDate(fmt_str)

    def setServiceCost(self, cost):
        self.w_rpane.setDeviceServiceCost(f"\u20b9{cost}")

