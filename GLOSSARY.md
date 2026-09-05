# Machine Learning Glossary

Canonical definitions for core concepts in machine learning, classification, and ensemble algorithms.

## Terms

**Backpropagation**:
Reverse-mode automatic differentiation applied to computational graphs to efficiently calculate exact gradients of a scalar loss function with respect to all network parameters.
_Avoid_: Backward pass algorithm, error back-pass

**Sigmoid Function**:
An S-shaped mathematical activation function $\sigma(z) = \frac{1}{1 + e^{-z}}$ that maps any real-valued number into a probability between 0.0 and 1.0.
_Avoid_: Logistic curve, S-function

**Log Loss (Binary Cross-Entropy)**:
A loss function used for binary classification that heavily penalizes confident wrong predictions.
_Avoid_: Cross-entropy error, classification MSE

**Entropy**:
A measure of impurity or chaos within a dataset node, defined as $H(S) = - \sum p_i \log_2(p_i)$.
_Avoid_: Disorder score, node variance

**Gini Impurity**:
A computationally efficient measure of node impurity defined as $G(S) = 1 - \sum p_i^2$, representing the probability of misclassifying a randomly chosen element.
_Avoid_: Gini index (in economics context)

**Information Gain**:
The reduction in entropy or impurity achieved by splitting a node on a given feature.
_Avoid_: Split value, entropy reduction

**Bootstrapping**:
Generating multiple distinct datasets by randomly sampling rows from the original training set with replacement.
_Avoid_: Row resampling, data duplication

**Bagging (Bootstrap Aggregating)**:
An ensemble technique that trains multiple models independently in parallel on bootstrapped datasets and aggregates their predictions to reduce variance.
_Avoid_: Parallel modeling, bootstrapped voting

**Random Forest**:
An extension of bagging that decorrelates decision trees by considering only a random subset of features ($\sqrt{M}$) at each node split.
_Avoid_: Forest classifier, random trees

**Boosting**:
An ensemble technique that trains weak models sequentially, where each new model is explicitly optimized to correct the residual errors or misclassifications of prior models.
_Avoid_: Sequential aggregation, error fitting
