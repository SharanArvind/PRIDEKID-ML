# PRIDEKID ML Recommendation System

## Overview

This repository contains the machine learning models and scripts used in the PRIDEKID project for content recommendation. The system is designed to suggest relevant content to users based on their preferences and interactions.

## Repository Structure

- `academic_ds.py`: Data processing and handling for academic datasets.
- `ds.py`: General dataset utilities and functions.
- `ml.py`: Core machine learning model implementations.
- `pride_model.pkl`: Serialized machine learning model used for recommendations.
- `pridekid.py`: Main script for integrating the recommendation system with the PRIDEKID platform.
- `prototype.py`: Prototype implementations and testing scripts.
- `sentiment.py`: Sentiment analysis module for understanding user feedback.
- `suggestion_gemini.py`: Recommendation engine using the Gemini algorithm.
- `suggestion_openai.py`: Recommendation engine leveraging OpenAI models.
- `youtube.py`: Module for integrating YouTube content into recommendations.
- `SVA Group Assessment Growth Reporting.xlsx`: Data report used for analysis and model training.

## Getting Started

### Prerequisites

Ensure you have Python 3.6+ installed along with the necessary libraries:

```sh
pip install -r requirements.txt
```

### Running the Project

1. Clone the repository:
   ```sh
   git clone https://github.com/SharanArvind/PRIDEKID-ML_recommendation.git
   cd PRIDEKID-ML_recommendation
   ```

2. Train the model (if not using the pre-trained model):
   ```sh
   python ml.py
   ```

3. Run the main application:
   ```sh
   python pridekid.py
   ```

