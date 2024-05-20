import streamlit as st
import altair as alt
import plotly.express as px
from streamlit_folium import st_folium
from slidebar import sideBar
from clustermap_severity import create_cluster_map
from map_road_type import map_road_type

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

df_lat_lon_filtered,selected_district,selected_color_theme, analytics_option = sideBar()

# def make_choropleth(input_df, input_id, input_column, input_color_theme):
#     choropleth = px.choropleth(input_df, locations=input_id, color=input_column,
#                                color_continuous_scale=input_color_theme)
#     choropleth.update_layout(
#         template='plotly_dark',
#         plot_bgcolor='rgba(0, 0, 0, 0)',
#         paper_bgcolor='rgba(0, 0, 0, 0)',
#         margin=dict(l=0, r=0, t=0, b=0),
#         height=350
#     )
#     return choropleth

st.markdown('## Karnataka State Police Dashboard')

with st.expander("🧭 My database"):
        shwdata = st.multiselect('Filter:', df_lat_lon_filtered.columns, default=[])
        if shwdata:
            st.dataframe(df_lat_lon_filtered[shwdata], use_container_width=True)
        else:
            st.dataframe(df_lat_lon_filtered, use_container_width=True)

col1, col2, col3, col4 = st.columns(4, gap="medium")

with col1:
        st.markdown('#### Total Accidents')
        total_accidents = df_lat_lon_filtered['Latitude'].count()
        st.metric(label="Total Accidents", value=total_accidents)

with col2:
        df_accident_count = df_lat_lon_filtered.groupby('DISTRICTNAME').size().reset_index(name='accident_count')
        highest_accidents_district = df_accident_count.loc[df_accident_count['accident_count'].idxmax()]
        st.markdown('#### Highest Accidents City')
        st.metric(label=highest_accidents_district['DISTRICTNAME'], value=highest_accidents_district['accident_count'])

with col3:
        st.markdown('#### Total Fatal Injuries')
        total_fatal_injuries = df_lat_lon_filtered[df_lat_lon_filtered['Severity'] == 'Fatal'].shape[0]
        st.metric(label="Total Fatal Injuries", value=total_fatal_injuries)

with col4:
        st.markdown('#### Migration Difference')
        # Placeholder for migration difference or other relevant metrics
        st.metric(label="Migration Difference", value="N/A")

cols = st.columns((2,3.5, 3.5), gap='medium')
with cols[0]:
        st.markdown('#### Top Districts by Accident Count')
        df_accident_count_sorted = df_accident_count.sort_values(by='accident_count', ascending=False)
        st.dataframe(df_accident_count_sorted,
                     column_order=["district", "accident_count"],
                     hide_index=True,
                     width=None,
                     column_config={
                         "district": st.column_config.TextColumn("District"),
                         "accident_count": st.column_config.ProgressColumn(
                             "Accident Count",
                             format="%d",
                             min_value=0,
                             max_value=max(df_accident_count_sorted.accident_count),
                         )
                     }
                     )

with cols[1]:
        st.markdown('#### Road Map')
        map_folium = map_road_type(df_lat_lon_filtered)
        # st_folium(map_folium, width=700, height=500)
        st.plotly_chart(map_folium, use_container_width=True, height=500)

        st.markdown('### Number of Accidents Per Year')
        # Aggregate data by year
        df_yearly_accidents = df_lat_lon_filtered.groupby('Year').size().reset_index(name='Total Accidents')

        # Create the column chart using Altair
        bar_chart = alt.Chart(df_yearly_accidents).mark_bar().encode(
            x=alt.X('Year:O', title='Year'),
            y=alt.Y('Total Accidents:Q', title='Number of Accidents'),
            tooltip=['Year', 'Total Accidents']
        ).properties(
            title='Number of Accidents Per Year',
            width=600,
            height=400
        )

        st.altair_chart(bar_chart, use_container_width=True)

        # heatmap = make_heatmap(df_lat_lon_filtered, 'Year', 'DISTRICTNAME', 'severity', selected_color_theme)
        # st.altair_chart(heatmap, use_container_width=True)

with cols[2]:
        
        st.markdown('#### Severity Map')
        map_folium = create_cluster_map(df_lat_lon_filtered,selected_district)
        st_folium(map_folium, width=700, height=440)

        
        

        # st.markdown('#### Choropleth Map')
        # # Adjust this line based on actual data and requirements for visualization
        # choropleth = make_choropleth(df_lat_lon_filtered, 'DISTRICTNAME', 'severity', selected_color_theme)
        # st.plotly_chart(choropleth, use_container_width=True)

        with st.expander('About', expanded=True):
            st.write('''
                - Data: [U.S. Census Bureau](https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-total.html).
                - :orange[**Gains/Losses**]: states with high inbound/ outbound migration for selected year
                - :orange[**States Migration**]: percentage of states with annual inbound/ outbound migration > 50,000
            ''')

# Utility functions
# def make_heatmap(input_df, input_y, input_x, input_color, input_color_theme):
#     heatmap = alt.Chart(input_df).mark_rect().encode(
#         y=alt.Y(f'{input_y}:O', axis=alt.Axis(title="Year", titleFontSize=18, titlePadding=15, titleFontWeight=900, labelAngle=0)),
#         x=alt.X(f'{input_x}:O', axis=alt.Axis(title="", titleFontSize=18, titlePadding=15, titleFontWeight=900)),
#         color=alt.Color(f'{input_color}:N',
#                         legend=None,
#                         scale=alt.Scale(scheme=input_color_theme)),
#         stroke=alt.value('black'),
#         strokeWidth=alt.value(0.25),
#     ).properties(width=900).configure_axis(
#         labelFontSize=12,
#         titleFontSize=12
#     )
#     return heatmap





