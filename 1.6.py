###
# Returns the name of the day of the week for a given day number (1-Monday ... 7-Sunday)
#
# Function to return the name of the day of the week for a given day number (1-Monday, 7-Sunday)
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n - 1]  # Odejmuje jeden zeby sie dopasowac do indeksu


print(weekday(1))  # Monday
print(weekday(4))  # Thursday
print(weekday(7))  # Sunday


