import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Medical Insurance Dashboard",
    layout="wide"
)

st.title("MEDICAL INSURANCE COST ANALYSIS DASHBOARD")
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
# KPI CARDS
# --------------------------------------------------
total_people = len(filtered_df)
avg_charges = filtered_df["Charges"].mean()
total_smokers = len(filtered_df[filtered_df["Smoker"] == "yes"])
total_non_smokers = len(filtered_df[filtered_df["Smoker"] == "no"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Insured", f"{total_people:,}")
col2.metric("Average Charges", f"${avg_charges:,.0f}")
col3.metric("Smokers", total_smokers)
col4.metric("Non-Smokers", total_non_smokers)

st.markdown("---")

# ==================================================
# OBJECTIVE 1
# ==================================================
st.header(
    "OBJECTIVE 1: TO COMPARE INSURANCE CHARGES BETWEEN SMOKERS AND NON-SMOKERS ACCORDING TO AGE CATEGORY"
)

charges_by_age_smoker = (
    filtered_df
    .groupby(["Age Group", "Smoker"])["Charges"]
    .mean()
    .reset_index()
)

fig1, ax1 = plt.subplots(figsize=(10, 6))

sns.barplot(
    data=charges_by_age_smoker,
    x="Age Group",
    y="Charges",
    hue="Smoker",
    palette={"yes": "red", "no": "blue"},
    ax=ax1
)

ax1.set_title(
    "Average Insurance Charges by Age Group and Smoker Status",
    fontsize=14,
    fontweight="bold"
)

ax1.set_xlabel("Age Category")
ax1.set_ylabel("Average Insurance Charges")

for container in ax1.containers:
    ax1.bar_label(container, fmt="%.0f")

st.pyplot(fig1)

st.markdown("---")

# ==================================================
# OBJECTIVE 2
# ==================================================
st.header(
    "OBJECTIVE 2: TO ANALYZE THE RELATIONSHIP BETWEEN INSURANCE CHARGES AND BMI"
)

col_left, col_right = st.columns(2)

# Male Scatter Plot
with col_left:

    male_df = filtered_df[
        filtered_df["Sex"].str.lower() == "male"
    ]

    fig2, ax2 = plt.subplots(figsize=(6, 5))

    sns.scatterplot(
        data=male_df,
        x="BMI",
        y="Charges",
        hue="Smoker",
        palette={"yes": "red", "no": "blue"},
        ax=ax2
    )

    ax2.set_title(
        "Male: BMI vs Insurance Charges",
        fontweight="bold"
    )

    ax2.set_xlabel("BMI")
    ax2.set_ylabel("Insurance Charges")

    st.pyplot(fig2)

# Female Scatter Plot
with col_right:

    female_df = filtered_df[
        filtered_df["Sex"].str.lower() == "female"
    ]

    fig3, ax3 = plt.subplots(figsize=(6, 5))

    sns.scatterplot(
        data=female_df,
        x="BMI",
        y="Charges",
        hue="Smoker",
        palette={"yes": "red", "no": "blue"},
        ax=ax3
    )

    ax3.set_title(
        "Female: BMI vs Insurance Charges",
        fontweight="bold"
    )

    ax3.set_xlabel("BMI")
    ax3.set_ylabel("Insurance Charges")

    st.pyplot(fig3)

st.markdown("---")

# ==================================================
# OBJECTIVE 3
# ==================================================
st.header(
    "OBJECTIVE 3: TO ANALYZE WHETHER THERE ARE MORE SMOKERS OR NON-SMOKERS IN EACH AGE GROUP OF THE INSURED PEOPLE"
)

fig4, ax4 = plt.subplots(figsize=(10, 6))

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

for container in ax4.containers:
    ax4.bar_label(container)

st.pyplot(fig4)
