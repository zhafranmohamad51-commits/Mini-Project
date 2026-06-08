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

{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Xk-UylJIIDa6"
      },
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "\n",
        "st.set_page_config(page_title=\"Smoker Status by Age Group\", layout=\"wide\")\n",
        "st.title(\"🚬 Smoker Status by Age Group Analysis\")\n",
        "\n",
        "# Load the data\n",
        "df_streamlit = pd.read_csv(\"clean_data.csv\")\n",
        "\n",
        "# Define age bins and labels\n",
        "age_bins = [18, 30, 40, 50, 60, 70]\n",
        "age_labels = [\"18-29\", \"30-39\", \"40-49\", \"50-59\", \"60-69\"]\n",
        "\n",
        "# Create 'Age Group' column\n",
        "df_streamlit[\"Age Group\"] = pd.cut(\n",
        "    df_streamlit[\"Age\"], bins=age_bins, labels=age_labels, right=False\n",
        ")\n",
        "\n",
        "# Set the style and create the plot\n",
        "fig, ax = plt.subplots(figsize=(10, 7)) # Create figure and axes for matplotlib\n",
        "sns.set_theme(style=\"whitegrid\")\n",
        "\n",
        "sns.countplot(\n",
        "    data=df_streamlit,\n",
        "    x=\"Age Group\",\n",
        "    hue=\"Smoker\",\n",
        "    palette={\"yes\": \"red\", \"no\": \"blue\"},\n",
        "    ax=ax # Pass the axes to seaborn\n",
        ")\n",
        "\n",
        "ax.set_title(\n",
        "    \"Number of Insured People by Age Group and Smoker Status\",\n",
        "    fontsize=16,\n",
        "    pad=20,\n",
        ")\n",
        "ax.set_xlabel(\"Age Group\", fontsize=14)\n",
        "ax.set_ylabel(\"Number of Insured People\", fontsize=14)\n",
        "\n",
        "# Customize the legend\n",
        "ax.legend(title=\"Smoker\", labels=[\"Yes\", \"No\"])\n",
        "\n",
        "plt.tight_layout()\n",
        "st.pyplot(fig) # Display the plot in Streamlit"
      ]
    }
  ]
}
