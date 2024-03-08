
# Spam Detection Project

This project is aimed at building a spam detection system using Python, Jupyter Lab, Django, and popular Python libraries such as Pandas, Scikit-learn, and Joblib.

## Overview

Spam detection is a vital component in various applications such as email filtering, message classification, and social media content moderation. This project utilizes machine learning techniques to classify messages as spam or not spam.

## Requirements

To run this project, you need to have the following installed:

- Python (3.6 or higher)
- Jupyter Lab
- Django
- Python libraries: Pandas, Scikit-learn, Joblib

## Installation

1. Clone this repository to your local machine
2. Install the required Python packages:
```
pip install -r requirements.txt
```

## Usage

### Jupyter Lab

1. Open the file  'data/train_model.ipynb'.
2. Follow the instructions to train the model and perform spam detection.

### Django Web Application

1. Navigate to the root directory of the app.
2. Run the Django server.
```
python manage.py runserver
```
3. Open your web browser and go to "http://localhost:8000/" to access the spam detection web application.


## Files
- `core/`: Django application model for spam detection.
- `data/`: Sample dataset for training and testing the spam detection model and pre-trained machine learning models saved using Joblib.
- `requirements.txt`: List of Python dependencies required for the project.
 
 

## Contributors:
- Abinash Parajuli
- Kushal Ghimire
- Sudesh Acharya