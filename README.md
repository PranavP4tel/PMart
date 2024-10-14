# PMart
Created a web app using Streamlit with 2 forms:
1. Inventory 
2. Order

These forms are connected to MongoDB via pymongo library. 
Currently only 3 functions are supported
1. Inserting data into the collections
2. Reading all documents from the collection
3. Counting records present in the collection


### Inventory Form
Allows a user to enter product details into inventory such as product name, price, quantity and more.
Allows user to list all the records and print the total number of records in the database as well.
![Inventory Form](https://github.com/PranavP4tel/PMart/blob/main/images/Inventory_Form.png)


### Order Form
Allows a user to place an order for a product, with details such as product name, quantity, address and more.
Also allows to list all the records and print total number of records in the database as well.

Inserting a document is detailed is completed as follows:
1. Checking if the product name matches any in the inventory document. Returns a warning if not present.
2. Check if product quantity of matched product is not 0. Else, "Out of Stock" message is returned
3. Check if user has requested product quantity of matched product, more than the quantity present in stock. If true, "Requested quantity not available" message is returned.
4. If all checks are passed, then price of matched product name in inventory document is obtained, and total amount as per the quantity is displayed. Finally, the document is inserted in the database with a timestamp.

![Order Form](https://github.com/PranavP4tel/PMart/blob/main/images/Order_Form.png)

