import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Dashboard Setup
# -------------------------------
st.set_page_config(page_title="Medical Insurance Dashboard", layout="wide")
st.title("🏥 Medical Insurance Cost Analysis Dashboard")

# Load Data
DATA_PATH = "clean_data.csv"
df = pd.read_csv(DATA_PATH)

# -------------------------------
# Sidebar Filters
# -------------------------------
st.sidebar.header("🔎 Filters")
age_range = st.sidebar.slider("Select Age Range", int(df["Age"].min()), int(df["Age"].max()), (20, 60))
smoker_filter = st.sidebar.multiselect("Smoker Status", options=df["Smoker"].unique(), default=df["Smoker"].unique())

filtered_df = df[(df["Age"].between(age_range[0], age_range[1])) & (df["Smoker"].isin(smoker_filter))]

# -------------------------------
# Objective 1: Age vs Charges
# -------------------------------
st.subheader("📊 Objective 1: Age vs. Charges")
fig1, ax1 = plt.subplots()
sns.scatterplot(x="Age", y="Charges", hue="Smoker", data=filtered_df, ax=ax1, palette="coolwarm")
ax1.set_title("Age vs. Charges", fontsize=14)
ax1.set_xlabel("Age")
ax1.set_ylabel("Charges")
st.pyplot(fig1)

# -------------------------------
# Objective 2: Smokers vs Non-Smokers by Age Group
# -------------------------------
st.subheader("🚬 Objective 2: Smoker Status by Age Group")
age_bins = [18, 30, 40, 50, 60, 70]
age_labels = ["18-29", "30-39", "40-49", "50-59", "60-69"]
df["Age Group"] = pd.cut(df["Age"], bins=age_bins, labels=age_labels, right=False)

fig2, ax2 = plt.subplots(figsize=(9, 5))
sns.countplot(x="Age Group", hue="Smoker", data=df, palette={"yes": "red", "no": "blue"}, ax=ax2)
ax2.set_title("Number of Insured People by Age Group and Smoker Status", fontsize=14)
ax2.set_xlabel("Age Group")
ax2.set_ylabel("Count")
ax2.legend(title="Smoker")
st.pyplot(fig2)

# -------------------------------
# Objective 3: BMI vs Charges
# -------------------------------
st.subheader("⚖️ Objective 3: BMI vs. Charges")
fig3, ax3 = plt.subplots()
sns.scatterplot(x="BMI", y="Charges", hue="Smoker", data=filtered_df, ax=ax3, palette="Set1")
ax3.set_title("BMI vs. Charges", fontsize=14)
ax3.set_xlabel("BMI")
ax3.set_ylabel("Charges")
st.pyplot(fig3)

# -------------------------------
# Dashboard Notes
# -------------------------------
st.markdown("""
### ✅ Dashboard Features
- Interactive filters for **Age Range** and **Smoker Status**
- Clear titles, axis labels, and legends
- Multiple objectives visualized with different plots
- Clean layout with sidebar navigation
""")
