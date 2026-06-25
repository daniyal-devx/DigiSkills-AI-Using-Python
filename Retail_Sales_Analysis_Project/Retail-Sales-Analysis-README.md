# 📊 Retail Sales Analysis — EDA Project

> Exploratory Data Analysis on a retail sales dataset as part of the **DigiSkills AI Using Python** course.

---

## 📁 Files

| File | Description |
|------|-------------|
| `retail_sales_analysis_project.ipynb` | Main analysis notebook |
| `retail_sales.csv` | Dataset (1,825 rows × 6 columns) |

---

## 📋 Dataset Overview

| Column | Type | Description |
|--------|------|-------------|
| `Date` | datetime | Transaction date (Jan–Dec 2023) |
| `Category` | string | Product category (Electronics, Clothing, etc.) |
| `Sales` | float | Revenue per transaction |
| `Quantity` | int | Units sold |
| `Profit` | float | Profit per transaction |
| `Region` | string | Sales region (North, South, East, West) |

---

## 🔍 Analysis Performed

- **Data Cleaning** — null value handling, type conversion, datetime feature extraction
- **Statistical Summary** — descriptive stats by category and region
- **Monthly Trend Analysis** — sales & profit across all 12 months
- **Category Performance** — revenue and profit margin by product type
- **Regional Analysis** — sales distribution pie chart across 4 regions
- **Day-of-Week Pattern** — identifying peak sales days
- **Correlation Heatmap** — relationships between numerical features
- **4-Chart Business Dashboard** — combined summary visualization
- **Key Insights & Recommendations** — actionable business findings

---

## 📦 Requirements

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

---

## ▶️ How to Run

```bash
jupyter notebook retail_sales_analysis_project.ipynb
```

Or open directly in [Google Colab](https://colab.research.google.com/) — no setup needed.

---

*Part of [DigiSkills-AI-Using-Python](https://github.com/daniyal-devx/DigiSkills-AI-Using-Python) · by [@daniyal-devx](https://github.com/daniyal-devx)*
