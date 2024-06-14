# Import necessary libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Fixed inputs for training the model
total_questions = 90
total_marks_scored = 363
total_time_taken = 2893
total_max_time_allotted = 2700
total_count_of_5_pointers = 63
max_percentage_conversion = 1.111111111

# Define PRIDE Contribution % for each domain (target variable)
pride_contribution = {
    'Perceive Accuracy Score': [11],
    'Resolve Accuracy Score': [13],
    'Influence Accuracy Score': [1],
    'Deliver Accuracy Score': [7],
    'Engage Accuracy Score': [12]
}

# Convert data to DataFrame
data = pd.DataFrame({
    'Total No of Questions': [total_questions],
    'Total Marks Scored': [total_marks_scored],
    'Total Time Taken': [total_time_taken],
    'Total Max Time Allotted': [total_max_time_allotted],
    'Total Count of 5 Pointers': [total_count_of_5_pointers],
    'Max Percentage Conversion for Total Questions': [max_percentage_conversion],
    **pride_contribution
})

# Define features (input) and target variable (output)
X = data[['Total No of Questions', 'Total Marks Scored', 'Total Time Taken', 'Total Max Time Allotted', 'Total Count of 5 Pointers', 'Max Percentage Conversion for Total Questions']]
y = data.drop(['Total No of Questions', 'Total Marks Scored', 'Total Time Taken', 'Total Max Time Allotted', 'Total Count of 5 Pointers', 'Max Percentage Conversion for Total Questions'], axis=1)

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the trained model
try:
    joblib.dump(model, 'pride_model.pkl')
    print("Model trained and saved successfully!")
except Exception as e:
    print("An error occurred while saving the model:", e)

