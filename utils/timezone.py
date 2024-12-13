from datetime import datetime  #import datetime for working with date and time objects
from zoneinfo import ZoneInfo  #import ZoneInfo for timezone handling
from data.storage import TIMEZONES  #import predefined list of valid timezones

def convert_to_timezone(date_str, timezone_str):
    """
    Converts a naive datetime string to a timezone-aware datetime object.

    :param date_str: A string representing the date and time in the format "YYYY-MM-DD HH:MM".
    :param timezone_str: A string representing the desired timezone (e.g., "UTC", "Europe/Paris").
    :return: A timezone-aware datetime object or None if there is an error.
    """
    try:
        if timezone_str not in TIMEZONES:  #validate if the provided timezone is in the list of valid timezones
            print("Invalid timezone. Please ensure the timezone is valid.")  #print an error message for invalid timezone
            return None  #return None if the timezone is invalid

        naive_datetime = datetime.strptime(date_str, "%Y-%m-%d %H:%M")  #parse the datetime string into a naive datetime object

        localized_datetime = naive_datetime.replace(tzinfo=ZoneInfo(timezone_str))  #convert the naive datetime to timezone-aware
        return localized_datetime  #return the timezone-aware datetime object
    except ValueError:  #catch errors in datetime parsing
        print("Invalid date format. Please enter the date in 'YYYY-MM-DD HH:MM' format.")  #print an error message for invalid date format
    except Exception as e:  #catch other unexpected errors
        print(f"Error in timezone conversion: {e}")  #print a generic error message
    return None  #return None if any exception occurs
