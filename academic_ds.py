import numpy as np
import matplotlib.pyplot as plt

# Generate sample data for PRIDE proficiency scores and academic performance
num_students = 100
pride_scores = np.random.uniform(0, 100, num_students)
academic_performance = np.random.uniform(0, 100, num_students)

# Scatter plot to visualize the correlation
plt.figure(figsize=(8, 6))
plt.scatter(pride_scores, academic_performance, color='blue', alpha=0.5)
plt.title('Correlation between PRIDE Proficiency and Academic Performance')
plt.xlabel('PRIDE Proficiency Scores')
plt.ylabel('Academic Performance')
plt.grid(True)
plt.show()
