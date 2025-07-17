#multi scatter plot
#plt.scatter(x,y,color='color_name, marker='marker style', label='label name', s=size, linewidths=width)
import matplotlib.pyplot as plt

plt.scatter([1,2,3], [50,55,60], color='blue', label='class A') # group 1
plt.scatter([1,2,3], [45,50,52], color='orange', label='class B') # group 2

plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.title('Comparison of two classes')
plt.legend()
plt.grid(True)

plt.show()