import speedtest
def format_speed(speed):
    if speed >= 10**6:  # Convert to Mbps
        return f"{speed / 10**6:.2f} Mbps"
    elif speed >= 10**3:  # Convert to Kbps
        return f"{speed / 10**3:.2f} Kbps"
    else:  # Convert to bps
        return f"{speed:.2f} bps"

st = speedtest.Speedtest()
option = int(input('''What Speed you want to test:
1) Download Speed
2) Upload Speed
3) Ping
Your Choice: '''))

if option == 1:
    print("Stay back, we're getting your download speed...")
    download_speed = st.download()
    print(f"Download Speed: {format_speed(download_speed)}")
elif option == 2:
    print("Stay back, we're getting your upload speed...")
    upload_speed = st.upload()
    print(f"Upload Speed: {format_speed(upload_speed)}")
elif option == 3:
    servernames = []
    st.get_servers(servernames)
    print("Stay back, we're getting your ping...")
    ping = st.results.ping
    print(f"Ping: {ping:.2f} ms")
else:
    print("Please enter a correct choice!")
