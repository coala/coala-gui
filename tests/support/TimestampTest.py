import datetime
import sys
import unittest

sys.path.insert(0, ".")
from source.support.Timestamp import timestamp_diff
from coalib.misc.i18n import _


class TimestampTest(unittest.TestCase):
    def test_process_timestamp(self):
        reference_timestamp = datetime.datetime(
            2015, 7, 3, 20, 30, 0).timetuple()
        self.assertEqual(_("Just Now"), timestamp_diff(reference_timestamp,
                                                       reference_timestamp))
        timestamp = datetime.datetime(2014, 7, 1, 0, 0, 0).timetuple()
        self.assertEqual("2014", timestamp_diff(timestamp,
                                                reference_timestamp))
        timestamp = datetime.datetime(2015, 7, 1, 0, 0, 0).timetuple()
        self.assertEqual(_("Wednesday"),
                         timestamp_diff(timestamp, reference_timestamp))
        timestamp = datetime.datetime(2015, 6, 1, 0, 0, 0).timetuple()
        self.assertEqual(_("June"), timestamp_diff(timestamp,
                                                   reference_timestamp))
        timestamp = datetime.datetime(2015, 7, 3, 15, 0, 0).timetuple()
        self.assertEqual(_("5 hours ago"), timestamp_diff(
            timestamp, reference_timestamp))
        timestamp = datetime.datetime(2015, 7, 3, 20, 29, 0).timetuple()
        self.assertEqual(_("A minute ago"),
                         timestamp_diff(timestamp, reference_timestamp))
        timestamp = datetime.datetime(2015, 7, 3, 20, 0, 0).timetuple()
        self.assertEqual(_("30 minutes ago"),
                         timestamp_diff(timestamp, reference_timestamp))
        timestamp = datetime.datetime(2015, 7, 2, 0, 0, 0).timetuple()
        self.assertEqual(_("Yesterday"),
                         timestamp_diff(timestamp, reference_timestamp))
        timestamp = datetime.datetime(2015, 7, 3, 0, 0, 0).timetuple()
        self.assertEqual(_("Today"),
                         timestamp_diff(timestamp, reference_timestamp))
        timestamp = datetime.datetime(2015, 6, 23, 0, 0, 0).timetuple()
        self.assertEqual(_("1 week ago"),
                         timestamp_diff(timestamp, reference_timestamp))


if __name__ == '__main__':
    unittest.main(verbosity=2)
