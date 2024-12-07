from datetime import datetime
from zoneinfo import ZoneInfo

def convert_to_timezone(date_str, target_timezone):
    """
    Converts a naive datetime string to a timezone-aware datetime object.

    :param date_str: A string representing the date and time in the format "YYYY-MM-DD HH:MM".
    :param target_timezone: A string representing the desired timezone (e.g., "Europe/Paris", "UTC").
    :return: A timezone-aware datetime object.
    """
    try:
        # Parse the datetime string
        naive_datetime = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        # Localize the datetime to the target timezone
        localized_datetime = naive_datetime.replace(tzinfo=ZoneInfo(target_timezone))
        return localized_datetime
    except Exception as e:
        print(f"Error in timezone conversion: {e}")
        return None
