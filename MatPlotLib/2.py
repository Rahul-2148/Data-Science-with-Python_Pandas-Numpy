import matplotlib.pyplot as plt

x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] # x-axis labels
y = [10, 15, 7, 20, 12] # y-axis values

plt.plot(x, y) #creating line graph
# plt.bar(x, y) #creating bar graph
# plt.scatter(x, y) #creating scatter graph
# plt.pie(y) #creating pie chart

plt.title('Bakery Sales This Week!')

plt.xlabel('Day of the week')
plt.ylabel('Sales Per Day (in ₹)')

plt.show()
