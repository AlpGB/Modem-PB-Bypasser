import os
import sys
import subprocess
import platform

SERVER_IP = '0.0.0.0'
SERVER_PORT = 61937
PYTHON_VERSION = "3.12.2"
REQUIRED_MODULES = ["scapy", "cryptography"]

def install_python():
    os_name = platform.system()
    try:
        if os_name == "Windows":
            python_installer = "https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe"
            subprocess.run(["curl", "-O", python_installer], check=True)
            subprocess.run(["python-3.12.2-amd64.exe", "/quiet", "InstallAllUsers=1", "PrependPath=1"], check=True)
        elif os_name == "Darwin":
            subprocess.run(["brew", "install", f"python@{PYTHON_VERSION}"], check=True)
            subprocess.run(["brew", "link", "--force", f"python@{PYTHON_VERSION}"], check=True)
        elif os_name == "Linux":
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", f"python{PYTHON_VERSION}", "-y"], check=True)
    except subprocess.CalledProcessError as e:
        print("Python installation failed:", e)

def install_modules():
    for module in REQUIRED_MODULES:
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", module], check=True)
        except subprocess.CalledProcessError:
            subprocess.run([sys.executable, "-m", "pip3", "install", module], check=True)

def set_python_default():
    os_name = platform.system()
    if os_name == "Windows":
        subprocess.run(["setx", "PATH", f"%PATH%;C:\\Python{PYTHON_VERSION}\\python.exe"], check=True)
    elif os_name == "Darwin":
        subprocess.run(["ln", "-sf", f"/usr/local/bin/python{PYTHON_VERSION}", "/usr/local/bin/python"], check=True)
    elif os_name == "Linux":
        subprocess.run(["sudo", "update-alternatives", "--install", "/usr/bin/python3", "python3", f"/usr/bin/python{PYTHON_VERSION}", "1"], check=True)

def main():
    os_name = platform.system()
    try:
        python_version = subprocess.check_output(["python3", "--version"]).decode()
        if PYTHON_VERSION not in python_version:
            install_python()
            set_python_default()
    except Exception:
        install_python()
        set_python_default()
    install_modules()
    print(f"Setup complete. Client can now connect to server at {SERVER_IP}:{SERVER_PORT}")

if __name__ == "__main__":
    main()
