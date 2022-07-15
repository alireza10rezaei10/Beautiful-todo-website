from persiantools.jdatetime import JalaliDateTime
import pytz
from json import dumps

def Today():
    today = JalaliDateTime.now(pytz.timezone('Asia/tehran'))
    t = today.ctime().split(' ')
    today = {
        'title': t[0],
        'hour': int(t[4].split(':')[0]),
        'day': int(t[1]),
        'month': t[2],
        'year': int(t[3])
    }
    return dumps(today)
