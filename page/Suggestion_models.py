import streamlit as st

def suggestion_model1():
    st.title("Suggestion Model 1")
    st.write("This model is based on the following assumptions:")

def suggestion_model2():
    st.title("Suggestion Model 2")
    st.write("sdf")

def suggestion_page(suggestion_option="1"):
    if suggestion_option == "Temporal Analysis":
        suggestion_model1()
    elif suggestion_option == "Road Type Analysis":
        suggestion_model2()
    else:
        st.warning(f"Unknown suggestion option: {suggestion_option}")