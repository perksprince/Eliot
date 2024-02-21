import datetime
import pytz

# Get the timezone for the Philippines
ph_timezone = pytz.timezone("Asia/Manila")

# Get the current datetime in the Philippine timezone
ph_datetime = datetime.datetime.now(ph_timezone)

# Format the time output nicely
ph_time = ph_datetime.strftime("%H:%M:%S %p %Z")  

print("Current time in the Philippines:", ph_time)
