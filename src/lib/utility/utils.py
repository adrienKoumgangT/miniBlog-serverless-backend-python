import datetime
import time
import uuid
from json import JSONEncoder

import pytz


# subclass JSONEncoder
class MyJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return str(o)
        return o.__dict__


class TimeUtils(object):

    @staticmethod
    def get_current_time_ms():
        """
        Get the current time in milliseconds.
        """
        return int(time.time() * 1000)

    @staticmethod
    def convert_ms_to_utc(ms):
        """
        Convert time in milliseconds to UTC time.
        """
        utc_datetime = datetime.datetime.utcfromtimestamp(ms / 1000.0)
        return utc_datetime

    @staticmethod
    def get_current_datetime_iso_8601_format():
        # Get the current date and time
        current_datetime = datetime.datetime.utcnow()  # Get the current UTC date and time

        # Format the date and time according to the specified format
        formatted_datetime = current_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')

        return formatted_datetime

    @staticmethod
    def convert_formatted_datetime_iso_8601_to_datetime(formatted_datetime: str):
        # Convert the string to a datetime object
        converted_datetime = datetime.datetime.strptime(formatted_datetime, '%Y-%m-%dT%H:%M:%SZ')

        return converted_datetime

    @staticmethod
    def convert_formatted_datetime_iso_8601_to_local_datetime(formatted_datetime: str):
        # Convert the string to a datetime object
        utc_datetime = datetime.datetime.strptime(formatted_datetime, '%Y-%m-%dT%H:%M:%SZ')

        # Get the local timezone from the system
        local_timezone = datetime.datetime.now(pytz.utc).astimezone().tzinfo

        # Convert UTC datetime to local timezone
        local_datetime = utc_datetime.astimezone(local_timezone)

        return local_datetime


class IdentifiantUtils(object):
    @staticmethod
    def get_unique_id():
        t = time.time()
        id4 = uuid.uuid4()
        my_id = str(int(t)) + '-' + str(t).split('.')[1] + '-' + str(id4)
        return my_id


def test_time_utils():
    # Example usage
    current_time_ms = TimeUtils.get_current_time_ms()
    print("Current time in milliseconds:", current_time_ms)

    utc_time = TimeUtils.convert_ms_to_utc(current_time_ms)
    print("UTC time:", utc_time)


if __name__ == '__main__':
    # test_time_utils()

    t = TimeUtils.get_current_datetime_iso_8601_format()
    print(t)
    tt = TimeUtils.convert_formatted_datetime_iso_8601_to_datetime(t)
    print(tt)
    ttt = TimeUtils.convert_formatted_datetime_iso_8601_to_local_datetime(t)
    print(ttt)
