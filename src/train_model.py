"""Gesture Recognition Model Training

Trains a K-Nearest Neighbors model for hand gesture classification
using sensor data from flex sensors and accelerometer.
"""

import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Configuration
DATASET_PATH = '../data/gesture_dataset.csv'
MODEL_OUTPUT_PATH = '../models/gesture_model.sav'
TEST_SIZE = 0.3
RANDOM_STATE = 5
N_NEIGHBORS = 3


def load_data():
    """Load and prepare the gesture dataset"""
    print("Loading gesture dataset...")
    data = pd.read_csv(DATASET_PATH)
    print(f"Dataset shape: {data.shape}")
    
    # Features (all columns except the last one)
    X = data.iloc[:, :-1]
    # Target (last column)
    y = data.iloc[:, -1]
    
    print(f"Features shape: {X.shape}")
    print(f"Target classes: {sorted(y.unique())}")
    
    return X, y, data


def visualize_data(data):
    """Create visualizations of the dataset"""
    print("\nCreating data visualizations...")
    
    # Class distribution
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Target', data=data)
    plt.title('Gesture Class Distribution')
    plt.xlabel('Gesture Class')
    plt.ylabel('Count')
    plt.show()


def train_model(X_train, y_train):
    """Train the KNN classifier"""
    print(f"\nTraining KNN model with {N_NEIGHBORS} neighbors...")
    model = KNeighborsClassifier(n_neighbors=N_NEIGHBORS)
    model.fit(X_train, y_train)
    print("Model training completed.")
    return model


def save_model(model, filepath):
    """Save the trained model to disk"""
    print(f"\nSaving model to {filepath}...")
    with open(filepath, 'wb') as model_file:
        pickle.dump(model, model_file)
    print("Model saved successfully.")


def evaluate_model(model, X_test, y_test):
    """Evaluate model performance and create visualizations"""
    print("\nEvaluating model performance...")
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate accuracy
    accuracy = metrics.accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy * 100:.2f}%")
    
    # Confusion matrix
    cm = metrics.confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, cmap="Blues", fmt='g', cbar=False)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.show()
    
    # Classification report
    classification_report = metrics.classification_report(y_test, y_pred)
    print('\nClassification Report:')
    print(classification_report)
    
    return accuracy, y_pred


def main():
    """Main function to train and evaluate the gesture recognition model"""
    print("=== Gesture Recognition Model Training ===")
    
    # Load data
    X, y, data = load_data()
    
    # Visualize data
    visualize_data(data)
    
    # Split data
    print(f"\nSplitting data (test size: {TEST_SIZE})...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )
    print(f"Training set size: {X_train.shape[0]}")
    print(f"Test set size: {X_test.shape[0]}")
    
    # Train model
    model = train_model(X_train, y_train)
    
    # Save model
    save_model(model, MODEL_OUTPUT_PATH)
    
    # Evaluate model
    accuracy, y_pred = evaluate_model(model, X_test, y_test)
    
    print(f"\n=== Training Complete ===")
    print(f"Final Accuracy: {accuracy * 100:.2f}%")
    print(f"Model saved to: {MODEL_OUTPUT_PATH}")


if __name__ == "__main__":
    main()