import os
import platform
import subprocess
import sys
import time
from datetime import datetime

def uptime_linux():
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
        print("System uptime:", time.strftime('%H:%M:%S', time.gmtime(uptime_seconds)))
    except Exception as e:
        print("Linux uptime failed:", e)

def uptime_windows():
    try:
        # Try systeminfo
        output = subprocess.check_output("systeminfo", shell=True, text=True, stderr=subprocess.DEVNULL)
        for line in output.splitlines():
            if "System Boot Time" in line or "Systemstartzeit" in line:  # English or German
                boot_time_str = line.split(":", 1)[1].strip()
                try:
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
        print("Windows uptime failed:", e)

def uptime_macos():
    try:
        output = subprocess.check_output(['sysctl', '-n', 'kern.boottime'], text=True)
        boot_time_str = output.strip().split('=')[1].split(',')[0].strip()
        boot_time = datetime.fromtimestamp(int(boot_time_str))
        now = datetime.now()
        uptime = now - boot_time
        print(f"System uptime: {str(uptime).split('.')[0]}")
    except Exception as e:
        print("macOS uptime failed:", e)

def uptime_fallback():
    try:
        output = subprocess.check_output("uptime", shell=True, text=True)
        print("System uptime:", output.strip())
    except Exception as e:
        print("Generic uptime failed:", e)

def main():
    system = platform.system()
    if system == "Linux":
        uptime_linux()
    elif system == "Windows":
        uptime_windows()
    elif system == "Darwin":
        uptime_macos()
    else:
        uptime_fallback()

if __name__ == "__main__":
    main()
