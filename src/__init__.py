from datetime import datetime
from src.device import *
from src.iface.window import *

def main():
    # This is purely for testing purposes, please remove it before
    # production.
    dev11 = Device(DeviceType.BloodGlucoseMonitor, "BGLUCO-1")
    dev11.setHealthScore(10)
    dev11.setServiceDate(datetime.strptime("2025/07/24", "%Y/%m/%d"))
    dev11.setServiceCost(1000)
    dev12 = Device(DeviceType.BloodGlucoseMonitor, "BGLUCO-2")
    dev12.setHealthScore(7)
    dev12.setServiceDate(datetime.strptime("2026/03/01", "%Y/%m/%d"))
    dev12.setServiceCost(800)
    dev13 = Device(DeviceType.BloodGlucoseMonitor, "BGLUCO-3")
    dev13.setHealthScore(8)
    dev13.setServiceDate(datetime.strptime("2024/12/12", "%Y/%m/%d"))
    dev13.setServiceCost(3200)

    dev21 = Device(DeviceType.BloodPressureMonitor, "SPHYGM-1")
    dev21.setHealthScore(2)
    dev21.setServiceDate(datetime.strptime("2025/07/24", "%Y/%m/%d"))
    dev21.setServiceCost(5520)
    dev22 = Device(DeviceType.BloodPressureMonitor, "SPHYGM-2")
    dev22.setHealthScore(5)
    dev22.setServiceDate(datetime.strptime("2025/01/13", "%Y/%m/%d"))
    dev22.setServiceCost(2300)
    dev23 = Device(DeviceType.BloodPressureMonitor, "SPHYGM-3")
    dev23.setHealthScore(9)
    dev23.setServiceDate(datetime.strptime("2025/08/30", "%Y/%m/%d"))
    dev23.setServiceCost(7500)
    dev24 = Device(DeviceType.BloodPressureMonitor, "SPHYGM-4")
    dev24.setHealthScore(9)
    dev24.setServiceDate(datetime.strptime("2025/12/12", "%Y/%m/%d"))
    dev24.setServiceCost(2010)

    dev31 = Device(DeviceType.CTScanner, "CTSCAN-1")
    dev31.setHealthScore(8)
    dev31.setServiceDate(datetime.strptime("2025/07/09", "%Y/%m/%d"))
    dev31.setServiceCost(3420)

    dev41 = Device(DeviceType.MRIMachine, "MRIMAC-1")
    dev41.setHealthScore(1)
    dev41.setServiceDate(datetime.strptime("2025/09/07", "%Y/%m/%d"))
    dev41.setServiceCost(1130)
    dev42 = Device(DeviceType.MRIMachine, "MRIMAC-2")
    dev42.setHealthScore(7)
    dev42.setServiceDate(datetime.strptime("2025/12/17", "%Y/%m/%d"))
    dev42.setServiceCost(1640)

    Window.showFullScreen()
    return Window.displayWindow()
