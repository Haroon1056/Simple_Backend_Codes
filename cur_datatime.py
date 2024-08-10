import time
from datetime import datetime

current_datetime = datetime.now()

format_datetime = current_datetime.strftime("%y-%m-%d %H-%M-%S")
print(f"Current Date and Time: {format_datetime}")

# 10-second countdown
print("Starting 10-second countdown...")
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)   #wait for 1 second

print("Countdown Complete!")

