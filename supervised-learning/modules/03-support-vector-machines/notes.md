# Linear Support Vector Machines (SVM)

Whenever we are dealing with a linear classification problem, the support
vectors are the data points that are closest to the decision boundary (the line
that separates the two different features).

Support vector machines are **Discrimitive classifiers**.

- Hinge loss function: The hinge loss function is used for "maximum-margin" classification, most notably for support vector machines. It is a loss function that is used to train classifiers. The hinge loss function is defined as:

$$
L(y, f(x)) = \max(0, 1 - y \cdot f(x))
$$

where:

- $y$ is the true label of the data point (either -1 or 1)
- $f(x)$ is the predicted value of the data point
- $L(y, f(x))$ is the loss function

Vectors

- ||w|| is the form notation of vectors, it is the length or magnitude of the vector.

for vector $w$: $[w_1, w_2, ..., w_n]$, the most common norm is the Euclidean norm, which is defined as:

$$
||w|| = \sqrt{w_1^2 + w_2^2 + ... + w_n^2}
$$

## Multiclass classification

Is when the target variable (predicted value) can
take on multiple classes. Instead of yes or no, 0 or 1, multiclass classification
have many possible options. Example:

| Input          | Task              | Classes                                       |
| -------------- | ----------------- | --------------------------------------------- |
| Image of digit | digit recognition | 0 through 9 (10 classes)                      |
| Email text     | Categorize email  | Spam, social, primary, promotions (4 classes) |

For multiclass tasks, models usually output a vector of scores, one for each class.

$ z = [z_1, z_2,...,z_k] $

- Where $k$ is the number of classes.

## Softmax Activation Function

Softmax converts the raw scores returned by the model ($z$) into probabilities.

- Each $y^_i$ is the predicted probability of class $i$.

## Cross-entropy loss

A loss function used to compare the probabilities ($y^_i$) with the true class label
($y$). Measures how far off the predictions are from the true labels. **The loss function
used with softmax activation function**

- **Activation**: A function applied to a neuron's output. Take the raw score ->
  apply a function -> get the output.
  - **Sigmoid**: Used for binary classification. Converts the raw score into a
    probability between 0 and 1.
  - **Softmax**: Used for multiclass classification. Converts a vector of scores
    into probabilities.
  - **ReLU**: Used for hidden layers.
