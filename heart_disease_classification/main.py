import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
from sklearn.svm import SVC
import seaborn as sns
import time
import os

column_names = ["age", "sex", "cp", "trtbps", "chol", "fbs", "restecg", "thalachh", "exng", "oldpeak", "slp", "caa", "thall", "output"]

def plot_column(data, col_name):
    # Histogram plot
    plt.subplot(1, 2, 1)
    sns.histplot(data[col_name], kde=True)
    # Box plot
    plt.subplot(1, 2, 2)
    sns.boxplot(x=data[col_name])


    plt.tight_layout()
    plt.show()


def visualizer(data):
    # For each column in the csv
    for col in column_names:
        plot_column(data, col) # plot


def print_evaluations(y_test, y_pred):
    # Print accuracy
    print("Accuracy: ", round(accuracy_score(y_test, y_pred), 2) * 100, "%")

    # Print classification report
    print("Classification report:")
    print(classification_report(y_test, y_pred)) # precision, recall, f1-score

    # Print confusion matrix
    print("Confusion matrix:")
    print(confusion_matrix(y_test, y_pred))


def classifier(data, kernel, split):
    # Split the dataset into features and target variable
    x = data.drop('output', axis=1)
    y = data['output']

    # Split the dataset into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=split, random_state=100)

    # Standardize features ('center around 0')
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    # Choose SVM (Support Vector Machine) classification algorithm
    classifier = SVC(kernel=kernel, random_state=100)

    # Train the model on the training data
    classifier.fit(x_train, y_train)

    # Evaluate the model on the test data
    y_pred = classifier.predict(x_test)

    # Print Evaluations
    print_evaluations(y_test, y_pred)
    

def main():
    # Read the dataset
    file_path = os.path.join(os.path.dirname(__file__), "heart.csv")
    data = pd.read_csv(file_path)

    # VISUALIZATION
    #visualizer(data)

    # CLASSIFICATION
    start = time.time()

    # RBF
    classifier(data, 'rbf', 0.3) # 70% training - 30% testing
    # classifier(data, 'rbf', 0.2) # 80% training - 20% testing

    # Linear
    # classifier(data, 'linear', 0.3) # 70% training - 30% testing
    # classifier(data, 'linear', 0.2) # 80% training - 20% testing

    # Sigmoid
    # classifier(data, 'sigmoid', 0.3) # 70% training - 30% testing
    # classifier(data, 'sigmoid', 0.2) # 80% training - 20% testing

    end = time.time()

    # Print execution time (for 1 algorithm)
    print("Execution time: ", round((end - start) * 1000), "ms")


if __name__ == "__main__":
    main()