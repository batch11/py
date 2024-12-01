import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
# Sample Data: Independent variable (X) and Dependent variable (Y)
# Here X represents the input data (e.g., hours studied), Y represents
the target data (e.g., scores achieved)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
Y = np.array([1, 2, 1.5, 3, 3.5, 4, 4.5, 5, 5.5, 6])
# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
test_size=0.2, random_state=42)
# Create a Linear Regression model
model = LinearRegression()
# Train the model using the training data
model.fit(X_train, Y_train)
# Predict values using the test data
Y_pred = model.predict(X_test)
# Print out the coefficients (slope and intercept) of the regression
line
print(f&quot;Linear Regression Equation: Y = {model.coef_[0]} * X +
{model.intercept_}&quot;)
# Evaluate the model using Mean Squared Error (MSE) and R-squared

mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)
print(f&quot;Mean Squared Error (MSE): {mse}&quot;)
print(f&quot;R-squared: {r2}&quot;)
# Plotting the results
plt.scatter(X_test, Y_test, color=&#39;blue&#39;, label=&#39;Actual data&#39;)
plt.plot(X_test, Y_pred, color=&#39;red&#39;, label=&#39;Regression line&#39;)
plt.title(&quot;Linear Regression&quot;)
plt.xlabel(&quot;X (Independent Variable)&quot;)
plt.ylabel(&quot;Y (Dependent Variable)&quot;)
plt.legend()
plt.show()
