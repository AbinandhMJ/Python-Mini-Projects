import socket

def get_ip_address():
    try:
        # Get the local machine's IP address
        ip_address = socket.gethostbyname(socket.gethostname())

        # Format the IP address
        split_address = ip_address.split(".")
        separator = "[.]"
        formatted_ip = separator.join(split_address)

        return formatted_ip
    except socket.error as e:
        print("Error:", e)
        return None

formatted_ip_address = get_ip_address()

if formatted_ip_address:
    print("Your New address is:", formatted_ip_address)
else:
    print("Unable to fetch IP address.")
