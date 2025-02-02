# # Data Analysis for monthly gold prices
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Load CSV File
# data = pd.read_csv('Data-Monthly-2020-2025.csv')
#
# # Convert 'Date' to datetime, specifying the format
# data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')
#
#
# # Remove commas in price-related columns and convert to float
# cols_to_clean = ['Price', 'Open', 'High', 'Low']
# for col in cols_to_clean:
#     data[col] = data[col].str.replace(',', '').astype(float)
#
#
# # Convert 'Vol.' column: Replace 'K' with *1000 and 'M' with *1,000,000
# def convert_volume(value):
#     if isinstance(value, str):
#         if 'K' in value:
#             return float(value.replace('K', '')) * 1_000
#         elif 'M' in value:
#             return float(value.replace('M', '')) * 1_000_000
#     return float(value)
#
#
# data['Vol.'] = data['Vol.'].apply(convert_volume)
#
# # Remove '%' sign and convert to float in 'Change %' column
# data['Change %'] = data['Change %'].str.replace('%', '').astype(float)
#
# # Sort by Date (ascending)
# data = data.sort_values(by='Date')
#
# # Plot Gold Price Trend (Fixed)
# plt.figure(figsize=(12, 6))
# plt.plot(data['Date'], data['Price'], marker='o', linestyle='-', color='b', label='Close Price')
#
# # Set x-axis to display only yearly labels
# plt.xticks(pd.date_range(start='2020-02-01', end='2025-01-01', freq='YS'), rotation=45)
#
# # Set y-axis range
# plt.ylim(1900, 3000)  # Adjusted for higher values
#
# # Labels and title
# plt.title('Gold Price Trend (2024)')
# plt.xlabel('Year')
# plt.ylabel('Gold Price (USD)')
# plt.legend()
# plt.grid(True)
#
# # Show the plot
# plt.show()


# Data Analysis for daily prices year 2024
# cols_to_clean = ['Price', 'Open', 'High', 'Low']
# for col in cols_to_clean:
#     data[col] = data[col].str.replace(',', '', regex=True).astype(float)
#
# # Convert 'Vol.' column: Replace 'K' with *1000 and 'M' with *1,000,000
# def convert_volume(value):
#     if isinstance(value, str):
#         if 'K' in value:
#             return float(value.replace('K', '')) * 1_000
#         elif 'M' in value:
#             return float(value.replace('M', '')) * 1_000_000
#     return float(value)
#
# data['Vol.'] = data['Vol.'].apply(convert_volume)
#
# # Remove '%' sign and convert to float in 'Change %' column
# data['Change %'] = data['Change %'].str.replace('%', '', regex=True).astype(float)
#
# # Sort data by date (ascending)
# data = data.sort_values(by='Date')
#
# # Plot Daily Gold Price Trend
# plt.figure(figsize=(12, 6))
# plt.plot(data['Date'], data['Price'], marker='o', linestyle='-', color='b', label='Close Price')
#
# # Improve X-axis: Show labels at better intervals
# plt.xticks(pd.date_range(start=data['Date'].min(), end=data['Date'].max(), freq='MS'),
#            rotation=45)  # Show start of each month
#
# # Dynamically adjust Y-axis
# plt.ylim(data['Price'].min() - 50, data['Price'].max() + 50)
#
# # Labels and title
# plt.title('Gold Price Trend (Daily - 2024)')
# plt.xlabel('Date')
# plt.ylabel('Gold Price (USD)')
# plt.legend()
# plt.grid(True)
#
# # Show the plot
# plt.show()
