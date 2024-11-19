import os
import platform
import sys

bash = "pip"
cmd = f"{bash} install platform"
while True:
    try:
        os.system(cmd)
        break
    except:
        bash = "pip3"

os_name = platform.system()
if os_name == "Darwin":
    os_type = "macos"
elif os_name == "Windows":
    os_type = "windows"
elif os_name == "Linux":
    os_type = "linux"

if os_type == "macos" or os_type == "linux":
    script_path = os.path.expanduser("~/Desktop/PacketBanBypasser_by_AGB/main.py")
elif os_type == "windows":
    script_path = r"C:\Users\%USERNAME%\Desktop\PacketBanBypasser_by_AGB\main.py"

if os_type == "macos" or os_type == "linux":
    os.system(f"sudo python3 {script_path}")
elif os_type == "windows":
    os.system(f'runas /user:Administrator "python {script_path}"')
