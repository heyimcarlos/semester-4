# Machine Learning Fundamentals

It's the field of study that gives computers the ability to learn without being explicitly
programmed. - Arthur Samuel

## Types of learning

- **Supervised learning**: The model is trained on a completely labeled dataset, an input (classes, features) is given and an output (labels) is expected.
- **Unsupervised learning**: The model is trained on an unlabeled dataset, the model tries to learn the patterns and structure from the data without any labels.
- **Semi-supervised learning**: The model is trained on a dataset that's partially labeled, the model learns from both labeled and unlabeled data.
- **Reinforcement learning**: The model learns by interacting with the environment, it's a trial and error process; the model learns from each action it takes based on the feedback it receives (reward or penalty).
- **Self-supervised learning**: The model learns from the data itself, it generates its own labels from the data, and learns to predict those labels.

- **Forward-pass**: The process of passing an input through a model and gettin an
  output (prediction).
- **Back-propagation/backward pass**: Using the output (loss) to calculate the gradients.
- **Gradient descent**: The process of updating the model's parameters (weights)
  using the gradients calculated from the loss function.
- **Gradients**: The partial derivatives of the loss function with respect to the
  model's parameters (weights).
- **Loss function**: A function that measures how well the model's predictions match
  the true labels. The loss function is used to calculate the gradients.
- **Learning step**: Also called interaction, it's one complete round where the model
  does a forward pass to get an output, computes the loss, runs a backward pass to
  calculate the gradients, and updates the weights (parameters) using an optimizer
  (i.e., gradient descent).

Linear regression:

Polynomial regression:

how to decide the degree of the polynomial?

- cross validation:
- learning curves:

Bias: training data
Variance: test data
Regularization: A technique to reduce overfitting

Ways to constraint a model (loss functions):

1. L1 = math.abs(y-y^) (lasso)
2. L2 (ridge)
3. Elastic net
4. Dropout

Stochastic Gradient Descent (SGD) Regression
