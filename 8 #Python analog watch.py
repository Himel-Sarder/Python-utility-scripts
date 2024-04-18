from datetime import datetime

def show_current_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current Time:", current_time)

# Example usage:
show_current_time()
