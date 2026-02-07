"""
House Price Prediction - Flask Web Application
Production-ready Flask app for Render deployment
"""

from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

app = Flask(__name__)

# Load trained model
print("🔄 Loading trained model...")
try:
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    print("✅ Model loaded successfully!")
except FileNotFoundError:
    print("❌ Error: model.pkl not found!")
    print("Please run 'python train_model.py' first.")
    exit(1)

@app.route('/')
def home():
    """Display the home page with input form"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests"""
    try:
        # Get form data
        area = float(request.form['area'])
        bedrooms = int(request.form['bedrooms'])
        bathrooms = int(request.form['bathrooms'])
        floors = int(request.form['floors'])
        year_built = int(request.form['year_built'])
        location_score = int(request.form['location_score'])
        
        # Create DataFrame for prediction
        input_data = pd.DataFrame({
            'area': [area],
            'bedrooms': [bedrooms],
            'bathrooms': [bathrooms],
            'floors': [floors],
            'year_built': [year_built],
            'location_score': [location_score]
        })
        
        # Make prediction
        predicted_price = model.predict(input_data)[0]
        
        # Format price
        formatted_price = f"₹{predicted_price:,.2f}"
        
        # Return result
        return render_template('result.html', 
                             price=formatted_price,
                             area=area,
                             bedrooms=bedrooms,
                             bathrooms=bathrooms,
                             floors=floors,
                             year_built=year_built,
                             location_score=location_score)
    
    except Exception as e:
        return render_template('result.html', error=f"Error: {str(e)}")

if __name__ == '__main__':
    # Get port from environment variable (for Render deployment)
    port = int(os.environ.get('PORT', 5000))
    
    print("\n" + "="*70)
    print("🏠 HOUSE PRICE PREDICTION APP")
    print("="*70)
    print(f"📱 Running on: http://0.0.0.0:{port}")
    print("Press CTRL+C to stop")
    print("="*70 + "\n")
    
    # Run app
    app.run(host='0.0.0.0', port=port, debug=False)
