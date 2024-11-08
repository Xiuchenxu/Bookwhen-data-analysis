import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd

# Get the directory of the current script file
directory = os.path.dirname(os.path.abspath(__file__))

# Read the specific CSV file
filepath = os.path.join(directory, 'Filename.csv') #Enter csv file name here
df = pd.read_csv(filepath)


# Convert Event starts and Booking completed to datetime with timezone info
df['Event starts'] = pd.to_datetime(df['Event starts'], utc=True)
df['Booking completed'] = pd.to_datetime(df['Booking completed'], utc=True)

# Filter the DataFrame for dates between August 1st and August 3rd
start_date = pd.to_datetime('2024-05-01 17:00:00', utc=True)
end_date = pd.to_datetime('2024-07-03 23:00:00', utc=True)

mask = (df['Event starts'] >= start_date) & (df['Event starts'] <= end_date)
df = df[mask]

# Calculate the difference between Booking completed and Event starts
df['Booking completed'] = df['Booking completed'] - df['Event starts']
df['Booking completed'] = df['Booking completed'].apply(
    lambda x: x.total_seconds() / 86400)

 # Set the index to Booking completed
df.set_index('Booking completed', inplace=True)

  # Plot
plt.figure(figsize=(12, 6))
for class_name, group in df.groupby('Event title'):
        plt.plot(group.index, range(1, len(group) + 1),
                 marker='o', linestyle='-', label=class_name)

plt.title('Dance Class Bookings Over Time')
plt.xlabel('Booking Date')
plt.ylabel('Booking Index')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()
