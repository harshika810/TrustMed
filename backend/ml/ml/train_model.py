import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
import joblib
import os

# 1. Load dataset
df = pd.read_csv("backend/ml/ml/data/dataset.csv")

# 2. Select useful columns
df = df[[
    "Sleep Duration",
    "Heart Rate",
    "Physical Activity Level",
    "Blood Pressure",
    "Sleep Disorder"
]].copy()

# 3. Rename columns
df.columns = [
    "sleep_hours",
    "heart_rate",
    "activity",
    "blood_pressure",
    "target"
]

# 4. Convert target FIRST
df["target"] = df["target"].apply(lambda x: 0 if pd.isna(x) else 1)

# 5. Split blood pressure
df[["systolic_bp", "diastolic_bp"]] = df["blood_pressure"].str.split("/", expand=True)

# 6. Convert BP to numeric
df["systolic_bp"] = pd.to_numeric(df["systolic_bp"], errors="coerce")
df["diastolic_bp"] = pd.to_numeric(df["diastolic_bp"], errors="coerce")

# 7. Drop old blood pressure column
df.drop(columns=["blood_pressure"], inplace=True)

# 8. Drop rows with missing values only in feature columns
df.dropna(subset=["sleep_hours", "heart_rate", "activity", "systolic_bp", "diastolic_bp"], inplace=True)

# 9. Features and target
X = df[["sleep_hours", "heart_rate", "activity", "systolic_bp", "diastolic_bp"]]
y = df["target"]

# 10. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 11. Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)



# 12. Save model
os.makedirs("backend/ml/ml/data", exist_ok=True)
joblib.dump(model, "backend/ml/ml/data/risk_model.pkl")

print("Model retrained and saved successfully")
print("Features used:", X.columns.tolist())
print("Target values:", y.unique())
print("Target count:\n", y.value_counts())
