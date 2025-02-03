import streamlit as st
import pandas as pd  # Import pandas
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page title
st.title("NYC-CitiBike 2022")
st.markdown("The Dashboard visualizes the Citibike Trips Taken in NYC during the 2022 year")


####################### Import data #########################################

df = pd.read_csv('C:/Users/Kathe/NYC_CitiBike2022/CitibikeNYC/3.3_Include_Trips.csv', index_col=0)

# ########################### DEFINE THE CHARTS ############################

## Bar chart 

### Citi Bike Stations in NYC by Popularity ###

df['value'] = 1
df_groupby_bar = df.groupby('start_station_name', as_index=False).agg({'value': 'sum'})
top_20 = df_groupby_bar.nlargest(20, 'value')


fig = go.Figure(go.Bar(x=top_20['start_station_name'], y=top_20['value'], 
                      marker={'color': top_20['value'], 'colorscale': 'Blues'}))

fig.update_layout(
    title='Top 20 most popular bike stations in NYC',
    xaxis_title='Start stations',
    yaxis_title='Sum of trips',
    width=900, height=600
)
st.plotly_chart(fig, use_container_width=True)

### Citi Bike Trips Daily ###
fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(
    go.Scatter(x=df['date'], y=df['trips_per_day'], name='Daily bike rides',
               marker={'color': 'blue'}),
    secondary_y=False
)

fig.add_trace(
    go.Scatter(x=df['date'], y=df['avgTemp'], name='Daily temperature',
               marker={'color': 'red'}),
    secondary_y=True
)

### Citi Bike Trips Map ###
path_to_html = "C:/Users/Kathe/Downloads/Stations_3.5_kepler.gl/Stations_3.5_kepler.gl.html"

# Read file and keep in variable 
with open(path_to_html, 'r') as f:
    html_data = f.read()

st.header("Aggregated Bike Trips in NYC")

# Fixing typo in 'components' and passing HTML data to Streamlit component
st.components.v1.html(html_data, height=1000)

##### Weather Line Chart ######

fig = make_subplots(specs = [[{"secondary_y": True}]])

# Set up the figure with subplots for secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add the first trace (e.g., daily bike rides)
fig.add_trace(
    go.Scatter(x=df['date'], y=df['trips_per_day'], name='Daily bike rides',
               marker={'color': 'blue'}),
    secondary_y=False  # This traces goes on the first y-axis
)

# Add the second trace (e.g., daily temperature)
fig.add_trace(
    go.Scatter(x=df['date'], y=df['avgTemp'], name='Daily temperature',
               marker={'color': 'red'}),
    secondary_y=True  # This trace goes on the secondary y-axis
)

# Update layout for the chart
fig.update_layout(
    title='Daily Bike Rides and Temperature in NYC',
    xaxis_title='Date',
    yaxis_title='Bike Rides',
    yaxis2_title='Temperature (°C)',
    width=900, height=600
)

# Display the plot in the Streamlit app
st.plotly_chart(fig, use_container_width=True)

