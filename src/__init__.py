from src.device import *
from src.iface.window import *

def main():
    # This is purely for testing purposes, please remove it before
    # production.
    Device(DeviceType.BloodGlucoseMonitor, "BGLUCO-1")
    Device(DeviceType.BloodGlucoseMonitor, "BGLUCO-2")
    Device(DeviceType.BloodGlucoseMonitor, "BGLUCO-3")

    Device(DeviceType.BloodPressureMonitor, "SPHYGM-1")
    Device(DeviceType.BloodPressureMonitor, "SPHYGM-2")
    Device(DeviceType.BloodPressureMonitor, "SPHYGM-3")
    Device(DeviceType.BloodPressureMonitor, "SPHYGM-4")

    Device(DeviceType.CTScanner, "CTSCAN-1")

    Device(DeviceType.MRIMachine, "MRIMAC-1")
    Device(DeviceType.MRIMachine, "MRIMAC-2")

    Window.showFullScreen()
    return Window.display()
