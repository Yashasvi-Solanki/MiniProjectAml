# Applied Machine Learning: Dual-Pipeline Project

This repository contains a comprehensive dual-pipeline machine learning project focused on demonstrating applied workflows for both Continuous Regression and Multinomial Classification. 

## Project Overview

### 1. Continuous Regression (Diamonds Dataset)
- **Goal:** Predict the continuous market price of diamonds based on their physical characteristics (carat, depth, table, x, y, z, cut, color, clarity).
- **Techniques:** 
  - One-Hot Encoding (`pd.get_dummies` with `drop_first=True`) to handle categorical features and prevent multicollinearity.
  - Linear Regression baseline.
  - L1 (Lasso) and L2 (Ridge) Regularization for feature selection and stabilization.

### 2. Multinomial Classification (Water Potability Dataset)
- **Goal:** Classify water samples into 3 distinct potability tiers (Unsafe, Marginal, Safe).
- **Techniques:**
  - Target discretization using `pandas.qcut()`.
  - Strict anti-leakage train/test splitting prior to scaling and resampling.
  - Handling extreme class imbalance using **SMOTE** (Synthetic Minority Over-sampling Technique) applied strictly to the training partition.
  - Implementation of diverse algorithms including Logistic Regression (SAGA/LBFGS solvers), Decision Trees, Random Forests, K-Nearest Neighbors, and XGBoost.
  - Performance evaluation using Accuracy, Precision, Recall, Weighted F1-Scores, and Macro-Average ROC Curves.

## Repository Contents
- `miniproject.ipynb`: The main Jupyter Notebook containing the full end-to-end Python implementation, from data preprocessing and modeling to evaluation visualizations.
- `ProjectReport.tex`: The professional LaTeX source code for the comprehensive project report.

## How to Compile the Report
To compile the `ProjectReport.tex` file into a PDF:
1. Run all cells in `miniproject.ipynb` to generate the `.png` visualizations.
2. Export the notebook to PDF and save it as `miniproject.pdf` in the same directory.
3. Compile the `.tex` file using any standard LaTeX engine (or upload the folder to Overleaf).
