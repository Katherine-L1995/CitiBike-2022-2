import streamlit as st
import pandas as pd  # Import pandas
import plotly.graph_objects as go
from plotly.subplots import make_subplots


page = st.sidebar.selectbox('Select an aspect of the analysis',
   ["Intro page",  "Weather component and bike usage",
  "Most popular stations",
     "Interactive map with aggregated bike trips", "Recommendations"])

####################### Import data #########################################

df = pd.read_csv('C:/Users/Kathe/NYC_CitiBike2022/CitibikeNYC/3.3_Include_Trips.csv', index_col=0)


####################### DEFINE THE PAGES ##########################


### Intro page

 if page == "Intro page":
      st.makrdown("#### This dashboard aims at providing helpful insights on the expansion problems Divvy Bikes currently face.")
 st.markdown("Right now, Divvy bikes run into a situation where customers complain about bikes not being available at certain times. This analysis will look at the potential reasons behind this. The dashboard is separated into 4 sections:")



myImage = Image.open("Divvy_Bikes.jpg")
st.image(myImage)



# Set page title
st.title("NYC-CitiBike 2022")
st.markdown("The Dashboard visualizes the Citibike Trips Taken in NYC during the 2022 year")



# ########################### DEFINE THE CHARTS ############################

############################ Memebers Vs. Casual ############################ 

member_casual_counts = df['member_casual'].value_counts()

fig = go.Figure(data=[go.Pie(
    labels=member_casual_counts.index,
    values=member_casual_counts.values,
    hole=0.3,  # Add hole to make it a donut chart
    marker=dict(colors=['lightblue', 'salmon'])
)])

fig.update_layout(
    title='Member vs. Casual Riders',
    template='plotly_dark'
)


# ########################### Rideable Type Count ############################
rideable_type_counts = df['rideable_type'].value_counts()

fig = go.Figure(data=[go.Bar(
    x=rideable_type_counts.index,
    y=rideable_type_counts.values,
    marker=dict(color='royalblue')
)])

fig.update_layout(
    title='Distribution of Bike Types',
    xaxis_title='Rideable Type',
    yaxis_title='Count',
    template='plotly_dark'
)


############### Citi Bike Stations in NYC by Popularity ########################

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

################ Citi Bike Trips Daily ###########################
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


########################## Heatmap of Trip Counts by hour and Day of the Week #################################

plt.figure(figsize=(14, 7))  # Adjust figure size
sns.heatmap(heatmap_data, cmap="YlGnBu", annot=False)  # Remove annotations

plt.title("Heatmap of Trip Counts by Hour and Day of the Week", fontsize=16)
plt.xlabel("Hour of the Day", fontsize=14)
plt.ylabel("Day of the Week", fontsize=14)
plt.xticks(rotation=0, fontsize=12)
plt.yticks(fontsize=12)

plt.show()


######################################### Citi Bike Trips Map ############################################################
path_to_html = "C:\Users\Kathe\CitiBike-2022-2\2.6 Files - Copy\2.6 Files\heatmap.html"

# Read file and keep in variable 
with open(path_to_html, 'r') as f:
    html_data = f.read()

st.header("Aggregated Bike Trips in NYC")

# Fixing typo in 'components' and passing HTML data to Streamlit component
st.components.v1.html(html_data, height=1000)

######################################### Citi Bike by season ############################################################
trips_by_season = df.groupby('season')['trips_per_day'].sum()

fig = go.Figure(data=[go.Bar(
    x=trips_by_season.index,
    y=trips_by_season.values,
    marker=dict(color='indianred')
)])

fig.update_layout(
    title='Trips by Season',
    xaxis_title='Season',
    yaxis_title='Trips Per Day',
    template='plotly_dark'
)




############################# Weather Line Chart ######################################################

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

