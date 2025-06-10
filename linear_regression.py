import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Step 1: Create dataset
data = {
    "Square_Footage": [650, 800, 1200, 1500, 2000],
    "Price": [200000, 250000, 300000, 350000, 500000]
}
df = pd.DataFrame(data)

# Step 2: Prepare features and target
X = df[["Square_Footage"]]
y = df["Price"]

# Step 3: Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Make predictions on test data
y_pred = model.predict(X_test)

# Step 6: Evaluate model performance
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Step 7: Test model with new data
new_data = pd.DataFrame({"Square_Footage": [1000, 1700]})
predictions = model.predict(new_data)
print("Predicted Prices for New Data:", predictions)

# Step 8: Visualize regression line with all points

plt.scatter(X, y, color='blue', label='Actual Data')  # Original data points
plt.scatter(new_data, predictions, color='green', label='New Predictions', marker='X', s=100)  # New predictions

# Regression line on full dataset range
plt.plot(X, model.predict(X), color='red', label='Regression Line')

plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.title("Linear Regression - House Prices")
plt.legend()
plt.show()
