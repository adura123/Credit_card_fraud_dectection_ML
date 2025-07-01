from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load your trained model
with open('logistic_bal_smote_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form inputs
        data = request.form
        input_features = []

        # Only use V1 to V28 and Amount (not Time)
        for i in range(1, 29):  # V1 to V28
            input_features.append(float(data[f'V{i}']))
        input_features.append(float(data['Amount']))  # Add Amount

        # Convert to NumPy array
        input_array = np.array(input_features).reshape(1, -1)

        # Predict
        prediction = model.predict(input_array)[0]
        confidence = round(np.max(model.predict_proba(input_array)) * 100, 2)

        return render_template('result.html', prediction=prediction, confidence=confidence)
    
    except Exception as e:
        return f"Error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
