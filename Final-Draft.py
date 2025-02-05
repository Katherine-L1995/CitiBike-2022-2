import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image
import json
import pandas as pd
from keplergl import KeplerGl
import os
import matplotlib.pyplot as plt

# Sidebar navigation for selecting different analysis sections
page = st.sidebar.selectbox('Select an aspect of the analysis',
   ["Intro page", "Bike Usage", "Popular Stations",
    "Monthly Usage", "Interactive Map", "Recommendations"])

####################### Import data #########################################
df = pd.read_csv(r'3.3_Include_Trips.csv')

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
# Display the image

myImage = Image.open(r"CitiBike 2022.jpg")
st.image(myImage)



### Bike Usage
if page == "Intro page":
    st.markdown("Welcome to the intro page")

elif page == "Bike Usage":
    st.markdown("Bike Usage Analysis")

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
if page == "Bike Usage":
    st.markdown("### Weather Effect on Bike Usage")
    st.markdown("This section shows the weather effect on bike usage for each month, comparing classic and electric bikes.")

    # Display the image for monthly usage of classic and electric bikes
    image_path = r"Sheet 4.png"  # Path to the image
    st.image(image_path, caption="Monthly Usage: Classic vs Electric Bikes", use_column_width=True)


### Popular Stations
elif page == "Popular Stations":
    st.markdown("### Most Popular CitiBike Stations")

    ######## Top CitiBike Stations ######
    # Read the local HTML file for the map
    html_file_path = r"kepler.gl (1).html"
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Display the content as HTML in Streamlit
    st.components.v1.html(html_content, height=600)

    ### Tableau - Citi Stations ######
    image_path = r"Tableau - Citi Stations.png"
    # Load the image
    image = Image.open(image_path)
    # Display the image in Streamlit
    st.image(image, caption="CitiBike Sheet 2", use_column_width=True)

    ### **Citi Bike Trips Daily**
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    df['month'] = df['date'].dt.month
    df['month'] = df['month'].astype('int')
    df['season'] = [
    "winter" if (month == 12 or month in [1, 2, 3, 4])
    else "spring" if month in [5]
    else "summer" if month in [6, 7, 8, 9]
    else "fall"
    for month in df['month']
]
    df['value'] = 1
    df_groupby_bar = df.groupby('start_station_name', as_index=False).agg({'value': 'sum'})
    top_20 = df_groupby_bar.nlargest(20, 'value')
    fig = go.Figure(go.Bar(x = top_20['start_station_name'], y = top_20['value'], marker = {'color': top_20['value'],'colorscale': 'Blues'}))
    st.plotly_chart(fig, use_container_width=True)


### Monthly Usage
elif page == "Monthly Usage":
    st.markdown("### Monthly CitiBike Usage")

    ### **Citi Bike Trips by Season**
    csv_file_path = r"2.6 Files - Copy\2.6 Files\trips_by_season.csv"
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


    ### Tableau - CitiBike Usage by Months ######
    image_path = r"Tableau - Months.png"
    # Load the image
    image = Image.open(image_path)
    # Display the image in Streamlit
    st.image(image, caption="CitiBike by Month", use_column_width=True)

### Interactive Map
import os
import streamlit as st

if page == "Interactive Map":
    st.title("Interactive Bike Trip Map")

    # Define the path to your HTML file
    html_file_path = r"Start and End -Avg rides.html"

    # Ensure the file exists before trying to read it
    if os.path.exists(html_file_path):
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
            # Display the HTML content using Streamlit's HTML component
            st.components.v1.html(html_content, height=600)
    else:
        st.error(f"Error: HTML file not found at {html_file_path}")

    # **Time of Day Heat Map**
    st.title("Heatmap: Citibike Rider Activity")

    # Image path
    image_path = r"Screenshot.jpg"

    # Ensure the image file exists before displaying it
    if os.path.exists(image_path):
        st.image(image_path, caption="Heatmap: Citibike Rider Activity", use_column_width=True)
    else:
        st.error(f"Error: Image file not found at {image_path}")





### Recommendations

