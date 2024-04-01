import phonenumbers as ph
from phonenumbers import carrier, geocoder, timezone

number = "+919930050552"
number = ph.parse(number)

# Get time zones for the phone number
print(timezone.time_zones_for_number(number))

# Get the carrier name for the phone number
print(carrier.name_for_number(number, "en"))

# Get the geographical information for the phone number
print(geocoder.description_for_number(number, "en"))
