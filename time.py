import datetime
"""
    Simply takes a unix time stamp and returns human readable date and time 
"""

input_date = input('Timestamp to convert: ')

print(datetime.datetime.fromtimestamp(int(input_date)).strftime('%Y-%m-%d %H:%M:%S'))
