from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report

iris = load_iris()
X = iris.data
y = iris.target

print("Dataset loaded!")
print("Total samples:", len(X))
print("Total features:", X.shape[1])
print("Classes:", iris.target_names)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("Scaling done!")

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

print("Model trained!")

predictions = model.predict(X_test)

print("Accuracy:", round(accuracy_score(y_test, predictions) * 100, 2), "%")
print("F1 Score:", round(f1_score(y_test, predictions, average='weighted') * 100, 2), "%")
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))
print("Classification Report:")
print(classification_report(y_test, predictions, target_names=iris.target_names))