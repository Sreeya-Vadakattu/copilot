import subprocess
import platform

def get_uptime():
    try:
        if platform.system() == "Windows":
            result = subprocess.run(["net", "statistics", "workstation"], capture_output=True, text=True, check=True)
            for line in result.stdout.splitlines():
                if "Statistics since" in line:
                    print("System Uptime:", line)
                    break
        else:
            result = subprocess.run(["uptime"], capture_output=True, text=True, check=True)
            print("System Uptime:", result.stdout.strip())
    except Exception as e:
        print("Error getting uptime:", e)

if __name__ == "__main__":
    get_uptime()
