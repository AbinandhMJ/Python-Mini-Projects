import os
import platform
import time

def shutdown_PC():
    system_platform = platform.system().lower()

    if system_platform == "windows":
        print("Your System will shutdown in 60 Seconds")
        os.system("shutdown /s /t 1")
    elif system_platform == "linux" or system_platform == "darwin":
        print("Your System will shutdown in 60 Seconds")
        time.sleep(60)  # Wait for 60 seconds
        os.system("shutdown now")
    else:
        print("Unsupported operating system")

shutdown_PC()
