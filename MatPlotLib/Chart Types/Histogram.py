# Histogram -> Shows the distribution of continuous data using bars.
# plt.hist(data, bins= number_of_bins, color= 'color_name', edgecolor='edge_color', linewidth=width, label='label_name', density=True, cumulative=True, bottom=value, histtype='bar', align='left', orientation='vertical', rwidth=0.9, log=False, normed=False)
# Height of Bar = number of students in each score range

import matplotlib.pyplot as plt

scores = [45, 67, 89, 56, 78, 88, 92, 60, 74, 81, 59, 66, 75, 82, 90, 85, 70, 73, 68, 77]

plt.hist(scores, bins=5, color='purple', edgecolor='black', linewidth=2, label='Scores')
plt.xlabel('Score Range')
plt.ylabel('Number of Students')
plt.title('Score Distribution of Students')
plt.legend()
plt.show()

#output
# Score Distribution of Students - Histogram


