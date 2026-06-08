import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page setup
st.set_page_config(page_title="Medical Insurance Dashboard", layout="wide")
st.title("🏥 MEDICAL INSURANCE COST ANALYSIS DASHBOARD")

# Load data
df = pd.read_csv("clean_data.csv")

# Sidebar filters
st.sidebar.header("🔎 Filters")
age_min, age_max = st.sidebar.slider("Select Age Range", int(df["Age"].min()), int(df["Age"].max()), (20, 60))
smoker_filter = st.sidebar.multiselect("Smoker Status", options=df["Smoker"].unique(), default=df["Smoker"].unique())
gender_filter = st.sidebar.multiselect("Gender", options=df["Sex"].unique(), default=df["Sex"].unique())

# Apply filters
filtered_df = df[(df["Age"].between(age_min, age_max)) & 
                 (df["Smoker"].isin(smoker_filter)) &
                 (df["Sex"].isin(gender_filter))]

# ================================
# OBJECTIVE 1: COMPARE INSURANCE CHARGES BETWEEN SMOKERS AND NON-SMOKERS ACCORDING TO AGE CATEGORY (FLOW CHART)
# ================================
st.header("OBJECTIVE 1: COMPARE INSURANCE CHARGES BETWEEN SMOKERS AND NON-SMOKERS ACCORDING TO AGE CATEGORY")

# Create age groups
age_bins = [18, 30, 40, 50, 60, 70]
age_labels = ["18-29", "30-39", "40-49", "50-59", "60-69"]
filtered_df["Age Group"] = pd.cut(filtered_df["Age"], bins=age_bins, labels=age_labels, right=False)

fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.boxplot(x="Age Group", y="Charges", hue="Smoker", data=filtered_df, palette={"yes": "red", "no": "blue"}, ax=ax1)
ax1.set_title("INSURANCE CHARGES BY AGE GROUP AND SMOKER STATUS", fontsize=14, pad=15)
ax1.set_xlabel("Age Group")
ax1.set_ylabel("Insurance Charges")
st.pyplot(fig1)

# ================================
# OBJECTIVE 2: ANALYZE RELATIONSHIP BETWEEN INSURANCE CHARGES AND BMI (SCATTER PLOTS FOR MALE AND FEMALE)
# ================================
st.header("OBJECTIVE 2: RELATIONSHIP BETWEEN INSURANCE CHARGES AND BMI")

col1, col2 = st.columns(2)

with col1:
    fig2, ax2 = plt.subplots(figsize=(7, 5))
    sns.scatterplot(x="BMI", y="Charges", hue="Smoker", data=filtered_df[filtered_df["Sex"]=="male"], palette={"yes":"red","no":"blue"}, ax=ax2)
    ax2.set_title("MALE: BMI VS INSURANCE CHARGES", fontsize=12, pad=10)
    ax2.set_xlabel("BMI")
    ax2.set_ylabel("Charges")
    st.pyplot(fig2)

with col2:
    fig3, ax3 = plt.subplots(figsize=(7, 5))
    sns.scatterplot(x="BMI", y="Charges", hue="Smoker", data=filtered_df[filtered_df["Sex"]=="female"], palette={"yes":"red","no":"blue"}, ax=ax3)
    ax3.set_title("FEMALE: BMI VS INSURANCE CHARGES", fontsize=12, pad=10)
    ax3.set_xlabel("BMI")
    ax3.set_ylabel("Charges")
    st.pyplot(fig3)

# ================================
# OBJECTIVE 3: ANALYZE WHETHER THERE ARE MORE SMOKERS OR NON-SMOKERS IN EACH AGE GROUP (BAR CHART)
# ================================
st.header("OBJECTIVE 3: SMOKER STATUS BY AGE GROUP")

fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.countplot(x="Age Group", hue="Smoker", data=filtered_df, palette={"yes":"red","no":"blue"}, ax=ax4)
ax4.set_title("NUMBER OF INSURED PEOPLE BY AGE GROUP AND SMOKER STATUS", fontsize=14, pad=15)
ax4.set_xlabel("Age Group")
ax4.set_ylabel("Number of Insured People")
ax4.legend(title="Smoker", labels=["Yes", "No"])
st.pyplot(fig4)

