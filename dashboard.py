import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# PAGE CONFIGURATION
# -------------------------------
st.set_page_config(page_title="Medical Insurance Dashboard", layout="wide")
st.title("🏥 MEDICAL INSURANCE COST ANALYSIS DASHBOARD")

# -------------------------------
# LOAD DATA
# -------------------------------
DATA_PATH = "clean_data.csv"
df = pd.read_csv(DATA_PATH)

# -------------------------------
# SIDEBAR FILTERS
# -------------------------------
st.sidebar.header("🔎 Filters")
age_min, age_max = st.sidebar.slider("Select Age Range", int(df["Age"].min()), int(df["Age"].max()), (20, 60))
smoker_filter = st.sidebar.multiselect("Smoker Status", options=df["Smoker"].unique(), default=df["Smoker"].unique())

filtered_df = df[(df["Age"].between(age_min, age_max)) & (df["Smoker"].isin(smoker_filter))]

# -------------------------------
# OBJECTIVE 1: COMPARE INSURANCE CHARGES BETWEEN SMOKERS AND NON-SMOKERS ACCORDING TO AGE CATEGORY
# -------------------------------
st.header("OBJECTIVE 1: COMPARE INSURANCE CHARGES BETWEEN SMOKERS AND NON-SMOKERS ACCORDING TO AGE CATEGORY")

age_bins = [18, 30, 40, 50, 60, 70]
age_labels = ["18-29", "30-39", "40-49", "50-59", "60-69"]
filtered_df["Age Group"] = pd.cut(filtered_df["Age"], bins=age_bins, labels=age_labels, right=False)

fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.boxplot(data=filtered_df, x="Age Group", y="Charges", hue="Smoker", palette={"yes": "red", "no": "blue"}, ax=ax1)
ax1.set_title("Insurance Charges by Age Group and Smoker Status", fontsize=16, pad=20)
ax1.set_xlabel("Age Group")
ax1.set_ylabel("Charges")
st.pyplot(fig1)

# -------------------------------
# OBJECTIVE 2: ANALYZE THE RELATIONSHIP BETWEEN INSURANCE CHARGES AND BMI
# -------------------------------
st.header("OBJECTIVE 2: ANALYZE THE RELATIONSHIP BETWEEN INSURANCE CHARGES AND BMI")

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=filtered_df, x="BMI", y="Charges", hue="Smoker", palette={"yes": "red", "no": "blue"}, alpha=0.7, ax=ax2)
ax2.set_title("Relationship Between BMI and Insurance Charges", fontsize=16, pad=20)
ax2.set_xlabel("BMI")
ax2.set_ylabel("Charges")
st.pyplot(fig2)

# -------------------------------
# OBJECTIVE 3: ANALYZE WHETHER THERE ARE MORE SMOKERS OR NON-SMOKERS IN EACH AGE GROUP OF THE INSURED PEOPLE
# -------------------------------
st.header("OBJECTIVE 3: ANALYZE WHETHER THERE ARE MORE SMOKERS OR NON-SMOKERS IN EACH AGE GROUP OF THE INSURED PEOPLE")

fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.countplot(data=filtered_df, x="Age Group", hue="Smoker", palette={"yes": "red", "no": "blue"}, ax=ax3)
ax3.set_title("Number of Insured People by Age Group and Smoker Status", fontsize=16, pad=20)
ax3.set_xlabel("Age Group")
ax3.set_ylabel("Number of Insured People")
ax3.legend(title="Smoker", labels=["Yes", "No"])
st.pyplot(fig3)

