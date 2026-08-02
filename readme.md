# 🚢 MARITIME-X: Busan Port Decision Support & Carbon Monitoring System

> **Important Note**  
> This is a **prototype research project** developed using **simulated data** for educational and exploratory purposes.  
> Real-world data validation is planned as future work.

[![Hugging Face Space](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Live%20Dashboard-blue)](https://huggingface.co/spaces/shruttijadon/maritime-x-dashboardd)
[![Python](https://img.shields.io/badge/Python-3.10%2B-green)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Overview

**MARITIME-X** is an Explainable AI (XAI) prototype designed to support decision-making in port operations.

The system focuses on:
- Predicting vessel arrival delays
- Estimating ESG-related carbon emissions due to idle time
- Providing interpretable insights for port authorities

This project explores how machine learning combined with explainability techniques (SHAP) can be applied to maritime logistics and sustainable port management.

---

## Key Objectives

- Predict vessel idle/delay times at port
- Estimate excess carbon emissions caused by delays
- Quantify potential operational cost impact
- Provide risk categorization (Low / Medium / High)
- Demonstrate the use of Explainable AI in industrial decision support

---

## Methodology

### Approach
- **Machine Learning Model:** XGBoost (Gradient Boosting)
- **Explainability:** SHAP (SHapley Additive exPlanations)
- **Interface:** Interactive web dashboard

### Model Details
- Algorithm: XGBoost Regressor
- Purpose: Predict vessel delay time (in hours)
- Input: Spatial, temporal, vessel, and weather-related features
- Output: Predicted delay + risk category + estimated carbon impact

### Data
The current version uses **simulated data** generated based on publicly available patterns related to:
- Busan Port operations
- Vessel characteristics
- Weather conditions

Real operational data integration is planned as future work.

### Features Used
| Feature | Description |
|---------|-------------|
| Latitude / Longitude | Geolocation around Busan Port |
| Vessel Speed (SOG) | Speed Over Ground |
| Anchorage Status | Whether the vessel is anchored |
| Arrival Hour & Day | Temporal patterns |
| Wind Speed & Wave Height | Weather conditions |
| Local Port Vessel Density | Traffic density nearby |

---

## Extra Features

- **Risk Classification:** Automatically categorizes vessels into Low / Medium / High risk based on predicted delay
- **Carbon Estimation Module:** Estimates excess CO₂ emissions caused by idle time
- **Cost Impact Estimation:** Provides approximate operational cost impact of delays
- **Explainability Layer:** Uses SHAP to show which factors most influence the prediction
- **Interactive Dashboard:** Real-time input and visualization of results

---

## Dashboard Features

The interactive dashboard includes:

- Input panel for vessel and environmental parameters
- Real-time delay prediction
- Risk level indicator (Low / Medium / High)
- Estimated carbon emission display
- Feature contribution visualization (SHAP-based)
- Clean and responsive user interface

*(Some visual elements and transitions are included to improve user experience)*

---

## Current Status

This is a **prototype system**. The following components have been implemented:

- Feature engineering pipeline
- XGBoost-based delay prediction model
- SHAP-based explainability module
- Interactive dashboard with basic animations and visual feedback

**Note:** Performance metrics and impact quantifications will be reported after validation on real-world data.

---

## Limitations

- Developed using simulated data only
- Not yet validated on real AIS / berth / operational data
- Performance numbers are not available at this stage
- Not tested on extreme events (typhoons, major disruptions)

---

## Future Work

- Integrate real-world data from Busan Port (AIS, berth occupancy, weather, vessel records)
- Retrain and validate models on actual operational data
- Conduct detailed SHAP and error analysis
- Explore Digital Twin integration for port operations
- Improve dashboard interactivity and visualization
- Extend the framework toward multi-port generalization

---

## Tech Stack

- **Language:** Python 3.10+
- **Libraries:** pandas, numpy, scikit-learn, XGBoost, SHAP
- **Dashboard:** Streamlit / HTML + JavaScript
- **Deployment:** Hugging Face Spaces

---

## Live Demo

👉 [Launch Maritime-X Interactive Dashboard](https://huggingface.co/spaces/shruttijadon/maritime-x-dashboardd)

---

## Contact

**Shruti Jadon**  
B.Tech Computer Science Engineering (AI & ML)  
Email: shrutijadon1306@gmail.com  
GitHub: [github.com/shruttijadon](https://github.com/shruttijadon)  
Portfolio: [shruttijadon.github.io](https://shruttijadon.github.io)
