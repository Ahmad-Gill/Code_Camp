# -*- coding: utf-8 -*-
"""medical_data_visualizer.py.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16ZOVTzxr3U_tIU3FR5-FhCJ3p1amhp5d
"""

# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import the data from medical_examination.csv and assign it to the df variable
df = pd.read_csv('medical_examination.csv')

# Create the overweight column in the df variable
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Draw the Categorical Plot
def draw_cat_plot():
    # Create a DataFrame for the cat plot using pd.melt
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data in df_cat to split it by cardio and show the counts of each feature
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().to_frame('total').reset_index()

    # Rename one of the columns for the catplot to work correctly
    df_cat = df_cat.rename(columns={'variable': 'variable', 'value': 'value', 'total': 'total'})

    # Convert the data into long format and create a chart using seaborn's catplot
    fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar').fig

    # Return the figure for the output
    return fig


# Clean the data in the df_heat variable
def draw_heat_map():
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = (corr.triu() == 1)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # Plot the correlation matrix using seaborn's heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap='coolwarm', linewidths=0.5, square=True, ax=ax)

    # Return the figure for the output
    return fig