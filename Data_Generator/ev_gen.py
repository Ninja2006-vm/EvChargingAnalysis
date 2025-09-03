import numpy as np
import pandas as pd
np.random.seed(42)
stations = [f"S{i}" for i in range(1, 51)]  
cities = ["Bengaluru", "Mumbai", "Delhi", "Pune"]
dates = pd.date_range("2025-01-01", "2025-09-03", freq="D")

data = []
for date in dates:
    for station in stations:
        sessions = np.random.randint(20, 60)
        for _ in range(sessions):
            city = np.random.choice(cities)
            kWh = np.round(np.random.normal(25, 5), 2)
            duration = int(np.random.normal(45, 10))
            price = np.random.choice([7.5, 8, 8.5, 9])
            revenue = np.round(kWh * price, 2)
            peak = np.random.choice([True, False], p=[0.6, 0.4])
            data.append([station, city, date, kWh, duration, price,
                         revenue, peak])

df = pd.DataFrame(data, columns=["station_id", "city", "date",
                                 "kWh_consumed", "duration_mins", 
                                 "price_per_kWh",
                                 "revenue", "peak_hours"])

df.to_csv("abc.csv", index=False)
print(f"Dataset saved to {"abc.csv"} with {df.shape[0]} rows.")