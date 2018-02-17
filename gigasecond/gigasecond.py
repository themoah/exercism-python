import time
from datetime import datetime

def add_gigasecond(args):
    dateToParse = args
    convertedToSeconds = time.mktime(dateToParse.timetuple())
    convertedToSeconds += 1000000000
    newDateTime = datetime.fromtimestamp(convertedToSeconds)
    return newDateTime

