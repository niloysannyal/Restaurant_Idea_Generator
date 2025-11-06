import streamlit as st
import langchain_helper

# Page config
st.set_page_config(
    page_title="🍽️ Restaurant Idea Generator",
    page_icon="🍴",
    layout="wide"
)

# Header
st.markdown("<h1 style='text-align: center; color: #009999;'>🍴 Restaurant Idea Generator</h1>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar for user input
st.sidebar.markdown("## 🍽️ Customize Your Restaurant")
st.sidebar.markdown("---")

cuisine = st.sidebar.selectbox(
    "🌎 Select a Cuisine",
    (
        "Bangladeshi",
        "Indian",
        "Pakistani",
        "American",
        "Chinese",
        "French",
        "Mexican"
    )
)

st.sidebar.info("Select a cuisine to generate a restaurant name and menu items. 🍴")


# Generate button
generate = st.sidebar.button("Generate Ideas")

if generate and cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)

    restaurant_name = response.get('restaurant_name', 'Unnamed Restaurant')
    menu_items = response.get('menu_items', '').split(',')

    # Display restaurant name in a big bold card
    st.markdown(
        f"""
        <div style="
            background-color: #006666;
            padding: 18px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 3px 3px 10px rgba(0,0,0,0.2);
        ">
            <h2 style='color: #FFFFFF;'>{restaurant_name}</h2>
            <p style='color: #FFFFFF; font-size:20px;'>Cuisine: {cuisine}</p>
        </div>
        """, unsafe_allow_html=True
    )

    st.markdown("### 📜 Menu Items")

    # Display menu items in two columns
    col1, col2 = st.columns(2)
    for idx, item in enumerate(menu_items):
        if idx % 2 == 0:
            col1.markdown(f"✅ {item.strip()}")
        else:
            col2.markdown(f"✅ {item.strip()}")

    st.markdown("---")
    st.success("Your restaurant idea is ready! 🍽️")

# Footer
st.markdown(
    "<p style='text-align:center; color: #9CA3AF; font-size:18px;'>Built with ❤️ by Niloy Sannyal</p>",
    unsafe_allow_html=True
)
