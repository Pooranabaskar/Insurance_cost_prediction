# 🏥 Medical Insurance Cost Prediction

Welcome to the **Medical Insurance Cost Prediction** repository! This project is a web application that predicts medical insurance costs using a machine learning model (XGBoost) and provides an intuitive, creative, and responsive user interface built with **HTML**, **CSS**, and **FLask**. The project also integrates a **CSV dataset** for data collection and model training.

---

## 🌟 Features

- **Interactive UI**: A clean, modern, and user-friendly interface for inputting patient details and predicting insurance costs.
- **Machine Learning Model**: Powered by **XGBoost**, a state-of-the-art machine learning algorithm for accurate predictions.
- **Responsive Design**: The website is fully responsive and works seamlessly on all devices (desktop, tablet, and mobile).
- **Data Collection**: Uses a CSV dataset for training the model and storing user inputs.
- **Easy to Use**: Simple input fields for age, BMI, smoking status, region, etc., and instant prediction results.

---

## 🛠️ Technologies Used

- **Frontend**:
  - HTML5
  - CSS3 (Flexbox, Grid, Animations)
  - js (DOM Manipulation, Fetch API)
- **Backend**:
  - Python (for machine learning model)
  - Flask (for connecting the frontend and backend)
- **Machine Learning**:
  - XGBoost (for insurance cost prediction)
  - Pandas (for data preprocessing)
  - Scikit-learn (for model evaluation)
- **Tools**:
  - Visual Studio Code (for development)
  - Git (for version control)
  - Jupyter Notebook (for model training)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your machine.
- Flask and XGBoost libraries installed.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/medical-insurance-cost-prediction.git
   cd medical-insurance-cost-prediction

2. set up a virtual environment
 python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. install Dependencies
   pip install -r requirements.txt

4. run application
   python app.py

   project strecture
   medical-insurance-cost-prediction/
├── static/              # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── templates/           # HTML templates
│   └── index.html
├── models/              # Machine learning models
│   └── insurance_cost_model.pkl
├── data/                # CSV dataset
│   └── insurance.csv
├── app.py               # Flask application
├── train_model.py       # Script to train the XGBoost model
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation

      
