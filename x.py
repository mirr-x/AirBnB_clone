from datetime import datetime

# Your input string
input_string = '2024-02-07T21:33:25.062671'

# Define the format of your input string
date_format = '%Y-%m-%dT%H:%M:%S.%f'

# Use strptime to parse the string into a datetime object
parsed_datetime = datetime.strptime(input_string, date_format)

# Print the datetime object using its __repr__ format
print(repr(parsed_datetime))
# Output: datetime.datetime(2024, 2, 7, 21, 33, 25, 62671)
