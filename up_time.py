from uptime import uptime
from datetime import timedelta


def get_uptime():
    uptime_seconds = uptime()
    uptime_string = str(timedelta(seconds = uptime_seconds))
    print('uptime= ' + uptime_string)
    return uptime_string