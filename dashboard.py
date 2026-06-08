import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Medical Insurance Dashboard", layout="wide")
st.title("🏥 Medical Insurance Cost Analysis Dashboard")

import os

# Get the directory that this current script is in
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, 'clean_data.csv')

# Load the dataframe safely
DF = pd.read_csv(DATA_PATH)

# Define filtered_df (assuming no filtering yet, will be updated later with user input)
filtered_df = DF.copy()


# First Plot: Age vs. Charges Scatter Plot
fig1, ax1 = plt.subplots()
sns.set_style('white')
sns.scatterplot(x='Age', y='Charges', hue='Smoker', data=filtered_df, ax=ax1)
plt.title('Age vs. Charges')
st.pyplot(fig1)
# Second Plot: Count of Smokers vs Non-Smokers by Age Group
# Ensure age_group is defined on the DataFrame being used for plotting
DF['age_group'] = pd.cut(DF['Age'], bins=[17, 29, 39, 49, 65], labels=['18-29', '30-39', '40-49', '50-64'])

fig2, ax2 = plt.subplots(figsize=(9, 5)) # Create a new figure for the second plot
sns.countplot(x='age_group', hue='Smoker', data=DF, palette='Set2', ax=ax2)

plt.title('Count of Smokers vs Non-Smokers by Age Group')
plt.xlabel('Age Groups')
plt.ylabel('Number of Beneficiaries')
st.pyplot(fig2)
