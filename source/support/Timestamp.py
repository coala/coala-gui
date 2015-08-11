import time
import datetime
from gettext import ngettext


def timestamp_diff(timestamp, reference_time):
    """
    Takes as input the timestamp and outputs a text representing the time
    difference of the timestamp from a reference_time.

    :param timestamp:      Timestamp for which difference is calculated.
    :param reference_time: Reference time for difference to be calculated.
    """
    timediff = time.mktime(reference_time)-time.mktime(timestamp)
    d = datetime.timedelta(seconds=timediff)
    total_secs = d.total_seconds()
    if total_secs < 60:
        return "Just Now"
    elif total_secs < 3600:
        minutes = d.seconds // 60
        return ngettext("A minute ago", "{minutes} minutes ago",
                        minutes).format(minutes=minutes)
    elif total_secs <= 43200:
        hours = d.seconds // 3600
        return ngettext("An hour ago",
                        "{hours} hours ago",
                        hours).format(hours=hours)
    elif d.days == 0:
        return "Today"
    elif d.days == 1:
        return "Yesterday"
    elif total_secs // 3600 < 7 * 24 - reference_time.tm_hour:
        return time.strftime("%A", timestamp)
    elif d.days < 14:
        return "1 week ago"
    elif d.days <= reference_time.tm_yday:
        return time.strftime("%B", timestamp)
    else:
        return time.strftime("%Y", timestamp)
