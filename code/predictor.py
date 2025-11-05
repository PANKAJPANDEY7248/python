from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# Load the digits dataset
digits = load_digits()

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, test_size=0.2, random_state=42
)

# Train a simple logistic regression model
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

# Predict a digit from the test set
index = 0  # You can change this to test other digits
prediction = model.predict([X_test[index]])
actual = y_test[index]

# Show the result
print(f"Predicted digit: {prediction[0]}")
print(f"Actual digit: {actual}")

# Display the image
plt.gray()
plt.matshow(digits.images[index])
plt.title(f"Digit Image (Actual: {actual})")
plt.show()
