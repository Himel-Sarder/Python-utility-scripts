import speedtest

def check_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1e+6  # Convert from bits to megabits
    upload_speed = st.upload() / 1e+6  # Convert from bits to megabits
    ping = st.results.ping

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")

# Example usage:
check_internet_speed()
