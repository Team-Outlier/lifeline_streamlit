import streamlit as st

def analytics_page_1():
    st.title("Temporal Analysis")
    st.components.v1.iframe(
        src="https://app.powerbi.com/view?r=eyJrIjoiYjU3ZDkzMTAtZDEyYy00MTFmLWJjZGItYzA0YzcxMDJhZTYxIiwidCI6IjUyMjVmOWFhLWJiZjctNDA2MS04YTdhLTI0OGM3M2MyNTRhOCJ9",
        width=1400,
        height=870,
        scrolling=True
    )

def analytics_page_2():
    st.title("Road Type Analysis")
    st.components.v1.iframe(
        src="https://app.powerbi.com/view?r=eyJrIjoiODAwZjYwNTYtNWI1NC00ZjEzLWEyNjItZWU4YjE2MjZjMjExIiwidCI6IjUyMjVmOWFhLWJiZjctNDA2MS04YTdhLTI0OGM3M2MyNTRhOCJ9",
        width=1400,
        height=870,
        scrolling=True
    )

    st.write("This is the content for Analytics Page 2.")

def analytics_page_3():
    st.title("Landmark Analysis")
    st.components.v1.iframe(
        src="https://app.powerbi.com/view?r=eyJrIjoiM2EwNzc2MTItMDYxZS00ZmFiLTlhZTYtMTg0YmEzZWE1YjY1IiwidCI6IjUyMjVmOWFhLWJiZjctNDA2MS04YTdhLTI0OGM3M2MyNTRhOCJ9",
        width=1400,
        height=870,
        scrolling=True
    )


def analytics_page_4():
    st.title("Road Signage Analysis")
    st.components.v1.iframe(
        src="https://app.powerbi.com/view?r=eyJrIjoiYWNkZjNkMzctNDUzNy00ZGU2LTk5NGEtMWU2YTM4YWUzOTIwIiwidCI6IjUyMjVmOWFhLWJiZjctNDA2MS04YTdhLTI0OGM3M2MyNTRhOCJ9",
        width=1400,
        height=870,
        scrolling=True
    )

def analytics_page_5():
    st.title("Pedestrian Analysis")
    st.components.v1.iframe(
        src="https://app.powerbi.com/view?r=eyJrIjoiYWQ5NDlhMjUtOWI0NS00MGU4LTkwNDYtNTc0NjQ3Nzg2NmE3IiwidCI6IjUyMjVmOWFhLWJiZjctNDA2MS04YTdhLTI0OGM3M2MyNTRhOCJ9",
        width=1400,
        height=870,
        scrolling=True
    )

def analytics_page(analytics_option="Temporal Analysis"):
    if analytics_option == "Temporal Analysis":
        analytics_page_1()
    elif analytics_option == "Road Type Analysis":
        analytics_page_2()
    elif analytics_option == "Landmark Analysis":
        analytics_page_3()
    elif analytics_option == "Road Signage Analysis":
        analytics_page_4()
    elif analytics_option == "Pedestrian Analysis":
        analytics_page_5()
    else:
        st.warning(f"Unknown analytics option: {analytics_option}")