"""
House Price Prediction - Model Training Script
Trains and compares three regression models, saves the best one.
"""

import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

print("="*70)
print("HOUSE PRICE PREDICTION - MODEL TRAINING")
print("="*70)

# Step 1: Create synthetic dataset
print("\n📊 Creating dataset...")
np.random.seed(42)
n_samples = 1000

data = {
    'area': np.random.randint(500, 5000, n_samples),
    'bedrooms': np.random.randint(1, 6, n_samples),
    'bathrooms': np.random.randint(1, 5, n_samples),
    'floors': np.random.randint(1, 4, n_samples),
    'year_built': np.random.randint(1980, 2024, n_samples),
    'location_score': np.random.randint(1, 11, n_samples)
}

df = pd.DataFrame(data)

# Create target variable (price)
df['price'] = (
    df['area'] * 100 + 
    df['bedrooms'] * 50000 + 
    df['bathrooms'] * 30000 + 
    df['floors'] * 20000 + 
    (2024 - df['year_built']) * -1000 +
    df['location_score'] * 100000 +
    np.random.randint(-50000, 50000, n_samples)
)

print(f"✅ Dataset created with {len(df)} samples")

# Step 2: Check for missing values
print("\n🔍 Checking data quality...")
if df.isnull().sum().sum() == 0:
    print("✅ No missing values found")
else:
    print("⚠️  Filling missing values...")
    df.fillna(df.median(), inplace=True)

# Step 3: Prepare features and target
X = df.drop('price', axis=1)
y = df['price']

# Step 4: Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"✅ Training samples: {len(X_train)}")
print(f"✅ Testing samples: {len(X_test)}")

# Step 5: Train and compare models
print("\n🤖 Training models...\n")

models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree': DecisionTreeRegressor(random_state=42),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42)
}

results = {}

for name, model in models.items():
    print(f"Training {name}...")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    
    results[name] = {
        'model': model,
        'r2_score': r2,
        'mae': mae
    }
    
    print(f"  ✓ R² Score: {r2:.4f}")
    print(f"  ✓ MAE: ₹{mae:,.2f}\n")

# Step 6: Select best model
best_model_name = max(results, key=lambda x: results[x]['r2_score'])
best_model = results[best_model_name]['model']
best_r2 = results[best_model_name]['r2_score']

print("="*70)
print(f"🏆 BEST MODEL: {best_model_name}")
print(f"📊 R² Score: {best_r2:.4f}")
print(f"💰 MAE: ₹{results[best_model_name]['mae']:,.2f}")
print("="*70)

# Step 7: Save model
model_filename = 'model.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(best_model, file)

print(f"\n💾 Model saved as '{model_filename}'")
print("✅ Training complete!\n")

# Step 8: Test prediction
print("🧪 Testing prediction...")
sample = pd.DataFrame({
    'area': [2500],
    'bedrooms': [3],
    'bathrooms': [2],
    'floors': [2],
    'year_built': [2015],
    'location_score': [8]
})

predicted_price = best_model.predict(sample)[0]
print(f"Sample input: Area=2500, Bed=3, Bath=2, Floors=2, Year=2015, Location=8")
print(f"Predicted price: ₹{predicted_price:,.2f}")
print("\n" + "="*70)
