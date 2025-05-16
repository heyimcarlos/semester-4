# Why Regulatization?

When a model does not performs well on unseen or test data. It means the model
is not able to predict the output or target column, this is what we call an
overfitted model. We use regularization techniques to reduce overfitting.

Regularization shrinks coefficients to reduce complexity.

- Smaller coefficients → less complex → less flexible → better generalization.
- So:
  - More flexibility (big coefficients) → likely overfit.
  - Less flexibility (small coefficients) → likely to generalize better.

## Noise

It's those data points that don't represent the general trend of the data. Data
points in the dataset that don't represent the true properties of the data.

- Irrelevant, random, or unpredictable components in data.
- Caused by:
  - Measurement error
  - Data entry mistakes

The increase of flexibility of a model is represented by an increase in its
coefficients.

- When a model pays too much attention to noise, it overfits.

## How does Regularization work?

The goal of regularization is to minimize the RSS, by choosing the right
coefficients. In linear regression, we try to find the best coefficients by
minimizing the error term (i.e., the residual sum of squares).

If a model fits the data too well (overfits), the coefficients might get too large.
That's where regularization comes in:

- It adds a penalty to the RSS to control the size of the coefficients.

### The Problem

Overfitting due to noise. When data has noise (random patterns), fitting it too closely means:

- the model learns the noise.
- the model's generalization performance decreases.

how to fix it (regularization):

- penalize large coefficients.

### Types of Regularization techniques

- Ridge regression (L2 regularization): Ridge trades a bit of training accuracy for better generalization.

  - it introduces a penalty term to the loss function (RSS).
  - the penalty term is the sum of the squares of the coefficients.
  - the penalty term is multiplied by a hyperparameter (lambda) that controls the
    strength of the penalty.

  Benefits:

  - handles multicollinearity: Ridge regression distributes the weight
    across correlated features. Essentially assigning a smaller weight to each
    feature, rather than assigning a large weight to one feature.

- Lasso regression (L1 regularization): Stands for Least absolute and selection
  operator.

  - it introduces a penalty term to the loss function (RSS).
  - the penalty term is the sum of the absolute values of the coefficients.
  - the penalty term is multiplied by a hyperparameter (lambda) that controls the
    strength of the penalty.

  Benefits:

  - automatic feature selection: Since some coefficients are shrunk to zero, and
    in linear regression we multiple the weights/coefficients by the features, some
    features are completely removed/ignored.

## Keyterms

- **Multicollinearity**: The correlation between two or more independent variables (features).
- **Coefficients**: Coefficients/weights are the values applied to each feature,
  which determine the importance/impact of this feature when predicting the target.
  Weights that show how much each feature affects predictions.
- **Residual Sum of Squares**: The loss function for linear regresssion models.
  $$RSS = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$
  - This measures how far off our prediction are from the true values.
- **Flexibility**: model’s capacity to fit data closely.

Regularization reduces flexibility (by shrinking coefficients) to improve generalization.

Smaller coefficients usually = simpler model = better generalization, not more flexibility.

### Example

Example with Time-of-Day Features

Suppose you split a datetime feature into:

- is_morning (1 if time is morning, else 0)
- is_evening
- is_night

These are highly collinear because:

- If one is 1, the others are 0.
- Their values are mutually exclusive but dependent.
- Knowing one almost completely predicts the others

## Curse of dimensionality

The problem that arises when we have too many features/dimensions in our dataset.
as the number of dimensions (features) increases:

- Data becomes sparse (spread out)
- Distance between points becomes less meaningful
- Models become harder to train and generalize
- Overfitting becomes more likely
- You often need exponentially more data to train a model effectively
