import subprocess

def get_system_uptime():
    try:
        result = subprocess.run(["uptime", "-p"], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error retrieving uptime: {e}"

print("System Uptime:", get_system_uptime())
