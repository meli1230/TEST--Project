users = [] #list to store information about users
appointments = [] #list to store scheduled appointments
consultants = ["Consultant A", "Consultant B", "Consultant C"] #predefines list of consultants available for appointments
# Predefined available slots for consultants
available_slots = {
    "Consultant A": ["2024-12-14 10:00", "2024-12-14 11:00", "2024-12-14 14:00"],
    "Consultant B": ["2024-12-15 09:00", "2024-12-15 13:00", "2024-12-15 15:00"],
    "Consultant C": ["2024-12-16 08:00", "2024-12-16 12:00", "2024-12-16 16:00"],
}


#list of supported time zones for scheduling appointments
#timezones
TIMEZONES = [
    "UTC",  #standard time zone
    "Pacific/Midway", #UTC-11
    "America/Adak", #UTC-10
    "America/Anchorage", #UTC-9
    "America/Los_Angeles",# UTC-8
    "America/Denver", #UTC-7
    "America/Chicago", #UTC-6
    "America/New_York", #UTC-5
    "America/Caracas", #UTC-4
    "America/Sao_Paulo", #UTC-3
    "Atlantic/Azores", #UTC-11
    "Europe/London", #UTC
    "Europe/Paris", #UTC+1
    "Europe/Istanbul", #UTC+2
    "Europe/Moscow", #UTC+3
    "Asia/Dubai", #UTC+4
    "Asia/Karachi", #UTC+5
    "Asia/Kolkata", #UTC+5:30
    "Asia/Bangkok", #UTC+7
    "Asia/Shanghai", #UTC+8
    "Asia/Tokyo", #UTC+9
    "Australia/Sydney", #UTC+10
    "Pacific/Noumea", #UTC+11
    "Pacific/Auckland" #UTC+12
]