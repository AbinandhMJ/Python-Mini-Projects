import wifi
import subprocess
import sys
import platform

def scan_wifi():
    print("Scanning in progress...")
    # Scan for available WiFi networks
    cells = wifi.Cell.all('wlan0')

    # Print the details of each WiFi network
    for i, cell in enumerate(cells):
        print(f"Network {i + 1}:")
        print(f"  SSID: {cell.ssid}")
        print(f"  Signal Strength: {cell.signal}")
        print(f"  Quality: {cell.quality}")
        print(f"  Frequency: {cell.frequency} MHz")
        print(f"  Bitrates: {cell.bitrates}")
        print(f"  Encryption Type: {cell.encryption_type}")
        print("-" * 30)

def main():
    # Check the operating system
    if platform.system().lower() == 'linux':
        # Prompt the user for sudo access
        sudo_response = input("Do you want to run with sudo access? (yes/no): ").lower()
        if sudo_response == "yes":
            # Run the script with sudo
            subprocess.run(["sudo", "python3", __file__])
            sys.exit(0)  # Exit the script after running with sudo
        elif sudo_response != "no":
            print("Invalid response. Please enter 'yes' or 'no'.")
            sys.exit(1)  # Exit with an error code for invalid response

    # Run WiFi scanning without sudo
    scan_wifi()

if __name__ == "__main__":
    main()
