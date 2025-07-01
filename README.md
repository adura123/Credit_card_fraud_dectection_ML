
# 💳 Credit Card Fraud Detection Web App

A real-time web-based application built using **Flask** and **Machine Learning** to detect credit card fraud. This project applies advanced **resampling techniques** to address class imbalance and deploys the most efficient model — **Logistic Regression with SMOTE** — for accurate and scalable fraud detection.

---

## 📌 Project Overview

Credit card fraud poses a significant threat to financial institutions and consumers worldwide. Detecting fraudulent transactions is challenging due to:

- The **highly imbalanced nature** of datasets (only 0.172% fraud cases).
- The **evolving techniques** used by fraudsters.
- The limitations of rule-based fraud detection systems.

This project develops a robust ML pipeline to preprocess transaction data, handle imbalance using **SMOTE**, and evaluate multiple models. The best model is deployed in a user-friendly **Flask web app** for real-time prediction.

---

## 🧠 Machine Learning Approach

- **Dataset**: European cardholder transactions (284,807 records, 492 frauds) from [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud).
- **Feature Transformation**: PCA-applied numerical features (V1–V28), plus `Time` and `Amount`.
- **Resampling Techniques**: SMOTE, ADASYN, Random Oversampling, Undersampling.
- **Models Tested**:
  - Logistic Regression ✅ (Best, ROC-AUC: 0.97)
  - Random Forest
  - Decision Tree
  - XGBoost

---

## ✅ Best Model

| Model               | ROC-AUC (Test) | Precision | Recall | F1 Score |
|--------------------|----------------|-----------|--------|----------|
| Logistic Regression (with SMOTE) | **0.97**         | High      | High   | High     |

Chosen for its **simplicity**, **interpretability**, **performance**, and **low computational cost**.

---

## 🖥️ Web Application Features

- **Frontend**: HTML + CSS
- **Backend**: Python Flask
- **Model Interface**: Accepts user inputs for transaction features
- **Output**: Fraud / Not Fraud prediction + Confidence Score

### Screenshots

![Index Page](screenshots/index.png)
![Fraud Result](screenshots/fraud_result.png)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Flask
- Scikit-learn
- Pandas, NumPy
- imbalanced-learn (for SMOTE)

### Installation

```bash
git clone https://github.com/yourusername/credit-card-fraud-detector.git
cd credit-card-fraud-detector
pip install -r requirements.txt
```

### Run the App

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## 📁 Project Structure

```
├── app.py                 # Flask app
├── templates/
│   ├── home.html          # Main input form
│   └── result.html        # Prediction result page
├── static/
│   └── styles.css         # Styling
├── model/
│   └── logistic_model.pkl # Trained Logistic Regression model
├── utils/
│   └── preprocessing.py   # Scaling & input transformation
├── README.md
└── requirements.txt
```

---

## 🔍 Evaluation Metrics

- **Accuracy**
- **Precision**
- **Recall**
- **F1 Score**
- **ROC-AUC Curve**
- **Confusion Matrix**

These metrics ensure a balanced performance between identifying frauds and avoiding false positives.

---

## 📈 Results & Insights

- SMOTE significantly improved recall without increasing false positives.
- Logistic Regression consistently outperformed complex models like XGBoost in generalizability.
- Deployment via Flask ensures easy integration into fintech environments.

---

## 🔐 Ethical Considerations

- **Data Privacy**: PCA-anonymized features protect user data.
- **Bias Mitigation**: Balanced training data reduces discrimination.
- **Transparency**: Logistic Regression's simplicity aids in interpretability and compliance.

---

## 🔮 Future Improvements

- Integrate **Deep Learning** (e.g., Autoencoders, LSTM).
- Add **transactional context features** (e.g., device ID, geo-location).
- Implement **user dashboard** and **alert notifications**.
- Extend to **streaming data** via Kafka or AWS Kinesis.

---

## 🤝 Acknowledgements

Special thanks to:

- **Teesside University** – Academic support
- **Supervisor**: Mansha Nawaz
- **Contributors**: Friends & faculty for feedback and collaboration

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
