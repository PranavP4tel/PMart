#Importing libraries
import streamlit as st
from pymongo import MongoClient
import pandas as pd

#Creating a connection and retrieving object for Inventory collection
client = MongoClient(host = "localhost", port = 27017)
db = client['PMart']
collection = db['Inventory']

# Title of the app
st.title("Inventory Details Form")

# Form for inventory details
product_id = st.number_input("Product ID", min_value = 1, step = 1)
product_name = st.text_input("Product Name")
quantity = st.number_input("Quantity", min_value=0, step = 1)
price = st.number_input("Price ($)", min_value=0.0, format="%.2f")
location = st.text_input("Storage Location")

# Submit button logic
if st.button("Add To Inventory"):
    # Create a dictionary with the entered data
    inventory_item = {
        "product_id": product_id,
        "product_name": product_name,
        "quantity": quantity,
        "price": price,
        "location": location
    }

    #Insert product information within collection and return success
    collection.insert_one(inventory_item)

    st.success("Item added to inventory!")
    st.write(inventory_item)

#List inventory items
df = pd.DataFrame()
if st.button("List Inventory Records"):
    res = collection.find()
    records = list(res)
    if list(records):
        for i in records:
            df = pd.concat([df, pd.DataFrame([i])], ignore_index=True)

        st.markdown("""### Displaying Records""")
        st.dataframe(df)
    else:
        st.write("No records!")
    


#Check Total Records
if st.button("List inventory count"):
    count = collection.count_documents({})
    st.metric("Total inventory items: ", count)


#List inventory items 
#Logic to print each record individually
#if st.button("List Inventory Records"):
    #res = collection.find()
    #records = list(res)
    #if list(records):
        #st.markdown("""### Displaying Records""")
        #for i in records:
            #record = ""
            #for key, value in i.items():
                #if key == "_id":
                    #continue
                #else:
                    #record += f" {key} : {value}   " 
            #st.write(record)
            #st.write("")

    #else:
        #st.write("No records!")