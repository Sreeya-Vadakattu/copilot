import os
import platform

def print_system_uptime():
    if platform.system() == "Windows":
        # On Windows, use 'net stats srv'
        try:
            output = os.popen('net stats srv').read()
            for line in output.split('\n'):
                if "Statistics since" in line:
                    print(f"System uptime info: {line}")
                    return
            print("Could not determine uptime on Windows.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        # On Unix/Linux/macOS, use 'uptime -p'
        try:
            output = os.popen('uptime -p').read().strip()
            print(f"System uptime: {output}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    print_system_uptime()
