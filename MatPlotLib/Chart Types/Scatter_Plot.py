#plt.scatter(x,y,color='color_name, marker='marker style', label='label name', s=size, linewidths=width)
'''
To find the Co-Relation between two variables, we use Scatter Plot. 
  eg. Advertising budget vs Sales, emperature vs Ice cream sales etc. 
  And we use scatter plot in machine learning for to visualize prediction values or actual values.
'''
                
import matplotlib.pyplot as plt

hours_studies = [1,2,3,4,5,6,7,8]
exam_scores = [50,55,60,65,70,75,80,85]

#scatter plot
plt.scatter(hours_studies, exam_scores, color='red', marker='^', label='Student Data', s=100, linewidths=3)
plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.title('Relationship between Study Tie and Exam Score')
plt.legend()
plt.grid(True)

plt.show()