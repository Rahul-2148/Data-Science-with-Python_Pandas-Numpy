# plt.plot(x, y, color='color name', linestyle='line_style', linewidth=width, marker='marker symbol', label='label name', markersize=size)
# plt.xlabel('text') -> x-axis label
# plt.ylabel('text') -> y-axis label

import matplotlib.pyplot as plt

months = [1, 2, 3, 4]
sales = [1000, 1500, 1200, 1800]

plt.plot(months, sales, color='blue', linestyle='--', linewidth=2, marker='o', label='2025 Sales Data', markersize=10)
plt.title('Monthly Sales Data Report')
plt.xlabel('Month')
plt.ylabel('Sales Per Month')
plt.legend(loc='upper left', fontsize=12) # show legend means show label #upper left means top left corner #lower right means bottom right corner
plt.grid(color='gray', linestyle=':', linewidth=1) # show grid means show lines in chart
plt.xlim(1, 4) # limit the x-axis
plt.ylim(0, 2000) # limit the y-axis
plt.xticks([1,2,3,4], ['M1', 'M2', 'M3', 'M4']) # label the x-axis

plt.show() # show the plot