
import pandas as pd

df = pd.read_csv("data.csv", skiprows=4) 

print(df.head())

import matplotlib.pyplot as plt

# Mock data from the image
labels = ['0-20 Years', '21-64 Years', '65+ Years']
values = [513, 807, 98]  # in millions
colors = ['#FFEB3B', '#03A9F4', '#E91E63']

# Convert labels to numeric positions (simulate bins)
x_positions = [10, 42.5, 70]  # Midpoints for each age group

# Plot histogram-like bar chart
plt.bar(x_positions, values, width=20, color=colors, edgecolor='black')

# Label formatting
plt.xticks(x_positions, labels)
plt.title("India's Population Distribution by Age in 2022")
plt.xlabel("Age Range")
plt.ylabel("Population (in Millions)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
plt.savefig(" india population ")
