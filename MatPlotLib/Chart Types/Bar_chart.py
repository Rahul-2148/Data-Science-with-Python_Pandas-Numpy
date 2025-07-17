# Bar chart 
# plt.bar(x, height, color= 'color name', width = value, label='label name', bottom = value)

import matplotlib.pyplot as plt

product = ['A', 'B', 'C', 'D', 'E']
sales = [1000, 1500, 1200, 1800, 2000]

plt.bar(product, sales, color='orange', width=0.5, label='Sales 2025')

plt.xlabel('Product')
plt.ylabel('Sales')
plt.title('Product Sales Comparison 2025')
plt.legend()

plt.show()