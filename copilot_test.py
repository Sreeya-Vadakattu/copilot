import os
import time

def get_system_uptime():
    if os.name == 'posix':
        # For Unix/Linux systems
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_string = str(time.strftime('%H:%M:%S', time.gmtime(uptime_seconds)))
            print(f"System uptime: {uptime_string}")
    elif os.name == 'nt':
        # For Windows systems
        import ctypes
        import sys
        import datetime

        # GetTickCount returns milliseconds since system started
        GetTickCount64 = ctypes.windll.kernel32.GetTickCount64
        GetTickCount64.restype = ctypes.c_ulonglong
        millis = GetTickCount64()
        uptime_seconds = millis / 1000.0
        uptime_string = str(datetime.timedelta(seconds=int(uptime_seconds)))
        print(f"System uptime: {uptime_string}")
    else:
        print("Unsupported OS")

if __name__ == "__main__":
    get_system_uptime()
