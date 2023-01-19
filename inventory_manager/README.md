## Inventory Manager
---
## Contents

| Section | Description |
|--------------|-------------|
| Requirements | A list of any software necessary to run this solution. |
| Functions | Brief elucidation of this program's properties. |
| Usage | A detailed explanation of the program's features and how to use them. |

---
## Requirements

- Python 3.11 - [read more](https://www.python.org/downloads/release/python-3110/)
---

* **What is the goal of this project?**  This project was done using Python Programming and focused on applying Object-Oriented Programming principles. It provides a comprehensive and organized view and management tool for a shoe warehouse.

#### Functions:
* See all products: displays a list of all products currently available in a user-friendly format.
* Enter a new product: the user can add a new product to the inventory containing all pertinent details.
* Restock a product: the user can update the quantity in stock for a particular item.
* Search product/ see product value/ see item on sale: the user can see the referred information for a specific item.

#### Installation and Usage
This program requires Python 3.11, as previously described, and was developed applying all concepts inherent to Object-Oriented Programming principles. The whole file 'inventory_manager' must be downloaded, including 'inventory.txt', which holds all information about the products in stock.
Once the contents are downloaded, the script can be executed on the terminal by typing `python3 inventory_manager.py` as shown below. The user will be prompted with a menu, as shown below.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/inventory_manager_terminal.png" width=50% height=50%>
</p>
Obs.: you should navigate to the folder where financial_calculator.py is located in using the 'cd' command.


If the user chooses the option to see all items currently on stock, a list of all products will be displayed in a user-friendly format.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/inventory_manager_see_all.png" width=25% height=25%>
</p>

The user can also add register a new product to the program. After providing all the required deitals (e.g. product name, id, price and quantity), the product will automatically be added to 'inventory.txt' for future reference.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/inventory_manager_add_new.png" width=50% height=50%>
</p>

If the user decides to restock an item, the program will automatically find the product with the lowest quantity on stock, and ask the user if they would like to restock the referred item. After providing how many items they would like to restock, a feedback is shown to the user, as it is possible to see below.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/inventory_manager_restock.png" width=75% height=75%>
</p>

The user can also search an item using the item's id. Then, the program will automatically fetch all the details for the referred product and display them in a user-friendly manner.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/inventory_manager_search.png" width=50% height=50%>
</p>

It is possible to check the total item for every item currently in stock. The total value is calculated based on item's price and quantity. The final result is displayed to the user as a table.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/inventory_manager_total.png" width=50% height=50%>
</p>

Finally, the user can also fetch witch item is currently on sale. The program will automatically find the item with the highest availability on stock, and return this product's details to the user.

<p align="center">
<img src="https://github.com/juliaalencarb/finalCapstone/blob/master/images/inventory_manager_sale.png" width=50% height=50%>
</p>
