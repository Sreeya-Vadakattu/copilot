import os
import sys
import time
import platform
import subprocess

def get_system_uptime():
    try:
        if os.name == 'posix':
            # Linux/Unix/Mac
            if os.path.exists('/proc/uptime'):
                with open('/proc/uptime', 'r') as f:
                    uptime_seconds = float(f.readline().split()[0])
                    uptime_string = str(time.strftime('%H:%M:%S', time.gmtime(uptime_seconds)))
                    print(f"System uptime: {uptime_string}")
            else:
                # macOS or other Unix
                output = subprocess.check_output("uptime", shell=True).decode()
                print("System uptime:", output.strip())
        elif os.name == 'nt':
            # Windows (works in Git Bash, Command Prompt, and PowerShell)
            try:
                output = subprocess.check_output("net stats workstation", shell=True).decode(errors='ignore')
                for line in output.splitlines():
                    if "Statistics since" in line:
                        print(f"System uptime since: {line.split('since')[1].strip()}")
                        break
                else:
                    print("Could not determine uptime on Windows.")
            except Exception as e:
                print("Could not determine uptime on Windows.", e)
        else:
            print("Unsupported OS")
    except Exception as e:
        print("Error determining uptime:", e)

if __name__ == "__main__":
    get_system_uptime()
