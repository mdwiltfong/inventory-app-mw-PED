# Project Title: Inventory-app

## Project Description

This app was developed to challenge my backend skills in Flask. The application can do the following:

- Create Inventory Items
- View all inventory items stored in the database
- Update Inventory Items
- Delete inventory items.
- Create Warehouse locations
- Assign inventory to those warehouse locations

## Features

This app used the following technologies:

- Sqlite3 as a database
- Flask WTForms
- Flask
- Jninja
- Bootstrap
- SQLAlchemy

In addition, the app has a full suite of unit tests, integration tests, as well as comments to document the app's functionality. This means the app will support future developers who wish to add to the application.

## What I learned

This project was a great opportunity to learn more about Replit, and the various technologies it uses. For example, SQLITE. Although it behaves similar to PSQL since
it is a relational database, it was nonetheless interesting to see how much carries over from PSQL.

In addition, it was interesting to explore how inventory applications work. In my case I had decided to implement a many-to-many relationship between warehouses and items. This makes the app easy to scale as the inventory increases. In addition, this level of complexity will help future developers who wish to add more information/capabilities to the app.

## How to run/install the application

- By clicking on `Run` the app should install `flask_wtf` and `flask_sqlalchemy` before initalizing the server. Once the server is running, Replit's internal browser will show the app. It is highly recommended to NOT interact with the app in this browser, but instead in a new tab. You can run the app in your browser by clicking on "Open in new tab" button near the top right of the window. It will be right under the "Invite" and search button. Once you are viewing the app in your browser and not in Replit's browser, the app is ready to be tested.
  - In the event the app fails after clicking "Run," with an error related to it's dependencies, you can install ALL dependencies by running pip install -r requirements.txt in the console.
  - If by chance you try to run the app a second time after clicking on "Stop", you may have to terminate the port to re-run the app. You can do this by running `kill 1` in the console.
- If you want to run the app locally on your machine, you will have to first create a virtual enviornment after forking the repo and downloading it. You can create and initalize a virtual enviornment by running `python3 -m venv venv` in your terminal, and then `source venv/bin/activate`.
- The actual code is nested in a file. So you'll first want to change your directory by running `cd inventory-app-1`.
- Finally by running `python3 app.py` the app should appear on port 8080. Keep in mind that if there is a processes already occuring on this port you will have to terminate it. I usually do this by running `npx kill-port 8080`

# Demo Guide

1. View List of items
   - On the home page, you can immediately see a list of all the items in the database.
2. Create a warehouse
   - By clicking on `create a warehouse location` you can input the name of a new warehouse. Keep in mind, that the name of a warehouse is the primary key in the `warhouses` table. Meaning if you input the name of a warehouse that already exists, the page will return an error.
3. Create an inventory item
   - After creating a warehouse, you can create a new inventory item. Keep in mind you could have created an inventory item first before creating a warehouse. The actions are not connected. An item's SKU is a unique identifier, which is why it's the primary key in the `items` table. If you enter a SKU that already exists, the app will display an error message.
4. Edit an item
   - After an item is created, you can edit it's details by clicking on the `Edit` button. Although you can edit the SKU of an item, you still can't duplicate SKUs. So if you enter an already existing SKU the page will display an error message. If by chance you don't want to process an edit, you can click on `Cancel` to take you back to the main page.
5. Assign/View inventory
   - Now that you've created an item and a new warehouse, you can assign inventory. On the main page, click on `inventory` by the item you created. A new page will load. At the moment there are no assignments so that page will be empty. A new option will be available too. Click on `Assign Inventory`. A SKU can only exist in one warehouse. Although you've created a new item and it has no warehouse location, the page will display an error if you try to assign inventory to a warehouse twice. After you assign a warehouse from the drop down, you can assign how much of the total inventory you want to allocated. The app currently does not check the assigned inventory to the total quantity you made when creating the item. Therefore, the math will be up to the user to do.
   - Also, if you were to change an item's SKU, you will notice that it's inventory will carry over to the new assignment.
6. Edit Inventory
   - Now that you've assigned some of the total quantity to a warehouse, you can see an assignment in the `view_inventory` page. You can edit this assignment by clicking on `Edit` This page will also prevent you from assigning an item's inventory to a warehouse where it's already located.
7. Delete an Item
   - Deleting an item will also delete it's inventory history. You can do this by going back to the main page, and then select `Edit`. There will be a `Delete` option. Once you click on this option the item will be deleted and you will be directed back to the home page.
