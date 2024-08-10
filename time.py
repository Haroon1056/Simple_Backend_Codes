from datetime import datetime
import pytz

# define the Uk timezone
uk_timezone = pytz.timezone("Europe/London")

#Get the current time in the UK

uk_time = datetime.now(uk_timezone)
format_uk_time = uk_time.strftime("%y-%m-%d %H-%M-%S")

print(f"Current UK Time: {format_uk_time}")