import pandas as pd
import numpy as np
from datetime import date, timedelta

np.random.seed(42)

start = date(2026, 1, 1)
dates = [start + timedelta(days=i) for i in range(30)]
revenue = np.random.randint(10000, 50000, size=30)
expenses = np.random.randint(5000, 30000, size=30)
profit = revenue - expenses

df = pd.DataFrame({
    "Date": dates,
    "Revenue": revenue,
    "Expenses": expenses,
    "Profit": profit,
})

df.to_csv("data/financial_data.csv", index=False)
print("financial_data.csv created successfully.")
