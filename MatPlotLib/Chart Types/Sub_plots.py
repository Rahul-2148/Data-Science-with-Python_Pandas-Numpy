'''
it is beneficial in:
1- when comparing muiple charts side by side 
2- space is more efficient
3- it is used in EDA (Explorated Data Analysis), ML (Machine Learning) models comparison me, weekly sales analysis etc.

In subplot, indexing is 1 based , (not zero based)
'''
# plt.subplot(nrows, ncols, index) 

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,25]

plt.subplot(1,2,1) # 1 row, 2 column, 1st subplot
plt.plot(x, y)
plt.title('Line Chart')

plt.subplot(1,2,2) # 1 row, 2 column, 2nd subplot
plt.bar(x, y)
plt.title('Bar Chart')

plt.tight_layout()

plt.show()