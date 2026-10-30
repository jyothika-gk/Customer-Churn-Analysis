# ===== Telco Customer Churn Analysis =====
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter

# ---------- 1. LOAD ----------
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# ---------- 2. CLEAN ----------
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.dropna(subset=["TotalCharges"])
df["ChurnValue"] = (df["Churn"] == "Yes").astype(int)
df["TenureGroup"] = pd.cut(df["tenure"], bins=[0, 12, 24, 48, 72],
                           labels=["0-12", "13-24", "25-48", "49-72"])

# ---------- 3. RESULTS (remove the # to show a result) ----------
# print(df.shape)
# print(df["ChurnValue"].mean() * 100)
# print(df.groupby("Contract")["ChurnValue"].mean() * 100)
# print(df.groupby("TenureGroup", observed=True)["ChurnValue"].mean() * 100)
# print(df.groupby("InternetService")["ChurnValue"].mean() * 100)
# print(df.groupby("PaymentMethod")["ChurnValue"].mean() * 100)
# print(df.groupby("Churn")[["tenure", "MonthlyCharges"]].mean())
# print(df.groupby("SeniorCitizen")["ChurnValue"].mean() * 100)
# print(df.groupby("gender")["ChurnValue"].mean() * 100)
# print(df.groupby("OnlineSecurity")["ChurnValue"].mean() * 100)
# print(df.groupby("TechSupport")["ChurnValue"].mean() * 100)

# ---------- 4. CHARTS ----------
# Chart 1: churn by contract
sns.barplot(x="Contract", y="ChurnValue", data=df)
plt.title("Churn Rate by Contract Type")
plt.ylabel("Churn Rate")
plt.gca().yaxis.set_major_formatter(PercentFormatter(1.0))
plt.savefig("churn_by_contract.png")
plt.show()

# Chart 2: churn by tenure
sns.barplot(x="TenureGroup", y="ChurnValue", data=df)
plt.title("Churn Rate by Tenure (months)")
plt.ylabel("Churn Rate")
plt.gca().yaxis.set_major_formatter(PercentFormatter(1.0))
plt.savefig("churn_by_tenure.png")
plt.show()
# Chart 3: churn by internet service
sns.barplot(x="InternetService", y="ChurnValue", data=df)
plt.title("Churn Rate by Internet Service")
plt.ylabel("Churn Rate")
plt.gca().yaxis.set_major_formatter(PercentFormatter(1.0))
plt.savefig("churn_by_internet.png")
plt.show()

# Chart 4: monthly charges, stayed vs left
sns.boxplot(x="Churn", y="MonthlyCharges", data=df)
plt.title("Monthly Charges: Stayed vs Left")
plt.savefig("charges_by_churn.png")
plt.show()

# Chart 5: churn by payment method
sns.barplot(x="PaymentMethod", y="ChurnValue", data=df)
plt.title("Churn Rate by Payment Method")
plt.ylabel("Churn Rate")
plt.gca().yaxis.set_major_formatter(PercentFormatter(1.0))
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("churn_by_payment.png")
plt.show()
