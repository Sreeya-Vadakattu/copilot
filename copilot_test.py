import os
import platform
import time

def get_system_uptime():
    system = platform.system()
    if system == "Windows":
        try:
            import ctypes
            from ctypes import wintypes

            class SYSTEM_TIME(ctypes.Structure):
                _fields_ = [
                    ("wYear", wintypes.WORD),
                    ("wMonth", wintypes.WORD),
                    ("wDayOfWeek", wintypes.WORD),
                    ("wDay", wintypes.WORD),
                    ("wHour", wintypes.WORD),
                    ("wMinute", wintypes.WORD),
                    ("wSecond", wintypes.WORD),
                    ("wMilliseconds", wintypes.WORD),
                ]

            class FILETIME(ctypes.Structure):
                _fields_ = [
                    ("dwLowDateTime", wintypes.DWORD),
                    ("dwHighDateTime", wintypes.DWORD),
                ]

            GetTickCount64 = getattr(ctypes.windll.kernel32, 'GetTickCount64', None)
            if GetTickCount64:
                GetTickCount64.restype = ctypes.c_ulonglong
                uptime_millis = GetTickCount64()
            else:
                GetTickCount = ctypes.windll.kernel32.GetTickCount
                GetTickCount.restype = ctypes.c_uint32
                uptime_millis = GetTickCount()

            uptime_seconds = int(uptime_millis // 1000)
            hours, remainder = divmod(uptime_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            print(f"System uptime: {hours:02}:{minutes:02}:{seconds:02}")
        except Exception as e:
            print("Could not determine uptime on Windows.", e)
    elif system == "Linux":
        try:
            with open('/proc/uptime', 'r') as f:
                uptime_seconds = float(f.readline().split()[0])
                hours, remainder = divmod(int(uptime_seconds), 3600)
                minutes, seconds = divmod(remainder, 60)
                print(f"System uptime: {hours:02}:{minutes:02}:{seconds:02}")
        except Exception as e:
            print("Could not determine uptime on Linux.", e)
    else:
        print("Unsupported OS")

if __name__ == "__main__":
    get_system_uptime()
