# Import necessary libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
from tabulate import tabulate

import matplotlib.pyplot as plt

# Load the trained model
try:
    model = joblib.load('pride_model.pkl')
    print("Model loaded successfully!")
except Exception as e:
    print("An error occurred while loading the model:", e)
    exit()

# Get inputs from the user
total_questions = int(input("Enter the total number of questions: "))
total_marks_scored = int(input("Enter the total marks scored: "))
total_time_taken = int(input("Enter the total time taken (in seconds): "))
total_max_time_allotted = int(input("Enter the total max time allotted (in seconds): "))
total_count_of_5_pointers = int(input("Enter the total count of 5 pointers: "))
max_percentage_conversion = float(input("Enter the max percentage conversion for total questions: "))

# Prepare input data for prediction
input_data = pd.DataFrame({
    'Total No of Questions': [total_questions],
    'Total Marks Scored': [total_marks_scored],
    'Total Time Taken': [total_time_taken],
    'Total Max Time Allotted': [total_max_time_allotted],
    'Total Count of 5 Pointers': [total_count_of_5_pointers],
    'Max Percentage Conversion for Total Questions': [max_percentage_conversion]
})

# Predict PRIDE Contribution %
predicted_pride_contribution = model.predict(input_data)

# Display the inputs and predicted PRIDE Contribution %
print("\nInputs:")
print("Total number of questions:", total_questions)
print("Total marks scored:", total_marks_scored)
print("Total time taken (seconds):", total_time_taken)
print("Total max time allotted (seconds):", total_max_time_allotted)
print("Total count of 5 pointers:", total_count_of_5_pointers)
print("Max percentage conversion for total questions:", max_percentage_conversion)

print("\nPredicted PRIDE Contribution %:")
# Convert the prediction to a DataFrame for display
predicted_data = pd.DataFrame(predicted_pride_contribution, columns=['Perceive Accuracy Score', 'Resolve Accuracy Score', 'Influence Accuracy Score', 'Deliver Accuracy Score', 'Engage Accuracy Score'])
print(tabulate(predicted_data, headers='keys', tablefmt='grid'))

import matplotlib.pyplot as plt

# Create subplots for each domain
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

# Plot for Perceive Accuracy Score
axs[0, 0].bar(predicted_data.columns, predicted_data.values[0], color='skyblue')
axs[0, 0].set_title('Perceive Accuracy Score')
axs[0, 0].set_ylabel('PRIDE Contribution %')
axs[0, 0].set_ylim(0, 100)
axs[0, 0].grid(axis='y', linestyle='--', alpha=0.7)

# Plot for Resolve Accuracy Score
axs[0, 1].bar(predicted_data.columns, predicted_data.values[0], color='lightgreen')
axs[0, 1].set_title('Resolve Accuracy Score')
axs[0, 1].set_ylim(0, 100)
axs[0, 1].grid(axis='y', linestyle='--', alpha=0.7)

# Plot for Influence Accuracy Score
axs[0, 2].bar(predicted_data.columns, predicted_data.values[0], color='salmon')
axs[0, 2].set_title('Influence Accuracy Score')
axs[0, 2].set_ylim(0, 100)
axs[0, 2].grid(axis='y', linestyle='--', alpha=0.7)

# Plot for Deliver Accuracy Score
axs[1, 0].bar(predicted_data.columns, predicted_data.values[0], color='gold')
axs[1, 0].set_title('Deliver Accuracy Score')
axs[1, 0].set_ylabel('PRIDE Contribution %')
axs[1, 0].set_xlabel('Domain')
axs[1, 0].set_ylim(0, 100)
axs[1, 0].grid(axis='y', linestyle='--', alpha=0.7)

# Plot for Engage Accuracy Score
axs[1, 1].bar(predicted_data.columns, predicted_data.values[0], color='plum')
axs[1, 1].set_title('Engage Accuracy Score')
axs[1, 1].set_xlabel('Domain')
axs[1, 1].set_ylim(0, 100)
axs[1, 1].grid(axis='y', linestyle='--', alpha=0.7)

# Hide the last subplot as we have only 5 domains
axs[1, 2].axis('off')

plt.tight_layout()
plt.show()
