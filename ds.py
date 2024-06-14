import numpy as np
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

# Generate sample data for PRIDE proficiency scores
num_students = 100
pride_scores = np.random.uniform(0, 100, num_students)

# Generate sample data for other PRIDE features
feature1_scores = np.random.uniform(0, 100, num_students)
feature2_scores = np.random.uniform(0, 100, num_students)
feature3_scores = np.random.uniform(0, 100, num_students)

# Create a scatter plot for PRIDE proficiency vs other features
scatter_trace1 = go.Scatter(x=pride_scores, y=feature1_scores, mode='markers', name='Feature 1')
scatter_trace2 = go.Scatter(x=pride_scores, y=feature2_scores, mode='markers', name='Feature 2')
scatter_trace3 = go.Scatter(x=pride_scores, y=feature3_scores, mode='markers', name='Feature 3')

# Create histograms for PRIDE proficiency and other features
hist_trace1 = go.Histogram(x=pride_scores, name='PRIDE Proficiency', marker=dict(color='blue'))
hist_trace2 = go.Histogram(x=feature1_scores, name='Feature 1', marker=dict(color='orange'))
hist_trace3 = go.Histogram(x=feature2_scores, name='Feature 2', marker=dict(color='green'))
hist_trace4 = go.Histogram(x=feature3_scores, name='Feature 3', marker=dict(color='red'))

# Create subplots for scatter plots and histograms
fig = make_subplots(rows=2, cols=2, subplot_titles=('PRIDE Proficiency vs Features', 'PRIDE Proficiency Distribution', 'Feature 1 Distribution', 'Feature 2 Distribution', 'Feature 3 Distribution'))

fig.add_trace(scatter_trace1, row=1, col=1)
fig.add_trace(scatter_trace2, row=1, col=1)
fig.add_trace(scatter_trace3, row=1, col=1)
fig.add_trace(hist_trace1, row=1, col=2)
fig.add_trace(hist_trace2, row=2, col=1)
fig.add_trace(hist_trace3, row=2, col=2)
fig.add_trace(hist_trace4, row=2, col=2)

# Update layout
fig.update_layout(height=800, width=1000, title_text="PRIDE Proficiency Dashboard")

# Show dashboard
fig.show()
