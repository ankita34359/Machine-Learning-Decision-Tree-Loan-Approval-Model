# Loan Approval Prediction Model - Decision Tree

## Overview

The **Loan Approval Prediction Model** leverages a Decision Tree algorithm to predict loan approval outcomes based on applicant data. This project provides an interpretable approach to assist financial institutions in making informed lending decisions.

## Features

- **Predictive Modeling**: Uses Decision Tree for loan approval predictions.
- **Data Analysis**: Analyzes applicant features like income, credit history, and loan amount.
- **Model Evaluation**: Assesses the accuracy and performance of the prediction model.
- **Visualization**: Provides visual representation of the Decision Tree and key metrics.

## Technologies Used

- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Scikit-learn

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ankita34359/Machine-Learning-Decision-Tree-Loan-Approval-Model.git
   cd Machine-Learning-Decision-Tree-Loan-Approval-Model
   ```

2. **Set Up Virtual Environment** (optional)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Project**
   Execute the Python script to train and evaluate the Decision Tree model:
   ```bash
   python loan_approval_model.py
   ```

## Dataset

- The dataset includes features such as:
  - Applicant Income
  - Loan Amount
  - Loan Term
  - Credit History
  - Loan Status (Approved/Rejected)

- Data preprocessing includes handling missing values, encoding categorical variables, and feature scaling.

## How It Works

1. **Data Preprocessing**:
   - Handles missing values.
   - Encodes categorical data into numerical form.
     
2. **Model Training**:
   - Splits data into training and testing sets.
   - Trains the Decision Tree model on the training data.
     
3. **Prediction and Evaluation**:
   - Evaluates model performance using accuracy, precision, and recall metrics.
   - Visualizes the Decision Tree for better interpretability.

## Results

- Provides metrics like accuracy, confusion matrix, and decision boundaries.
- Identifies key factors influencing loan approval.

## Contributing
Contributions are welcome! Fork the repository, create a new branch, and submit a pull request to enhance the project.

## License
This project is licensed under the [MIT License](LICENSE).

---

Enhancing financial decision-making with interpretable Machine Learning models! 🚀
