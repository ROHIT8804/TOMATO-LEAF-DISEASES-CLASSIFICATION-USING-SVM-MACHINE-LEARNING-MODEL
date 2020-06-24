import pandas as pd
from sklearn import svm
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler


datasets = pd.read_csv('Labled_DATAUpdate1.csv')
X = datasets.iloc[:,1:].values
print(X.shape)
Y = datasets.iloc[:, 0].values

scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)
X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.25, random_state=0)


clf = svm.SVC(kernel='linear') # Linear Kernel
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Score: ")
a=accuracy_score(y_test, y_pred)
print(a1*100)

cm=confusion_matrix(y_test, y_pred)
print("Confusion Matrix: ")
print(cm)

print('Report : ')
print(classification_report(y_test, y_pred))



