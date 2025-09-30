import pandas as pd
import sqlalchemy
import os

# Read data
input_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "openmeteo_data.csv")
df = pd.read_csv(input_path)

# Transform
df['time'] = pd.to_datetime(df['time'])
df = df.dropna()  # Remove missing values
df['date'] = df['time'].dt.date
daily_avg = df.groupby('date').agg({
    'temperature_2m': 'mean',
    'precipitation': 'sum'
}).reset_index()

# Save transformed CSV
output_csv = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transformed_data.csv")
os.makedirs(os.path.dirname(output_csv), exist_ok=True)
daily_avg.to_csv(output_csv, index=False)
print(f"Transformed data saved to {output_csv}")

# Load into SQLite
db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "weather.db")
engine = sqlalchemy.create_engine(f"sqlite:///{db_path}")
daily_avg.to_sql('daily_weather', engine, if_exists='replace', index=False)
print(f"Data loaded into SQLite: {db_path}, table: daily_weather")