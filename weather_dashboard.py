import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configuration
API_KEY = 'OpenWeatherMap Key'  #Enter your key 
CITIES = ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata','Solapur', 'Pune']  
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather(city):
    """Fetch weather data for a city using OpenWeatherMap API"""
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            'City': city,
            'Temperature': data['main']['temp'],
            'Humidity': data['main']['humidity'],
            'Pressure': data['main']['pressure'],
            'Wind_Speed': data['wind']['speed'],
            'Description': data['weather'][0]['description'].title()
        }
    return None

# Fetch data for all cities
weather_data = []
for city in CITIES:
    data = fetch_weather(city)
    if data:
        weather_data.append(data)
    print(f"Fetched data for {city}")

df = pd.DataFrame(weather_data)
print("\nRaw Data:")
print(df)

# Create visualizations
plt.style.use('seaborn-v0_8')  # Modern seaborn style
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Weather Dashboard - Major Indian Cities', fontsize=16, fontweight='bold')

# 1. Temperature vs Humidity Scatter Plot
sns.scatterplot(data=df, x='Humidity', y='Temperature', hue='City', size='Wind_Speed', 
                sizes=(50, 300), palette='viridis', ax=axes[0,0])
axes[0,0].set_title('Temperature vs Humidity (Size=Wind Speed)')

# 2. Bar plot for Temperature comparison
sns.barplot(data=df, x='City', y='Temperature', palette='coolwarm', ax=axes[0,1])
axes[0,1].set_title('Temperature Comparison')
axes[0,1].tick_params(axis='x', rotation=45)

# 3. Wind Speed Box Plot
sns.boxplot(data=df, x='City', y='Wind_Speed', palette='Set2', ax=axes[1,0])
axes[1,0].set_title('Wind Speed Distribution')
axes[1,0].tick_params(axis='x', rotation=45)

# 4. Correlation Heatmap
numeric_cols = ['Temperature', 'Humidity', 'Pressure', 'Wind_Speed']
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap='RdYlBu_r', center=0, ax=axes[1,1])
axes[1,1].set_title('Weather Parameters Correlation')

plt.tight_layout()
plt.savefig('weather_dashboard.png', dpi=300, bbox_inches='tight')  # High-res PNG deliverable
plt.show()

print("\nDashboard saved as 'weather_dashboard.png'")
print("\nSample DataFrame:")
print(df.to_string(index=False))
