result = divmod(13, 4)
print(result)  # Output: (3, 1)  (13 // 4 = 3, 13 % 4 = 1)

#convert second to minutes and seconds
total_seconds = 135
minutes, seconds = divmod(total_seconds, 60)
print(f"{total_seconds} seconds is equal to {minutes} minutes and {seconds} seconds")

#format  time durations
import datetime

start_time = datetime.datetime(2023, 1, 1, 10, 0, 0)  
end_time = datetime.datetime(2023, 1, 1, 12, 30, 15)  

duration = end_time - start_time
total_seconds = duration.total_seconds()

hours, remainder = divmod(total_seconds, 3600)
minutes, seconds = divmod(remainder, 60)

print(f"Duration: {hours} hours, {minutes} minutes, {seconds} seconds")
