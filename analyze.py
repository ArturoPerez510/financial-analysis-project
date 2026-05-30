import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/financial_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

total_profit = df["Profit"].sum()

print("First 5 rows:")
print(df.head())
print(f"\nTotal Profit: ${total_profit:,.2f}")

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df["Date"], df["Revenue"], label="Revenue", color="steelblue", marker="o", markersize=3)
ax.plot(df["Date"], df["Expenses"], label="Expenses", color="tomato", marker="o", markersize=3)
ax.fill_between(df["Date"], df["Profit"], 0, where=df["Profit"] >= 0, alpha=0.2, color="green", label="Profit (positive)")
ax.fill_between(df["Date"], df["Profit"], 0, where=df["Profit"] < 0, alpha=0.2, color="red", label="Profit (negative)")
ax.set_title("30-Day Financial Overview")
ax.set_xlabel("Date")
ax.set_ylabel("Amount ($)")
ax.legend()
ax.tick_params(axis="x", rotation=45)
fig.tight_layout()
plt.savefig("data/financial_chart.png", dpi=150)
print("Chart saved to data/financial_chart.png")
