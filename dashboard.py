import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Medical Insurance Dashboard",
    layout="wide"
)

st.title("🏥 MEDICAL INSURANCE COST ANALYSIS DASHBOARD")
st.markdown("---")

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "clean_data.csv")

df = pd.read_csv(DATA_PATH)

# --------------------------------------------------
# CREATE AGE GROUPS
# --------------------------------------------------
age_bins = [18, 30, 40, 50, 60, 70]
age_labels = ["18-29", "30-39", "40-49", "50-59", "60-69"]

df["Age Group"] = pd.cut(
    df["Age"],
    bins=age_bins,
    labels=age_labels,
    right=False
)

# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------
st.sidebar.header("FILTERS")

gender_filter = st.sidebar.multiselect(
    "Gender",
    options=df["Sex"].unique(),
    default=df["Sex"].unique()
)

smoker_filter = st.sidebar.multiselect(
    "Smoker Status",
    options=df["Smoker"].unique(),
    default=df["Smoker"].unique()
)

filtered_df = df[
    (df["Sex"].isin(gender_filter)) &
    (df["Smoker"].isin(smoker_filter))
]

# --------------------------------------------------
# OBJECTIVE 1
# --------------------------------------------------
st.header(
    "OBJECTIVE 1: TO COMPARE INSURANCE CHARGES BETWEEN SMOKERS AND NON-SMOKERS ACCORDING TO AGE CATEGORY"
)

fig1, ax1 = plt.subplots(figsize=(10,6))

sns.boxplot(
    data=filtered_df,
    x="Age Group",
    y="Charges",
    hue="Smoker",
    palette="Set2",
    ax=ax1
)

ax1.set_title(
    "Insurance Charges by Age Group and Smoker Status",
    fontsize=14,
    fontweight="bold"
)

ax1.set_xlabel("Age Category")
ax1.set_ylabel("Insurance Charges")

st.pyplot(fig1)

st.markdown("---")

# --------------------------------------------------
# OBJECTIVE 2
# --------------------------------------------------
st.header(
    "OBJECTIVE 2: TO ANALYZE THE RELATIONSHIP BETWEEN INSURANCE CHARGES AND BMI"
)

col1, col2 = st.columns(2)

# Male Scatter Plot
with col1:

    male_df = filtered_df[
        filtered_df["Sex"].str.lower() == "male"
    ]

    fig2, ax2 = plt.subplots(figsize=(6,5))

    sns.scatterplot(
        data=male_df,
        x="BMI",
        y="Charges",
        hue="Smoker",
        ax=ax2
    )

    ax2.set_title(
        "Male: BMI vs Insurance Charges",
        fontweight="bold"
    )

    st.pyplot(fig2)

# Female Scatter Plot
with col2:

    female_df = filtered_df[
        filtered_df["Sex"].str.lower() == "female"
    ]

    fig3, ax3 = plt.subplots(figsize=(6,5))

    sns.scatterplot(
        data=female_df,
        x="BMI",
        y="Charges",
        hue="Smoker",
        ax=ax3
    )

    ax3.set_title(
        "Female: BMI vs Insurance Charges",
        fontweight="bold"
    )

    st.pyplot(fig3)

st.markdown("---")

# --------------------------------------------------
# OBJECTIVE 3
# --------------------------------------------------
st.header(
    "OBJECTIVE 3: TO ANALYZE WHETHER THERE ARE MORE SMOKERS OR NON-SMOKERS IN EACH AGE GROUP OF THE INSURED PEOPLE"
)

fig4, ax4 = plt.subplots(figsize=(10,6))

sns.countplot(
    data=filtered_df,
    x="Age Group",
    hue="Smoker",
    palette={"yes": "red", "no": "blue"},
    ax=ax4
)

ax4.set_title(
    "Number of Insured People by Age Group and Smoker Status",
    fontsize=14,
    fontweight="bold"
)

ax4.set_xlabel("Age Group")
ax4.set_ylabel("Number of Insured People")

st.pyplot(fig4)
