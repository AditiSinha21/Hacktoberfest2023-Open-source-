import pandas as pd
import matplotlib.pyplot as plt

# Load data from Excel into a DataFrame
data = pd.read_csv('data.csv')

# Assuming your Excel data has columns 'X' and 'Y'
x = data['X']
y = data['Y']

# Create a line plot
plt.plot(x, y)

# Add labels and a title
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.title('Graph from Excel Data')

# Display the graph
plt.show()
