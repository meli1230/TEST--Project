from datetime import datetime
import pytz

def convert_to_timezone(date_str, target_timezone):
    try:
        naive_datetime = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        local_timezone = pytz.timezone(target_timezone)
        return local_timezone.localize(naive_datetime)
    except Exception as e:
        print(f"Error in timezone conversion: {e}")
        return None
