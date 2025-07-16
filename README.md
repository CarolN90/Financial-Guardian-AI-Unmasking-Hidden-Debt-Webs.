![Enterprise-Automation-and-its-Elements](https://github.com/user-attachments/assets/235d57be-3308-43f6-8d1f-76c5433daa7e)


## Financial Guardian AI: Unmasking Hidden Debt Webs. 


##  GROUP 9 Members

- Caroline Wachira.
- Godwine Wasonga.
- Naomi Ngigi.
- Elvis Kiprono.
- Janine Makorra
- Trevor Maina.

## Introduction


The AI-driven loan stacking detection model is a vital solution for mitigating significant risks in Kenya's digital lending sector, aiming to improve credit decisions, safeguard borrowers, and foster responsible lending.


##  Problem Statement
Digital lenders operating in isolation lack the tools to detect loan stacking behavior before issuing loans as they lack visibility into borrowers’ full credit behavior.

This leads to:
- Increased default rates
- Increased operational losses
- Regulatory and compliance concerns

There is a pressing need for a smart, data-driven system that can detect loan stacking patterns early and support more responsible lending decisions.

---

##  Business Objective

This project aims to use behavioral borrower data to:
- Identify and flag high-risk borrowers engaging in loan stacking
- Enable early detection before loan disbursement
- Support responsible and inclusive lending across digital platforms

---

##  Dataset Overview

We used a synthetic dataset simulating mobile lending behavior in Kenya. Key features include:

- `loan_amount`
- `repayment_ratio`
- `apps_installed`
- `loans_last_30_days`
- `employment_status`
- `location_type`
- `default_risk` (target)

The dataset was preprocessed to clean, scale, and encode the features, reducing dimensionality from 20 to 15 features after transformation.

---

##  Project Approach

1. **Data Simulation** — Modeling mobile lending patterns using realistic behavioral features
2. **Exploratory Data Analysis (EDA)** — Understanding default signals through visualizations
3. **Neural Network Modeling** — Training a classifier to detect loan stacking risk
4. **Model Evaluation** — Measuring accuracy, recall, and interpretability
5. **API Development** — Deploying the model using FastAPI for real-time scoring
6. **Testing** — Simulating loan applicants through test inputs

---

## Business Analysis
- Loan Default Rate by Employment Status
!<Figure size 1000x700 with 1 Axes><img width="923" height="624" alt="image" src="https://github.com/user-attachments/assets/14d6ce31-1407-4725-9f8d-45cfe9297efc" />

"Hourly", "Casual", "Unemployed" appear to pose higher default risk

 
- Loan Amount Distributions by   Default Status
!<Figure size 1000x600 with 1 Axes><img width="876" height="547" alt="image" src="https://github.com/user-attachments/assets/c769534e-ecc0-4528-b2d4-943ec54f3e13" />

Investigates if users will default based on loan amount.
Shows that loan defaults are more common among lower loan amounts.
Shows that borrowers taking smaller loans are in more financial distress or have less capacity to pay.
  

-Number of active loans for defaulted vs non-defaulted users
!<Figure size 1000x600 with 1 Axes><img width="841" height="547" alt="image" src="https://github.com/user-attachments/assets/99f04e0b-0d1d-4690-812f-62340c765705" />

Offers insight on loan defaults and potential loan stacking behavior.
Users engaged in loan stacking have elevated risk of defaulting on their loans.
Number of active loans is a powerful predictor of default risk.


## Evaluation

-**Model Comparison**
!<Figure size 720x432 with 1 Axes><img width="675" height="387" alt="image" src="https://github.com/user-attachments/assets/82829341-b848-449c-9857-9ce18768bef2" />

**Model Comparison Interpretation**

1.Random Forest and XGBoost:
Mean Accuracy: 94%
Standard Deviation: 0.00
The models achieved perfect classification across all 5 folds.

2.Neural Net (MLP)
Mean Accuracy: ~92%
Standard Deviation: ~0.46%

3.SVM & Logistic Regression
Mean accuracy :92%

-**Confusion Matrix**

!<Figure size 432x288 with 1 Axes><img width="380" height="278" alt="image" src="https://github.com/user-attachments/assets/ee6de049-8581-49ab-b6ea-6cb1e9ec3b47" />

**Confusion Matrix Findings**

True Negatives (TN)= 1410 → Correctly identified non-loan stackers
False Positives (FP)=48 → Incorrectly flagged 48 safe borrowers as risky
False Negatives (FN)= 78 →   Missed 78 actual loan stackers
True Positives (TP)= 464 → Correctly identified 464 loan stackers


---

##  Results Summary

- Neural network model successfully detects high-risk stacking behavior
- Key predictive signals include:
  - High number of loans in the last 30 days
  - Low repayment ratio
  - Higher app usage
- Accuracy and recall were significantly improved over baseline models

---

## Conclusions

The project yields the following key insights:

-Critical Hidden Risk: Loan stacking poses a significant, often undetected, risk within Kenya's digital lending market, leading directly to higher default rates for borrowers managing multiple concurrent loans.

-Effective Data-Driven Solution: Utilizing borrower behavioral data enables the early detection of risky patterns, and an intelligent, data-driven system demonstrably enhances credit decision-making prior to loan issuance.

-Lender Financial Protection: This proactive approach directly supports responsible lending practices, which in turn leads to a significant reduction in operational losses for financial institutions.

-Strengthened Ecosystem: Collaborative efforts among lenders, facilitated by such a system, are crucial for increasing market visibility and collectively safeguarding the stability and integrity of the broader digital lending ecosystem.

---

## Recommendations

To address loan stacking effectively and promote a robust digital lending environment, the following actions are recommended:

-Implement Advanced Risk Analytics: Deploy AI-driven tools that leverage comprehensive behavioral data for real-time risk assessment, automatic flagging of suspicious activity, and continuous model adaptation with regular retraining.

-Foster Collaborative Data Sharing: Establish secure and ethical data-sharing mechanisms among lenders to enhance collective visibility into borrower behavior and improve joint risk management.

-Prioritize Ethical Lending & Transparency: Promote responsible borrowing through borrower education and ensure transparent credit decision-making processes to build and maintain borrower trust.

-Ensure Regulatory Alignment: Actively engage with regulators to ensure that the detection system adheres to evolving credit policies and promotes fair practices while protecting consumers.


---

## Next Steps

To advance the loan stacking detection system from concept to impactful deployment, the following steps are crucial:

-Pilot Program & Testing: Initiate a pilot program to test the real-time API in a controlled environment with key stakeholders.

-Scalability & Security Audits: Conduct comprehensive audits to ensure the system is scalable for high volumes and secure to protect sensitive data.

-Model Enhancement & Ethical AI: Continuously improve the model through advanced feature engineering, exploration of new data sources, and proactive bias detection and mitigation.

-Operational Integration & Training: Develop thorough training programs and documentation to enable lenders and risk teams to effectively utilize and integrate the API into their workflows.

---






## A minimal, end-to-end **Streamlit** dashboard that wraps the AI-driven **Loan-Stacking Detection** model trained in the Jupyter notebook.

---

## 📦 Prerequisites

1. **Python 3.8+**
2. **Trained artifacts** (generated by the notebook):
   ```
   utils/preprocessor.pkl
   models/model_keras.h5
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Quick Start

1. **Clone / copy this folder** (should contain `app.py`, `utils/`, `models/` and `requirements.txt`).  
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Launch the app**:
   ```bash
   streamlit run app.py
   ```
4. Your browser opens at `http://localhost:8501`.

---

## 📁 File Tree

```
loan-stacking-streamlit/
├── app.py                 
├── utils/
│   └── preprocessor.pkl   
├── models/
│   └── model_keras.h5  # Keras model
├── requirements.txt
└── README.md
```

---

## 📋 requirements.txt

```
streamlit==1.37.0
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.5.1
tensorflow==2.17.0
joblib==1.4.2
```

---

## 🖥️ Using the App

1. Fill in or upload a CSV with customer features (column names must match training).  
2. Click **Predict**.  
3. Results table + download link appear instantly.

---



## 🤝 Troubleshooting

- **Blank screen / 404** → check port `8501` is free or pass `--server.port 8502`.  
- **Model not found** → ensure `utils/` and `models/` folders are in the same directory as `app.py`.  
- **TensorFlow GPU warnings** → harmless; suppress with `export TF_CPP_MIN_LOG_LEVEL=2`.

---

Happy stacking detection!
