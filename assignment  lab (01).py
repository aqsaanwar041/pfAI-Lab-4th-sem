import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import os

data = pd.read_csv("train.csv")
data = data[["GrLivArea", "OverallQual", "YearBuilt", "SalePrice"]].dropna()

X = data[["GrLivArea", "OverallQual", "YearBuilt"]]
y = data["SalePrice"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

output = pd.DataFrame({"Actual": y_test, "Predicted": predictions})

output_path = os.path.join(os.getcwd(), "submission.csv")
output.to_csv(output_path, index=False)

print(f"✅ Done! Results saved at: {output_path}")
