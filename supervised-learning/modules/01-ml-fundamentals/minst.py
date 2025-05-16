from typing import cast

import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.utils import Bunch

np.random.seed(0)

# Load MNIST dataset
# cast it bunch to get over pyright
mnist = cast(Bunch, fetch_openml("mnist_784", version=1, parser="auto"))
mnist.keys()
# error: Diagnostics: 1. Cannot access attribute "keys" for class "tuple[Unknown, Unknown]" Attribute "keys" is unknown [reportAttributeAccessIssue]

print("Keys: ", mnist.keys())

X: pd.DataFrame = mnist["data"]
print("X shape: ", X.shape)
print("X first 5 rows: ", X.head())

y: pd.Series = mnist["target"]
print("y shape: ", y.shape)

# each image is 28x28 pixels
some_digit = X.iloc(0)
print(some_digit)
