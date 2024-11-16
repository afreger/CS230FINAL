import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import matplotlib.pyplot as plt

# Documentation String
"""
Name: Andrew
CS230: Section 6
Data: Fast Food USA Dataset
URL: (Link to Streamlit app if posted)

Description: This program loads a dataset of fast food restaurants across the US and presents an interactive
dashboard with charts, graphs, and a map to explore restaurant locations and other trends.
"""

# [DA1] Load and clean the data
def load_data(file_path):
    """Loads and cleans the dataset, returning a DataFrame."""
    try:
        data = pd.read_csv(file_path)
        data.drop_duplicates(inplace=True)
        # Remove unnecessary columns, but keep latitude and longitude for map functionality
        data.drop(columns=['id', 'dateAdded', 'dateUpdated', 'address', 'keys', 'postalCode'], errors='ignore', inplace=True)
        data['is_chain'] = data['name'].apply(lambda x: 'Chain' if 'Chain' in str(x) else 'Independent')
        return data
    except FileNotFoundError:
        st.error("The dataset file was not found. Please make sure the file is in the correct location.")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return pd.DataFrame()

# [DA2] Sort data by state and city
def sort_data(data, sort_by="state"):
    """Sorts the data by a specified column."""
    return data.sort_values(by=sort_by)

# [PY1] Function with default parameter, called twice [DA4]
def filter_data(data, state=None, chain=None):
    """Filters the data by state and/or chain."""
    if state:
        data = data[data['province'] == state]
    if chain:
        data = data[data['name'] == chain]
    return data

# [PY2] Function returning multiple values
def get_stats(data):
    """Calculates and returns basic stats on restaurant count by state."""
    top_state = data['province'].mode()[0]
    top_city = data['city'].mode()[0]
    return top_state, top_city

# Load data
file_path = r'C:\Users\andre\Downloads\fast_food_usa.csv'  # Update the path to your file location
data = load_data(file_path)

# Sidebar for additional options
st.sidebar.title("Options")
st.sidebar.write("Use the sidebar to navigate additional options.")

# Sidebar options: Top Chain Analysis
top_chains = data['name'].value_counts().head(10).index.tolist()  # Top 10 chains by count [DA3]
selected_chain = st.sidebar.selectbox("Filter by Top Chain", ["All"] + top_chains) # [ST2]
selected_chart = st.sidebar.selectbox("Select Chart Type", ["Top Cities (Bar Chart)", "Restaurant Distribution (Histogram)"])
map_zoom = st.sidebar.slider("Map Zoom Level", min_value=5, max_value=15, value=10) # [ST3]

# Filter data based on sidebar options
if selected_chain != "All":
    data = data[data['name'] == selected_chain]

# Streamlit UI [ST4]
st.title("Fast Food Restaurant Analysis Across the United States")

# [ST1] Select a state for filtering
if not data.empty:  # Check if data is loaded
    state_options = data['province'].unique()
    selected_state = st.selectbox("Select a state to view:", state_options) #[ST1]
    filtered_data = filter_data(data, selected_state, selected_chain if selected_chain != "All" else None)

    # Display selected state's data
    st.write(f"Displaying data for {selected_state} - {selected_chain}")
    st.dataframe(filtered_data)

    # Chart display based on user selection
    if selected_chart == "Top Cities (Bar Chart)":
        # [VIZ1] Bar chart of top 10 cities with the most restaurants
        st.subheader(f"Top Cities with the Most {selected_chain if selected_chain != 'All' else 'Fast Food'} Restaurants in {selected_state}")
        city_counts = filtered_data['city'].value_counts().head(10)
        fig, ax = plt.subplots()
        city_counts.plot(kind='bar', color='lightcoral', ax=ax)
        ax.set_xlabel("City")
        ax.set_ylabel("Number of Restaurants")
        ax.set_title("Top 10 Cities with the Most Restaurants")
        st.pyplot(fig)
    elif selected_chart == "Restaurant Distribution (Histogram)":
        # [VIZ2] Histogram of restaurant distribution by city within the selected state
        st.subheader(f"Distribution of {selected_chain if selected_chain != 'All' else 'Fast Food'} Restaurants in {selected_state}")
        fig, ax = plt.subplots()
        filtered_data['city'].value_counts().plot(kind='hist', bins=20, color='teal', edgecolor='black', ax=ax)
        ax.set_title("Histogram of Restaurant Counts in {selected_state}")
        ax.set_xlabel("Number of Restaurants")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

    # [MAP] Map with custom icon and hoverable text for restaurant locations
    st.subheader(f"Map of {selected_chain if selected_chain != 'All' else 'Fast Food'} Restaurants in {selected_state}") # [ST4]

    # Ensure latitude and longitude columns are included
    if 'latitude' in filtered_data.columns and 'longitude' in filtered_data.columns:
        map_data = filtered_data[['latitude', 'longitude', 'name', 'city']].dropna()

        # Define icon data for each restaurant
        icon_data = map_data.assign(icon_data=[
            {"url": "https://img.icons8.com/ios-filled/50/000000/restaurant.png", "width": 40, "height": 40,
             "anchorY": 40}
            for _ in range(map_data.shape[0])
        ])

        # [PY5] Create an IconLayer with hover text
        layer = pdk.Layer(
            "IconLayer",
            data=icon_data,
            get_icon="icon_data",
            get_position=["longitude", "latitude"],
            get_size=4,
            pickable=True,  # Enable picking to show tooltips on hover
            tooltip={"text": "{name}\nCity: {city}"},
        )

        # Set the initial view state based on filtered data
        view_state = pdk.ViewState(
            latitude=map_data['latitude'].mean(),
            longitude=map_data['longitude'].mean(),
            zoom=map_zoom,
            pitch=45,
        )

        # Render the map
        st.pydeck_chart(pdk.Deck(
            layers=[layer],
            initial_view_state=view_state,
            tooltip=True,
        ))
    else:
        st.error("Latitude and longitude data are missing, unable to display map.")

    # [PY3] Error checking with try/except for loading statistics
    try:
        top_state, top_city = get_stats(data)
        st.write(f"State with the most restaurants: {top_state}")
        st.write(f"City with the most restaurants: {top_city}")
    except Exception as e:
        st.error(f"Error calculating stats: {e}")

    st.success("Program executed successfully.")
else:
    st.error("No data available. Please check the file path and ensure the dataset is properly loaded.")