if page == "Recommendations":
    st.title("2022 CitiBike Insights")

    st.markdown("""
    - Ridership peaks during the warmer months, with the highest usage in summer through early fall.  
    - **Classic bikes** are preferred over electric bikes, likely due to lower cost, easier maintenance, and wider availability.  
    - **Electric bikes**, however, maintain steadier ridership year-round, suggesting they are more commonly used for commuting rather than leisure.
    """)

    # **Popular Stations**
    st.header("Popular Stations")

    st.subheader("Columbus Circle & Central Park")
    st.markdown("""
    - This area experiences the highest ridership, likely due to its proximity to Central Park, a major attraction for both tourists and locals who prefer cycling in a car-free environment.  
    - Analyzing ridership on the opposite side of Central Park could provide insights into potential expansion or station redistribution.
    """)

    st.subheader("Battery Park & Teardrop Park")
    st.markdown("""
    - These locations form a high-ridership cluster, likely due to their scenic routes and safe, open spaces for both leisure riders and commuters.
    """)

    # **Recommendations & Insights**
    st.header("Recommendations & Insights")

    st.subheader("Expand CitiBike Stations in Central Park’s Lesser-Used Areas")
    st.markdown("""
    - Investigate demand on the other side of the park to determine if station placement influences usage.
    """)

    st.subheader("Enhance Infrastructure for Electric Bike Commuters")
    st.markdown("""
    - To further improve accessibility and daily use for commuters who live further away from Manhattan, more charging stations could be added in commuter-heavy areas, such as near subway stations.  
    - Increasing the availability of e-bikes in these areas could also improve year-round ridership, leading to higher subscriptions and overall growth in the New York Metro Area.
    """)

    st.subheader("Encourage Leisure Riding in Scenic Areas")
    st.markdown("""
    - Given the popularity of Battery Park and Teardrop Park, CitiBike could promote designated cycling routes through these areas to attract more riders.  
    - Additionally, launching CitiBike tours in these scenic locations—where customers can rent and reserve bikes in advance—would enhance brand visibility and organically increase ridership.
    """)

    # **Challenges & Potential Solutions**
    st.header("Challenges & Potential Solutions")

    st.subheader("Potential Bottlenecks in Bike Distribution")
    st.markdown("""
    - **Issue:** Popular stations experience frequent shortages, while lower-usage stations may have idle bikes.  
    - **Solution:** Implement a dynamic bike redistribution strategy to optimize availability at high-demand locations.
    """)

    st.subheader("Seasonal Adjustments")
    st.markdown("""
    - **Issue:** Ridership declines in colder months, especially for classic bikes.  
    - **Solution:** Scale back classic bike availability while maintaining strong e-bike access near commuter-heavy stations.
    """)

    # **Improving CitiBike Distribution in NYC**
    st.header("Improving CitiBike Distribution in NYC")

    st.subheader("Expanding CitiBike Stations in Boroughs Outside of Manhattan")
    st.markdown("""
    - Increasing CitiBike availability in Brooklyn and Queens could improve commuting options into Manhattan.  
    - **Opportunity:** Partner with apartment complexes to offer electric bikes for tenants, providing a low-cost rental program as an alternative to public transit.  
    - **Advantage:** Indoor storage solutions for bikes during winter months, along with dedicated charging stations, would improve accessibility.
    """)

    st.subheader("Incentivizing Balanced Bike Distribution")
    st.markdown("""
    - Since bike availability is unequal at pickup and drop-off locations, CitiBike could introduce:  
      - A **points-based rewards system** or **discounted rides** for users who drop off bikes at underutilized stations.  
      - **Real-time traffic comparisons** in the CitiBike app to encourage biking over rideshare options like Uber.
    """)

    st.subheader("Setting Up Temporary CitiBike Stations in High-Demand Areas")
    st.markdown("""
    - **Solution:** Deploy temporary docking stations during peak hours and weekends to alleviate shortages at certain locations.  
    - **Benefit:** Allows CitiBike’s analytics team to measure demand and optimize station placement dynamically.
    """)

