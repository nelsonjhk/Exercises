import time

"""
Prints current time in hh:mm:sec and days since epoch
"""

day = 60 * 60 * 24

current = int(time.time())
daysSince = current // day
current = current % day
hours = current // (60*60)
minutes = (current % (60*60))//60
seconds = current % 60
print("The time is now ", hours, ":", minutes, ":", seconds, " and it has been ", daysSince, " days since the epoch." )
