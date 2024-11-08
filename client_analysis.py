import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('file_name.csv') #Enter CSV file name here.
df = df[df['Total bookings'] != 0]
# Count the number of unique values in the "Email" column
unique_emails = df['Email'].nunique()
average = df['Bookings value'].mean()

bookings_over_1 = df[df['Total bookings'] > 1].shape[0]
print(f"Number of entries with 'Total bookings' larger than 1: {bookings_over_1}")
print(f"Average Spending: {average}")
# Print the result
print(f"Number of unique emails: {unique_emails}")
