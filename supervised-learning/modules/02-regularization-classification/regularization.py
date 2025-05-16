# Stochastic Gradient Descent
import numpy as np
from sklearn.linear_model import SGDRegressor
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import StandardScaler

n_samples, n_features = 10, 5
rng = np.random.RandomState(0)
y = rng.randn(n_samples)
X = rng.randn(n_samples, n_features)
# Always scale the input. The most convenient way is to use a pipeline.
reg = make_pipeline(StandardScaler(), reg.fit(X, y))

Pipeline(steps=[("standardscaler", StandardScaler()), ("sgdregressor", SGDRegressor())])
