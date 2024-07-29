from datetime import datetime

now = datetime.now()

year = now.strftime("%Y")

month = now.strftime("%m")

day = now.strftime("%d")

time = now.strftime("%H:%M:%S")

dateTime = now.strftime("29/07/2024, 15:41:12")

print("date and time:",dateTime)


