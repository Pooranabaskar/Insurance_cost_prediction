import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib


url = "insurance.csv"
data = pd.read_csv(url)


print("Dataset Head:")
print(data.head())


data['sex'] = data['sex'].map({'male': 1, 'female': 0})  # Male: 1, Female: 0
data['smoker'] = data['smoker'].map({'yes': 1, 'no': 0})  # Smoker: 1, Non-smoker: 0
data = pd.get_dummies(data, columns=['region'], drop_first=True)  # One-hot encode 'region'


X = data.drop('charges', axis=1)  # Features
y = data['charges']  # Target variable


print("\nProcessed Features:")
print(X.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


print("\nTraining the model...")
model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
print("\nModel Evaluation:")
print(f"Mean Absolute Error: {mean_absolute_error(y_test, y_pred)}")
print(f"R² Score: {r2_score(y_test, y_pred)}")


joblib.dump(model, 'insurance_cost_model.pkl')
print("\nModel saved as insurance_cost_model.pkl")