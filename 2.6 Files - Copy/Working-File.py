import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image

# Sidebar navigation for selecting different analysis sections
page = st.sidebar.selectbox('Select an aspect of the analysis',
   ["Intro page", "Bike Usage", "Popular Stations",
    "Monthly Usage", "Interactive Map", "Recommendations"])

####################### Import data #########################################
df = pd.read_csv(r'C:\Users\Kathe\CitiBike-2022-2\3.3_Include_Trips.csv')

####################### DEFINE THE PAGES ##########################

### Intro page
if page == "Intro page":
    st.markdown("#### Welcome to the CitiBike Analysis Dashboard")
    st.markdown("This dashboard provides insights into bike usage, popular stations, seasonal trends, and recommendations based on CitiBike data in NYC for 2022.")
    st.markdown("The dashboard is divided into the following sections:")

    st.markdown("1. **Bike Usage**: Analyzing rider demographics, bike types, and weather impacts.")
    st.markdown("2. **Popular Stations**: A look at the most frequently used stations.")
    st.markdown("3. **Monthly Usage**: Trends in bike trips across months and seasons.")
    st.markdown("4. **Interactive Map**: Explore bike trips across NYC.")
    st.markdown("5. **Recommendations**: Suggestions for improving CitiBike service.")

    # You can also add an introductory image here
    intro_image = Image.open(r"C:\Users\Kathe\CitiBike-2022-2\Intro_Page_Image.jpg")
    st.image(intro_image, caption="CitiBike 2022 Overview", use_column_width=True)


### Bike Usage
elif page == "Bike Usage":
    st.markdown("### Weather Component and Bike Usage Analysis")

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

### Popular Stations
elif page == "Popular Stations":
    st.markdown("### Most Popular CitiBike Stations")

    ######## Top CitiBike Stations ######
    # Read the local HTML file for the map
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

### Monthly Usage
elif page == "Monthly Usage":
    st.markdown("### Monthly CitiBike Usage")

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

    ### Tableau - CitiBike Usage by Months ######
    image_path = r"C:\Users\Kathe\Tableau - Months.png"
    # Load the image
    image = Image.open(image_path)
    # Display the image in Streamlit
    st.image(image, caption="CitiBike by Month", use_column_width=True)

### Interactive Map
elif page == "Interactive Map":
    st.markdown("### Interactive Map of Bike Trips")
    
    ######## Interactive Map ######
    image_path = r"C:\Users\Kathe\CitiBike-2022-2\Interactive_Map.png"
    # Load the image
    image = Image.open(image_path)
    # Display the image in Streamlit
    st.image(image, caption="Interactive Map", use_column_width=True)

### Recommendations
elif page == "Recommendations":
    st.markdown("### Recommendations for CitiBike Expansion")

    # Display the image for recommendations or any other insights
    myImage = Image.open(r"C:\Users\Kathe\CitiBike-2022-2\Recommendation_Insights.jpg")
    st.image(myImage)
