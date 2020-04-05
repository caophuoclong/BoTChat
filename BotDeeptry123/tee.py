import datetime
import pytz
from dateutil.parser import parse

# Dạng string time
date_string = '2019-03-20T03:41:16Z'

# Dạng datetime format
date_time_python = parse(date_string)
print(date_time_python)