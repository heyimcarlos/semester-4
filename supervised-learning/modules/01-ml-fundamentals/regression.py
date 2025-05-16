import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures

# Sample number
m = 100
# Feature number
X = 6 * np.random.rand(m, 1) - 3
print("X.shape", X.shape)
print("X", X[:5])
# Target/label
y = 0.5 * X**2 + X + 2 + np.random.randn(m, 1)
print("y.shape", y.shape)
print("y", y[:5])

# Plotting the data
plt.scatter(X, y, color="red")
plt.title("Scatter plot")
plt.xlabel("X")
plt.ylabel("y")
plt.show()

poly_features = PolynomialFeatures(degree=2, include_bias=True, interaction_only=False)
# fit and transform the data
# fit: find the coefficients
# transform: apply the transformation
X_poly = poly_features.fit_transform(X)

print("X_poly.shape", X_poly.shape)
print("X_poly", X_poly)
print(poly_features.get_feature_names_out(input_features=None))

# Fit the model
linear_reg = LinearRegression()
m = linear_reg.fit(X_poly, y)

# Used in the inference step to give the same step-by-step transformations
#  TODO: research how pipelines are used
polynomial_regression = Pipeline([])

Ridge()
