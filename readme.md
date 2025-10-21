# 🏙️ Capstone Project Module 2 — Daegu Apartment Price Prediction  

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Modeling-orange?logo=scikit-learn)
![XGBoost](https://img.shields.io/badge/XGBoost-Regression-green?logo=xgboost)
![EDA](https://img.shields.io/badge/EDA-Data%20Visualization-blueviolet?logo=plotly)

### 👩‍💻 Author: Caroline 
### 🧾 Dataset: Daegu Apartment Dataset  
### 🕒 Project Duration: 15 days  

---

## 📌 Problem Statement  
As the number of apartment units in Daegu continues to grow, **determining the right selling price** becomes increasingly critical to remain competitive while maintaining profit margins.  

This project aims to identify the **key factors driving apartment prices** and develop a **machine learning model** that can accurately predict sale prices based on physical and locational attributes.

---

## 🎯 Objectives  
- Develop a predictive model for apartment sale prices using regression algorithms.  
- Provide **data-driven insights** into which property features most influence price.  
- Help **developers** and **investors** set fair, competitive prices.  
- Minimize prediction errors (**RMSE**, **MAE**, **MAPE**) for optimal model accuracy.

---

## 💼 Business Impact  
**For Developers:** Set optimal pricing and design features that increase property value.  
**For Buyers/Investors:** Identify undervalued units with high potential ROI.  
**For Financial Institutions:** Improve property valuation accuracy for lending and appraisal.

---

## 📊 Dataset Overview  
- **Total Records:** 4,123 apartment listings in Daegu  
- **After Cleaning:** 2,671 unique listings (duplicates & outliers removed)  
- **Key Features:**  
  `Size_m2`, `Age`, `HallwayType`, `TimeToSubway_min`,  
  `N_FacilitiesInApt`, `N_Parkinglot(Basement)`, `SubwayStation`  
- **Target Variable:** `SalePrice`

---

## 🧹 Data Preparation & Feature Engineering  
- Normalized `TimeToSubway` categories (e.g., “0–5min”, “10–15min”, “no_subway”).  
- Used **OneHotEncoder** for categorical variables.  
- Applied **log transformation** on skewed features (`Size_m2`, `Age`, `TimeToSubway_min`).  
- Addressed **multicollinearity** (high VIF > 10) through tree-based modeling.  
- Transformed target using `log1p(SalePrice)` for better distribution balance.  

---

## 🔍 Exploratory Data Analysis (EDA)

| Feature | Correlation (ρ) with SalePrice |
|----------|-------------------------------:|
| `Size_m2` | **+0.66** |
| `HallwayType_terraced` | **+0.65** |
| `N_FacilitiesInApt` | +0.57 |
| `N_Parkinglot(Basement)` | +0.56 |
| `Age` | **−0.50** |
| `TimeToSubway_min` | **−0.44** |

> 🧠 *Larger, newer, and terraced-hallway apartments near subway stations command significantly higher prices.*

---

## 🤖 Modeling & Evaluation  

### 📦 Algorithms Tested  
| Model | Mean RMSE | Mean MAE | Mean MAPE |
|-------|-----------:|----------:|----------:|
| Linear Regression | 49,178 | 39,689 | 19.6% |
| KNN Regressor | 48,444 | 38,100 | 18.9% |
| DecisionTree Regressor | 46,395 | 36,866 | 18.3% |
| **RandomForest Regressor** | **46,248** | **36,783** | **18.2%** |
| **XGBoost Regressor** | 46,278 | 36,817 | 18.3% |

> ✅ **Best Benchmark Model:** RandomForest Regressor  

---

### 🔧 Hyperparameter Tuning (XGBoost)
**Best Parameters:**  
`subsample=0.8, reg_lambda=2.0, n_estimators=300, min_child_weight=3, max_depth=3, learning_rate=0.05, colsample_bytree=1.0`

---

### 🧮 Final Model Performance (Test Set)

| Model | RMSE | MAE | MAPE | R² |
|-------|------:|-----:|-----:|----:|
| RandomForest (Benchmark) | 47,739 | 38,200 | 18.81% | 0.785 |
| **XGB Tuned** | **47,463** | **37,996** | **18.69%** | **0.788** |

> 🟢 **Train–Test Gap:** ~6–8% → Model is **balanced**, not overfitted.  
> 📈 **R² ≈ 0.78–0.82:** Explains ~80% of price variability.  

---

## 🌲 Feature Importance (Tree-Based)

| Rank | Feature | Importance (%) |
|------|----------|---------------:|
| 1 | `HallwayType_terraced` | 27.99 |
| 2 | `Size_m2` | 23.98 |
| 3 | `log_Size_m2` | 22.96 |
| 4 | `N_Parkinglot(Basement)` | 6.55 |
| 5 | `Age` | 5.06 |
| 6 | `log_Age` | 4.55 |

> 🧩 Architectural design and unit size are the top price determinants, followed by building age and parking facilities.

---

## 📈 Visualization Highlights  
- **Actual vs Predicted SalePrice (Test Set)** shows tight clustering near the ideal line.  
- Dense price range between **180–250K** — the most accurately predicted region.  
- Minor “regression to mean” at extremes: underestimation of luxury units, slight overestimation of cheaper ones.

---

## 🧩 Conclusions  
1. **Unit Size**, **Hallway Type**, **Building Age**, and **Subway Proximity** are the strongest drivers of apartment prices in Daegu.  
2. **RandomForest/XGBoost** models achieved the best predictive accuracy (RMSE ≈ 47K, MAPE ≈ 18.7%).  
3. The model shows **no overfitting** (train–test gap < 10%) and generalizes well to unseen data.  
4. Location effects remain important but are distributed across multiple dummy features.  

---

## 💼 Business Recommendations  

### 🏗️ For Developers
- Focus on **terraced hallway designs** and **basement parking** to raise property value.  
- Prioritize **medium-to-large units** within **5 minutes of premium subway stations** (e.g., Banwoldang, Kyungbuk Uni Hospital).  
- Renovate older buildings to reduce *effective age* and boost resale price.  

### 💰 For Buyers & Investors
- Target **older or mixed-hallway** apartments near subways — often undervalued.  
- Avoid distant locations unless discounts are substantial.  

### 🏛️ For Policymakers
- Strengthen **public transport connectivity** to enhance property values.  
- Establish **minimum facility standards** (parking, amenities) to ensure equitable area growth.  

---

## ⚙️ Technical Recommendations  
- Add **geospatial coordinates** (lat/long, distance to CBD or schools).  
- Use **target encoding** for categorical variables like `SubwayStation`.  
- Explore **LightGBM / CatBoost** for faster training and improved interpretability.  
- Implement **Quantile Regression** to provide price range forecasts (p10–p90).  

---

## 🚀 Next Steps  
- Develop a **Streamlit or Dash web app** for interactive price predictions.  
- Package model via **API deployment** (`pickle` / `Flask`).  
- Test performance using new Daegu housing data (2024–2025).  

---

## 🔗 References  
- Daegu Apartment Dataset – Kaggle / UCI Repository  
- Scikit-Learn & XGBoost Documentation  
- Seaborn, Matplotlib – EDA Visualizations  

---

## 💬 Summary  
This project analyzes apartment data from Daegu, Korea to uncover the key features driving housing prices and builds a predictive model using XGBoost and RandomForest.  
The final tuned XGBoost model achieves **RMSE ≈ 47K** and **MAPE ≈ 18.7%**, with consistent generalization and no overfitting.  
Results highlight the importance of **unit size, architectural type, building age, and subway proximity**, providing actionable insights for developers, investors, and policymakers.

---

