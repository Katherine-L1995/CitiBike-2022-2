import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image

# Sidebar navigation
page = st.sidebar.selectbox('Select an aspect of the analysis',
   ["Intro page", "Weather component and bike usage",
    "Most popular stations",
    "Interactive map with aggregated bike trips", "Recommendations"])




####################### Import data #########################################

df = pd.read_csv(r'C:\Users\Kathe\CitiBike-2022-2\3.3_Include_Trips.csv')

####################### DEFINE THE PAGES ##########################





### Intro page
if page == "Intro page":
    st.markdown("#### This dashboard aims at providing helpful insights on the expansion problems Divvy Bikes currently face.")
    st.markdown("Right now, Divvy bikes run into a situation where customers complain about bikes not being available at certain times. This analysis will look at the potential reasons behind this. The dashboard is separated into 4 sections:")




# Display the image
myImage = Image.open(r"C:\Users\Kathe\CitiBike-2022-2\CitiBike 2022.jpg")
st.image(myImage)




# Set page title
st.title("NYC-CitiBike 2022")
st.markdown("The Dashboard visualizes the Citibike Trips Taken in NYC during the 2022 year")




# ########################### DEFINE THE CHARTS ############################

### **Member vs. Casual Riders**
member_casual_counts = df['member_casual'].value_counts()

fig1 = go.Figure(data=[go.Pie(
    labels=member_casual_counts.index,
    values=member_casual_counts.values,
    hole=0.3,  
    marker=dict(colors=['lightblue', 'salmon'])
)])
fig1.update_layout(title='Member vs. Casual Riders', template='plotly_dark')

st.plotly_chart(fig1, use_container_width=True)




### **Rideable Type Count**
rideable_type_counts = df['rideable_type'].value_counts()

fig2 = go.Figure(data=[go.Bar(
    x=rideable_type_counts.index,
    y=rideable_type_counts.values,
    marker=dict(color='royalblue')
)])
fig2.update_layout(
    title='Distribution of Bike Types',
    xaxis_title='Rideable Type',
    yaxis_title='Count',
    template='plotly_dark'
)

st.plotly_chart(fig2, use_container_width=True)




######## Top CitiBike Stations ######

# Read the local HTML file

html_file_path = "C:/Users/Kathe/CitiBike-2022-2/kepler.gl (1).html"

with open(html_file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Display the content as HTML in Streamlit
st.components.v1.html(html_content, height=600)

### Tableau - Citi Stations ######

image_path = r"C:\Users\Kathe\Tableau - Citi Stations.png"

# Load the image
image = Image.open(image_path)

# Display the image in Streamlit
st.image(image, caption="CitiBike Sheet 2", use_column_width=True)



### **Citi Bike Trips Daily**
fig3 = make_subplots(specs=[[{"secondary_y": True}]])
fig3.add_trace(
    go.Scatter(x=df['date'], y=df['trips_per_day'], name='Daily bike rides', marker={'color': 'blue'}),
    secondary_y=False
)
fig3.add_trace(
    go.Scatter(x=df['date'], y=df['avgTemp'], name='Daily temperature', marker={'color': 'red'}),
    secondary_y=True
)
fig3.update_layout(title='Daily Citi Bike Trips & Temperature')

st.plotly_chart(fig3, use_container_width=True)



### Tableau - Citibike Usage by Months ######

image_path = r"C:\Users\Kathe\Tableau - Months.png"
# Load the image
image = Image.open(image_path)

# Display the image in Streamlit
st.image(image, caption="CitiBike by Month", use_column_width=True)



### **Citi Bike Trips by Season**
csv_file_path = r"C:\Users\Kathe\CitiBike-2022-2\2.6 Files - Copy\2.6 Files\trips_by_season.csv"

fig4 = make_subplots(specs=[[{"secondary_y": True}]])
fig4.add_trace(
    go.Scatter(x=df['date'], y=df['trips_per_day'], name='Daily bike rides', marker={'color': 'blue'}),
    secondary_y=False
)
fig4.add_trace(
    go.Scatter(x=df['date'], y=df['avgTemp'], name='Daily temperature', marker={'color': 'red'}),
    secondary_y=True
)
fig4.update_layout(title='Bike Trips by Season')

st.plotly_chart(fig4, use_container_width=True)




### **Weather Line Chart**
fig5 = make_subplots(specs=[[{"secondary_y": True}]])
fig5.add_trace(
    go.Scatter(x=df['date'], y=df['trips_per_day'], name='Daily bike rides', marker={'color': 'blue'}),
    secondary_y=False
)
fig5.add_trace(
    go.Scatter(x=df['date'], y=df['avgTemp'], name='Daily temperature', marker={'color': 'red'}),
    secondary_y=True
)
fig5.update_layout(title='Weather Impact on Bike Usage')

st.plotly_chart(fig5, use_container_width=True)


