import os
import sys
import time
import platform
import subprocess
from datetime import datetime

def get_uptime_windows():
    try:
        # Use systeminfo to get the system boot time
        output = subprocess.check_output("systeminfo", shell=True, text=True, stderr=subprocess.DEVNULL)
        for line in output.splitlines():
            if "System Boot Time" in line or "Systemstartzeit" in line:  # German Windows too
                boot_time_str = line.split(":", 1)[1].strip()
                try:
                    # Try parsing with common formats
                    boot_time = datetime.strptime(boot_time_str, '%m/%d/%Y, %I:%M:%S %p')
                except ValueError:
                    try:
                        boot_time = datetime.strptime(boot_time_str, '%d.%m.%Y, %H:%M:%S')
                    except ValueError:
                        print("Could not parse boot time:", boot_time_str)
                        return
                now = datetime.now()
                uptime = now - boot_time
                print(f"System uptime: {str(uptime).split('.')[0]}")
                return
        print("Could not determine uptime from systeminfo output.")
    except Exception as e:
        print("Could not determine uptime on Windows.", e)

def get_uptime_linux():
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_string = str(time.strftime('%H:%M:%S', time.gmtime(uptime_seconds)))
            print(f"System uptime: {uptime_string}")
    except Exception as e:
        print("Could not determine uptime on Linux.", e)

def get_uptime_unix():
    try:
        output = subprocess.check_output("uptime", shell=True, text=True)
        print("System uptime:", output.strip())
    except Exception as e:
        print("Could not determine uptime with 'uptime' command.", e)

def get_system_uptime():
    system = platform.system()
    if system == "Windows":
        get_uptime_windows()
    elif system == "Linux":
        get_uptime_linux()
    else:
        get_uptime_unix()

if __name__ == "__main__":
    get_system_uptime()
