from datetime import datetime
from zoneinfo import ZoneInfo
from data.storage import TIMEZONES


def convert_to_timezone(date_str, timezone_index):
    """
    Converts a naive datetime string to a timezone-aware datetime object.

    :param date_str: A string representing the date and time in the format "YYYY-MM-DD HH:MM".
    :param timezone_index: The index of the desired timezone from the TIMEZONES list (1-based index).
    :return: A timezone-aware datetime object.
    """
    try:
        # Get the timezone string from the index
        target_timezone = TIMEZONES[timezone_index - 1]

        # Parse the datetime string
        naive_datetime = datetime.strptime(date_str, "%Y-%m-%d %H:%M")

        # Localize the datetime to the target timezone
        localized_datetime = naive_datetime.replace(tzinfo=ZoneInfo(target_timezone))
        return localized_datetime
    except IndexError:
        print("Invalid timezone index. Please choose a valid timezone.")
    except Exception as e:
        print(f"Error in timezone conversion: {e}")
    return None
