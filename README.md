# SHL Assessment Recommendation Engine

This is a simple content-based recommendation system built using Python and Flask. It helps users find relevant SHL assessments based on their input, leveraging SHL's product catalog.

## Features

- Search for assessments by typing a query (e.g., job role, skills).
- Recommends top relevant assessments.
- Clean and minimal UI (no external styling).

## Tech Stack

- Python
- Flask
- scikit-learn
- Pandas
- HTML 

# How to Run:

## Clone the repository ##
git clone https://github.com/k-nageswari/shl-assessment-recommendation-engine.git
cd shl-assessment-recommendation-engine

## Create and activate virtual environment
python -m venv venv
## On Windows:
venv\Scripts\activate
## Install dependencies
pip install -r requirements.txt
## Make sure 'shl_catalogue.csv' is in the project root
## Run the Flask app
python -m app.app
## Open in browser
http://127.0.0.1:5000

## 📷 Preview

### 🏠 Home Page
![Homepage png](https://github.com/user-attachments/assets/e04572e1-3ee1-4c09-adc0-f6ad2e6905e4)
### 📊 Results Page
![Resultpage png](https://github.com/user-attachments/assets/49b98ebc-d79d-457d-b80d-ad64ff90574d)


