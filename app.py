import gradio as gr
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# 1. Generate Synthetic Training Data
np.random.seed(42)
n_samples = 500

df_sim = pd.DataFrame({
    'LAT': np.random.uniform(35.05, 35.15, n_samples),
    'LON': np.random.uniform(129.00, 129.15, n_samples),
    'SOG_Knots': np.random.uniform(0, 18, n_samples),
    'Is_Anchored': np.random.choice([0, 1], size=n_samples, p=[0.7, 0.3]),
    'Hour': np.random.randint(0, 24, n_samples),
    'DayOfWeek': np.random.randint(0, 7, n_samples),
    'Wind_Speed_Knots': np.random.uniform(5, 35, n_samples),
    'Wave_Height_m': np.random.uniform(0.5, 4.0, n_samples),
    'Weather_Risk_Index': np.random.uniform(1.0, 5.0, n_samples),
    'Local_Port_Density': np.random.randint(0, 10, n_samples),
    'Is_Peak_Hours': np.random.choice([0, 1], size=n_samples)
})

# Target Variables
df_sim['Delay_Hours'] = (
    0.5 * df_sim['Weather_Risk_Index'] + 
    0.8 * df_sim['Local_Port_Density'] + 
    2.0 * df_sim['Is_Anchored'] + 
    np.random.normal(0, 0.5, n_samples)
).clip(lower=0)

df_sim['Extra_CO2_Tons'] = (df_sim['Delay_Hours'] * 1.8 + np.random.normal(0, 0.2, n_samples)).clip(lower=0)

# Train Models
features = [
    'LAT', 'LON', 'SOG_Knots', 'Is_Anchored', 'Hour', 'DayOfWeek', 
    'Wind_Speed_Knots', 'Wave_Height_m', 'Weather_Risk_Index', 
    'Local_Port_Density', 'Is_Peak_Hours'
]

X = df_sim[features]
model_delay = RandomForestRegressor(n_estimators=50, random_state=42).fit(X, df_sim['Delay_Hours'])
model_co2 = RandomForestRegressor(n_estimators=50, random_state=42).fit(X, df_sim['Extra_CO2_Tons'])

# Prediction Function
def predict_maritime_metrics(lat, lon, sog, is_anchored, hour, wind, wave, density):
    weather_risk = round((wind / 35.0 * 2.5) + (wave / 4.0 * 2.5), 2)
    is_peak = 1 if (6 <= hour <= 10 or 16 <= hour <= 20) else 0
    day_of_week = 2
    
    input_data = pd.DataFrame([[
        lat, lon, sog, int(is_anchored), hour, day_of_week, 
        wind, wave, weather_risk, density, is_peak
    ]], columns=features)
    
    pred_delay = model_delay.predict(input_data)[0]
    pred_co2 = model_co2.predict(input_data)[0]
    
    wasted_fuel = pred_co2 / 3.114
    estimated_cost = (wasted_fuel * 600) + (pred_delay * 250)
    
    risk_level = "🟢 LOW RISK" if pred_delay < 1.5 else ("🟠 MEDIUM RISK" if pred_delay < 3.5 else "🔴 HIGH RISK")
    
    return (
        f"{risk_level}",
        f"{pred_delay:.2f} Hours",
        f"{pred_co2:.2f} Tons",
        f"${estimated_cost:.2f} USD"
    )

# Gradio Interface
app = gr.Interface(
    fn=predict_maritime_metrics,
    inputs=[
        gr.Slider(35.05, 35.15, value=35.10, label="Latitude (Busan Port)"),
        gr.Slider(129.00, 129.15, value=129.08, label="Longitude"),
        gr.Slider(0, 20, value=8.5, label="Vessel Speed (SOG Knots)"),
        gr.Checkbox(label="Is Vessel Anchored?"),
        gr.Slider(0, 23, value=14, step=1, label="Arrival Hour (0-23)"),
        gr.Slider(0, 40, value=18.0, label="Wind Speed (Knots)"),
        gr.Slider(0.0, 5.0, value=1.8, label="Wave Height (Meters)"),
        gr.Slider(0, 12, value=4, step=1, label="Local Port Vessel Density (2km Radius)")
    ],
    outputs=[
        gr.Textbox(label="Port Risk Status"),
        gr.Textbox(label="Predicted Arrival Delay"),
        gr.Textbox(label="Predicted Extra CO2 Emissions"),
        gr.Textbox(label="Estimated Financial Impact")
    ],
    title="🚢 MARITIME-X: Busan Port Decision Support System",
    description="Explainable AI Framework for Predicting Port Congestion, ESG Carbon Emissions, and Operational Idle Costs."
)

if __name__ == "__main__":
    app.launch()
