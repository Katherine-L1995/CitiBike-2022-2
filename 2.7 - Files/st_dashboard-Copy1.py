import streamlit as st
import pandas as pd  # Import pandas
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image
import seaborn as sns


page = st.sidebar.selectbox('Select an aspect of the analysis',
   ["Intro page",  "Weather component and bike usage",
  "Most popular stations",
     "Interactive map with aggregated bike trips", "Recommendations"])

####################### Import data #########################################

df = pd.read_csv('C:\\Users\\Kathe\\CitiBike-2022-2\\3.3_Include_Trips.csv')


####################### DEFINE THE PAGES ##########################


### Intro page

if page == "Intro page":
    st.markdown("#### This dashboard aims at providing helpful insights on the expansion problems Divvy Bikes currently face.")
    st.markdown("Right now, Divvy bikes run into a situation where customers complain about bikes not being available at certain times. This analysis will look at the potential reasons behind this. The dashboard is separated into 4 sections:")



myImage = Image.open(r"C:\Users\Kathe\CitiBike-2022-2\CitiBike 2022.jpg")
# Display the image
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


# Show the figure
fig.show()

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

# Show the figure
fig.show()

########################## Heatmap of Trip Counts by hour and Day of the Week #################################
# Path to your saved heatmap
image_path = r"C:\Users\Kathe\CitiBike-2022-2\2.4\heatmap.png"

# Upload and display the heatmap image
st.image(image_path, caption="Heatmap of Trip Counts by Hour and Day of the Week")

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

# Show the figure
fig.show()

######################################### Citi Bike Trips Map ############################################################
path_to_html = "C:\\Users\\Kathe\\CitiBike-2022-2\\2.6 Files - Copy\\2.6 Files\\heatmap.html"


# Read file and keep in variable 
with open(path_to_html, 'r') as f:
    html_data = f.read()

st.header("Aggregated Bike Trips in NYC")

# Fixing typo in 'components' and passing HTML data to Streamlit component
st.components.v1.html(html_data, height=1000)

# Show the figure
fig.show()


######################################### Citi Bike by season ############################################################

# Define the correct path to your CSV file
csv_file_path = r"C:\Users\Kathe\CitiBike-2022-2\2.6 Files - Copy\2.6 Files\trips_by_season.csv"

fig = make_subplots(specs = [[{"secondary_y": True}]])

# Add the first trace (Daily bike rides)
fig.add_trace(
    go.Scatter(
        x=df['date'], 
        y=df['trips_per_day'], 
        name='Daily bike rides', 
        marker={'color': 'blue'}  # Use a single color
    ),
    secondary_y=False  # Primary y-axis
)

# Add the second trace (Daily temperature)
fig.add_trace(
    go.Scatter(
        x=df['date'], 
        y=df['avgTemp'], 
        name='Daily temperature', 
        marker={'color': 'red'}  # Use a single color
    ),
    secondary_y=True  # Secondary y-axis
)

# Show the figure
fig.show()
############################# Weather Line Chart ######################################################

fig.add_trace(
 go.Scatter(x = df['date'], y = df['trips_per_day'], name = 'Daily bike rides', 
 marker={'color': df['trips_per_day'],'color': 'blue'}),
 secondary_y = False)
fig.add_trace(
 go.Scatter(x=df['date'], y = df['avgTemp'], name = 'Daily temperature', 
 marker={'color': df['avgTemp'],'color': 'red'}),
 secondary_y=True)

# Show the figure
fig.show()


# Display the plot in the Streamlit app
st.plotly_chart(fig, use_container_width=True)

