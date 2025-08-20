# TDSGA7_5 Email: 22f1001636@ds.study.iitm.ac.in
Customer Analytics: Customer Engagement Correlation Matrix

# Seaborn Heatmap – Customer Engagement Analysis

This repository contains a professional-grade Seaborn visualization of synthetic business data, following best practices from the *Data Visualization with Seaborn* module.  

## Files in Repository
- **chart.py** → Python script that generates the Seaborn heatmap.  
- **chart.png** → Heatmap image (exactly 512x512 pixels).  
- **README.md** → This file (contains required email).  

## Email
22f1001636@ds.study.iitm.ac.in  

## Steps Followed
1. Generated realistic synthetic data representing **customer engagement across segments and channels**.  
2. Created a **Seaborn heatmap** with `sns.heatmap()`.  
3. Applied professional styling:
   - `sns.set_style("whitegrid")`
   - `sns.set_context("talk")`
   - Used `YlGnBu` color palette for clear gradients.  
4. Annotated values directly inside the heatmap for readability.  
5. Set chart size to **512x512 pixels** with `plt.figure(figsize=(8, 8))` and `dpi=64`.  
6. Exported chart as **chart.png**.  

---

## How to Reproduce
1. Clone this repository  
2. Install dependencies:
   ```bash
   pip install seaborn matplotlib pandas numpy
