# 🚢 MARITIME-X: Busan Port Decision Support & Carbon Monitoring System

[![Hugging Face Space](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Live%20Dashboard-blue)](https://huggingface.co/spaces/shruttijadon/maritime-x-dashboardd)
[![Python](https://img.shields.io/badge/Python-3.10%2B-green)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> An Explainable AI (XAI) and Decision Support framework designed for **Busan Port Authority (BPA)** to predict vessel arrival delays, optimize port operations, and quantify ESG carbon emissions and operational idle costs.

---

## 📌 Project Overview

Port congestion and idle vessel anchorage contribute significantly to operational inefficiency and excess maritime carbon emissions. **Maritime-X** leverages machine learning algorithms trained on simulated spatial-temporal and oceanographic features (AIS-derived data, weather parameters, and port density) to deliver predictive insights for port authorities and fleet managers.

### Key Objectives:
* ⏱️ **Congestion & Delay Prediction:** Estimate vessel idle delay times (in hours) at Busan Port.
* 🌿 **ESG Carbon Accounting:** Calculate excess $\text{CO}_2$ tonnage generated during idle burn.
* 💰 **Financial Impact Estimation:** Translate delays and wasted fuel into real-time operational costs ($ USD).
* 🚦 **Risk Categorization:** Provide an actionable 3-tier risk status (Low, Medium, High Risk) for incoming maritime traffic.

---

## 🛠️ Architecture & Tech Stack

* **Language:** Python 3.10+
* **Data Processing & ML:** `pandas`, `numpy`, `scikit-learn` (Random Forest Regressors)
* **Interactive Dashboard:** HTML5 / CSS3 / JavaScript (Client-side WASM & ML Inference Engine)
* **Deployment:** Hugging Face Spaces

---

## 📊 Feature Variables & Methodology

The model takes into account key spatial-temporal and environmental parameters:

| Feature Variable | Description |
| :--- | :--- |
| **Latitude / Longitude** | Geolocation coordinates around Busan Port |
| **Vessel Speed (SOG Knots)** | Speed Over Ground in knots |
| **Anchorage Status** | Boolean flag indicating whether the vessel is anchored |
| **Arrival Hour & Day** | Temporal tracking to account for peak hours |
| **Wind Speed & Wave Height** | Oceanographic weather inputs driving the Weather Risk Index |
| **Local Port Vessel Density** | Traffic density within a 2km radius |

---

## 🚀 Live Demo

You can interact with the live deployed model without running any local code:

👉 **[Launch Maritime-X Live Interactive Dashboard](https://huggingface.co/spaces/shruttijadon/maritime-x-dashboardd)**

---

## 💻 Local Setup & Installation

To run this repository locally or experiment with the Jupyter Notebook:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/shruttijadon/maritime-x-busan-esg.git](https://github.com/shruttijadon/maritime-x-busan-esg.git)
   cd maritime-x-busan-esg
