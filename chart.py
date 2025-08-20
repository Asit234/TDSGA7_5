# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic business data - customer engagement (hours per week × segments)
segments = ["High Value", "Medium Value", "Low Value", "New Customers", "Churn Risk"]
channels = ["Email", "Social Media", "Website", "Mobile App", "In-Store"]

# Create synthetic engagement scores (20–100)
data = np.random.randint(20, 100, size=(len(segments), len(channels)))
df = pd.DataFrame(data, index=segments, columns=channels)

# Apply Seaborn styling best practices
sns.set_style("whitegrid")
sns.set_context("talk")

# Create heatmap
plt.figure(figsize=(8, 8))  # 8 inches × 64 dpi = 512 pixels
ax = sns.heatmap(
    df,
    annot=True,
    fmt="d",
    cmap="YlGnBu",
    linewidths=0.5,
    cbar_kws={"label": "Engagement Score"}
)

# Customize titles and labels
plt.title("Customer Engagement Across Segments and Channels", fontsize=14, pad=20)
plt.xlabel("Engagement Channel")
plt.ylabel("Customer Segment")

# Save chart with exact 512x512 pixels (no trimming)
plt.savefig("chart.png", dpi=64, bbox_inches=None, pad_inches=0)
plt.close()
