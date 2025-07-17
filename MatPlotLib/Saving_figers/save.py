#DPI -> controls the resolution of the image
#BBOX_INCHES -> controls the size of the image # tight -> it is cropped or removed white spaces from the image
# # savefig('filename.extention', dpi= value, bbox_inches='tight')

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,25]

# create plot
plt.plot(x, y, color='blue', marker= 'o')

plt.title('Simple Line Plot')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

# save plot
plt.savefig('MatPlotLib/Saving_figers/line_plot.png', dpi=300, bbox_inches='tight') 
plt.show() # it is optional, agar dekhna hai toh use karo nhi toh save toh ho hi rha h.
