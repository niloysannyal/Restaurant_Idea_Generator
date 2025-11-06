import streamlit as st
import langchain_helper

st.title('Restaurant Idea Generator')

cuisine = st.sidebar.selectbox("Select a Cuisine", ("Bangladeshi", "Indian", "Pakistani", "American", "Chinese", "French", "Mexican"))


if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)

    st.header(response['restaurant_name'])
    st.write("**Menu Items:**")
    menu_items = response['menu_items'].split(',')
    for item in menu_items:
        st.write("-",item)

