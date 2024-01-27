from datetime import datetime
import pytz

timezone_lookup = dict([(pytz.timezone(x).localize(datetime.now()).tzname(), x) for x in pytz.all_timezones])

print(timezone_lookup)