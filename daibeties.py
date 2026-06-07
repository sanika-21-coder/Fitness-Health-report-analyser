
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
import os

print("🔄 Training Diabetes Model...")

df = pd.read_csv("report_dataset.csv")

print("Columns in dataset:", df.columns)

target_column = "Label"  

X = df.drop(target_column, axis=1)
y = df[target_column]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"✅ Model trained successfully with accuracy: {accuracy*100:.2f}%")

os.makedirs("model", exist_ok=True)

model_path = os.path.join("model", "diabetes_model.pkl")
pickle.dump(model, open(model_path, "wb"))

print(f"🎉 Diabetes model saved successfully at {model_path}")
