import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Load your data
combined_data = pd.read_csv('dashboard/main_data.csv')

# Set the page layout to wide
st.set_page_config(layout="wide")

# Title for the app
st.title("Air Quality Data Analysis")

# Sidebar for selecting the pollutant to analyze
pollutant = st.sidebar.selectbox("Select a Pollutant", ['PM2.5', 'PM10', 'NO2', 'CO'])

# Layout for different sections (split in columns)
col1 = st.columns(1)[0]  # Only one column

with col1:
    # Function to plot trends and moving averages
    st.subheader(f"Trends and Moving Averages for {pollutant}")
    
    def plot_trends(data, pollutant):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(data.index, data[pollutant], label=pollutant, color='blue')
        ax.set_title(f'{pollutant} Trends Over Time')
        ax.set_ylabel('Concentration (µg/m³)')
        ax.legend()
        st.pyplot(fig)
        
        # Moving average
        data[f'{pollutant}_MA'] = data[pollutant].rolling(window=30).mean()
        fig_ma, ax_ma = plt.subplots(figsize=(10, 6))
        ax_ma.plot(data.index, data[f'{pollutant}_MA'], label=f'{pollutant} Moving Average', color='blue')
        ax_ma.set_title(f'Moving Average of {pollutant} Over Time')
        ax_ma.set_ylabel('Concentration (µg/m³)')
        ax_ma.legend()
        st.pyplot(fig_ma)
        
        # Linear regression for trends
        X = data.index.values.reshape(-1, 1)  # Use the index as the independent variable
        y = data[pollutant].values  # Target variable
        model = LinearRegression().fit(X, y)
        st.write(f"Slope (Trend in {pollutant}): {model.coef_[0]}")
    
    plot_trends(combined_data, pollutant)

# Split seasonal patterns and heatmaps into two columns
col3, col4 = st.columns(2)

with col3:
    st.subheader("Seasonal Patterns in Air Quality")
    
    # Sidebar to select pollutant for seasonal analysis
    seasonal_pollutant = st.sidebar.selectbox("Select a Pollutant for Seasonal Analysis", ['PM2.5', 'PM10', 'NO2', 'CO'])
    
    # Plot monthly averages
    def plot_monthly_avg(data, pollutant):
        monthly_avg = data.groupby('month').mean(numeric_only=True)[[pollutant]]
        fig, ax = plt.subplots(figsize=(10, 6))
        monthly_avg.plot(kind='bar', ax=ax)
        ax.set_title(f'Monthly Average of {pollutant}')
        ax.set_ylabel('Concentration')
        st.pyplot(fig)
    
    plot_monthly_avg(combined_data, seasonal_pollutant)

with col4:
    st.subheader(f"Heatmap of {seasonal_pollutant} Levels by Month and Hour")
    
    # Heatmap for patterns by month and hour
    def plot_heatmap(data, pollutant):
        pivot_table = data.pivot_table(values=pollutant, index='month', columns='hour', aggfunc='mean')
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.heatmap(pivot_table, cmap="coolwarm", annot=False, ax=ax)
        ax.set_title(f'{pollutant} Levels by Month and Hour')
        st.pyplot(fig)
    
    plot_heatmap(combined_data, seasonal_pollutant)
