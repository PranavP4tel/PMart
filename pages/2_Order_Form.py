#Importing libraries
import pandas as pd
import streamlit as st
from pymongo import MongoClient
from datetime import datetime

#Creating connection and retrieving objects for Inventory and Order collections
client = MongoClient(host = "localhost", port = 27017)
db = client['PMart']
orders = db['Orders']
inventory = db['Inventory']

# Title of the app
st.title("Order Form")

# Form for order details
cust_name = st.text_input("Customer Name")
product_name = st.text_input("Product Name")
quantity = st.number_input("Quantity", min_value=0, step = 1)
del_location = st.text_area("Street Address")
pincode = st.number_input("Pincode", min_value = 1, step = 1)

# Submit button logic
if st.button("Place Order"):
    #Check if entered product name is existing in the inventory
    records = inventory.find_one({"product_name":product_name},{'price':1,'quantity':1})

    #If product name doesn't exists, then user is alerted to enter a correct name
    if records is None:
        st.error("Enter correct product name!")
    else:
        #Check if product is in stock
        if records.get("quantity")>=1:
            #Check if quantity requested by user is more than that available in the inventory
            if quantity >= records.get("quantity"):
                st.error("Oops! We do not have requested quantity in stock")
            
            #Calculating order amount by obtaining price of product.
            #Inserting the order details in the collection
            else: 
                total_amount = quantity * records.get("price")
                order_data = {
                    "Order_Timestamp": datetime.now(),
                    "cust_name": cust_name,
                    "product_name": product_name,
                    "quantity":quantity,
                    "total_amount":total_amount,
                    "delivery_location":del_location,
                    "pincode":pincode
                }

                #Insert order information in collection and return total amount of order
                orders.insert_one(order_data)
                st.success("Order Placed!")
                st.write("Total Amount: ",total_amount)
        else:
            st.error("Product is out of stock!")

#List inventory items
df = pd.DataFrame()
if st.button("List Order Records"):
    res = orders.find()
    records = list(res)
    if list(records):
        for i in records:
            df = pd.concat([df, pd.DataFrame([i])], ignore_index=True)
        st.markdown("""### Displaying Records""")
        st.dataframe(df)
    else:
        st.write("No records!")

#Check Total Records
if st.button("List Order count"):
    count = orders.count_documents({})
    st.metric("Total Order placed: ", count)

#List all records
#Old Logic to print each record individually
#if st.button("List Order Records"):
    #res = orders.find()
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