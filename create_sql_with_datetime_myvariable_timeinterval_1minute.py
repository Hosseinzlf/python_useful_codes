# This code is developed by Hossein ZOLFAGHARI, 2024, France.

'''
Explanation of code:
Create a template SQL database including a table, datetime column in UTC with TIMESTAMP format, and my_variable column.
Datetime is filled with 1 minutes time interval and can be changed for whatever you want.
The my_variable is filled with 0 but cane be modified.
'''

import sqlite3
import random
import schedule
import time
from datetime import datetime, timedelta


# Connect to the SQLite database
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS main_table (
                    datetime_utc TIMESTAMP,
                    "my_variable" REAL
                  )''')

# Define start date and time
start_date = datetime(2024, 2, 6, 0, 0, 0)

# Define end date and time
end_date = start_date + timedelta(days=1)

# Insert rows into the table
current_date = start_date
while current_date < end_date:
    
    # Format the datetime string in UTC timezone
    formatted_datetime = current_date.strftime('%Y-%m-%d %H:%M:%S+00:00')
    
    # Insert a row with datetime and 0 value
    cursor.execute('''INSERT INTO main_table (datetime_utc, "my_variable")
                      VALUES (?, ?)''', (formatted_datetime, 0))
    
    # Move to the next minute
    current_date += timedelta(minutes=1)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database created successfully.")






