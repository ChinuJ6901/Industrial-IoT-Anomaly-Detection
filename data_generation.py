# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

# Generate sample data (replace this with your actual data)
np.random.seed(42)
data = pd.DataFrame({
    'Temperature': np.random.normal(25, 5, 1000),
    'Pressure': np.random.normal(100, 10, 1000),
    'Humidity': np.random.normal(50, 15, 1000)
})

# Train Isolation Forest model
model = IsolationForest(contamination=0.1)  # Adjust contamination based on anomaly threshold
model.fit(data)

# Predict anomalies
data['Anomaly'] = model.predict(data)
data['Anomaly'] = np.where(data['Anomaly'] == -1, 'Anomaly', 'Normal')

# Print anomaly counts
print(data['Anomaly'].value_counts())

# Save data with anomaly labels
data.to_csv('anomaly_data.csv', index=False)
