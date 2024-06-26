import streamlit as st
from slidebar import sideBar
from lifeline_streamlit.home_page import home_page
import altair as alt

from pages.prediction_page import progress_page
from pages.analytics_page import analytics_page

# Page configuration
st.set_page_config(
    page_title="KSP Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded"
)

alt.themes.enable("dark")

# CSS styling
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# st.sidebar.title("Navigation")
# selected = st.sidebar.radio("Go to", ["Home", "Predicted Spot", "Analytics"])

# Main
df_lat_lon_filtered,selected_district,selected_color_theme, analytics_option = sideBar()

# if selected == "Home":
#     try:
#         home_page(df_lat_lon_filtered,selected_district,selected_color_theme)
#     except Exception as e:
#         st.warning(f"An error occurred: {e}")

# elif selected == "Predicted Spot":
#     try:
#         progress_page(df_lat_lon_filtered)
#     except Exception as e:
#         st.warning(f"An error occurred: {e}")

# elif selected == "Analytics":
#     try:
#         if analytics_option:
#             analytics_page(analytics_option)
#         else:
#             analytics_page()
#     except Exception as e:
#         st.warning(f"An error occurred: {e}")