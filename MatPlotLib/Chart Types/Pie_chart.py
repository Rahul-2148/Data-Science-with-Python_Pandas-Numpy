# Pie chart 
# plt.pie(values, labels= label_list, colors= color_list, autopct= '%1.1f%%', startangle=angle, counterclock=direction, radius=radius, center=center, wedgeprops=wedge_properties, textprops=text_properties)
 # startangle=90 means start from 90 degree

import matplotlib.pyplot as plt

regions = ['East', 'West', 'North', 'South']
revenue = [3000, 2000, 1500, 1000]

plt.pie(revenue, labels=regions, autopct='%1.1f%%', colors=['gold', 'skyblue', 'lightgreen', 'coral'])

plt.title('Reenue Contribution by Region')

plt.show()