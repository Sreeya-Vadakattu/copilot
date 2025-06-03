# GitHub Copilot Test - System Uptime Script

## Task Overview
This script prints the system uptime using a Linux command. The initial script was generated using **GitHub Copilot on GitHub.com** by typing a comment in a new Python file.

## Copilot's Suggested Code
```python
import os

# Get the system uptime
uptime = os.popen('uptime -p').read()

# Print the system uptime
print("System Uptime: " + uptime)
