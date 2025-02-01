import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('Daily-gold-data-10years.csv')


plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Price'], label='Close Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Gold Price Over Time')
plt.legend()
plt.show()
