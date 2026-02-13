import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import pickle


data = pd.read_csv('../data/gesture_dataset.csv')

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=5)

sns.countplot(x='Target', data=data)
plt.show()

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

filename = '../models/gesture_model.sav'
pickle.dump(model, open(filename, 'wb'))

y_pred = model.predict(X_test)

acc = metrics.accuracy_score(y_pred, y_test)
print("Accuracy is:", acc*100,"%")

cm = metrics.confusion_matrix(y_pred, y_test)
plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, cmap="Blues",fmt='g',cbar=False)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title("Confusion Matrix")
plt.show()



# Classification report
classification_report = metrics.classification_report(y_pred, y_test)
print('Classification Report:\n', classification_report)