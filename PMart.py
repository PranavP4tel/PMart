#Main Page
import streamlit as st

#Setting page configurations
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

#Page content
st.image("images/PMart logo.png")
st.header("Welcome to PMart!👋")

#Defining the sidebar
st.sidebar.success("Select a form from above")

#Main page content
st.markdown(
    """
    ### Created by Pranav Patel
    
    This is an app to allow form data to be stored in MongoDB.
    Two forms used here:
    1. Inventory: To store inventory details of a product

    2. Order: To place an order for a product present in the inventory

    #### Have Fun👋
    """
)