# API-Integration-and-Data-Visualization
COMPANY: CODTECH IT SOLUTIONS

NAME: SIDDHI TANAJI SATAV

INTERN ID: CTIS0158

DOMAIN: Python Programming

DURATION: 4 WEEEKS

MENTOR: NEELA SANTOSH

Internship Project Submission

Project Description
CODTECH Internship – Task 1
Title: Weather Data Visualization Dashboard using Python

1. Objective
Use Python to fetch real‑time weather data from a public API (OpenWeatherMap) and create visualizations using Matplotlib/Seaborn. The final output is a script plus a visualization dashboard image.

2. Tech Stack
Language: Python 3
Libraries:
requests – fetch data from OpenWeatherMap API
pandas – tabular data handling
matplotlib – plotting and layout
seaborn – styled statistical visualizations
Install dependencies:
bash
pip install requests pandas matplotlib seaborn
3. OpenWeatherMap Setup
Create a free account on OpenWeatherMap.
Generate an API key from the API keys section.
In weather_dashboard.py, set:
python
API_KEY = "YOUR_API_KEY_HERE"
The script uses the Current Weather Data endpoint with metric units.
4. Script Overview (weather_dashboard.py)
Main steps:
Configuration
List of cities (e.g., Delhi, Mumbai, Bangalore, Chennai, Kolkata, Solapur, Pune).
Base URL: http://api.openweathermap.org/data/2.5/weather.
Data Fetching
For each city, send a GET request with q, appid, and units=metric.
Extract: temperature, humidity, pressure, wind speed, and description.
Store results in a pandas.DataFrame.
Dashboard Visualizations
The script builds a 2×2 Matplotlib figure with Seaborn plots:
Scatter plot: Temperature vs Humidity, bubble size = wind speed, colored by city.
Bar plot: Temperature comparison across cities.
Box plot: Wind speed distribution by city.
Heatmap: Correlation between Temperature, Humidity, Pressure, and Wind_Speed.
Output
Shows the dashboard window.
Saves a high‑resolution image:
python
plt.savefig("weather_dashboard.png", dpi=300, bbox_inches="tight")
5. How to Run
From the folder containing weather_dashboard.py:
bash
python weather_dashboard.py
You should see:
Console logs: Fetched data for Delhi, Fetched data for Mumbai, etc.
Printed DataFrame with current weather for all cities.
A 4‑panel dashboard window and a saved file weather_dashboard.png

OUTPUT
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/b6656ba8-712f-4dce-ac1f-5f01ba3a8f32" />
