# Project Title: Inventory-app

## Project Description

This app was developed to challenge my backend skills in Flask. The application can do the following:

- Create Inventory Items
- View all inventory items stored in the database
- Update Inventory Items
- Delete inventory items.

The app also has an extra feature of being able to create warehouses, and then assign inventory to those warehouses.

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

In addition, it was interesting to explore how inventory applications work. In my case I had decided to implement a one-to-one relationship between warehouses and items. Yet, I used a SKU column on the frontend to help communicate to the client that if they wanted to distribute items, they'll have to use a SKU to do so.


## How to run/install the application

The instructions to install/run the application will change depending on whether you are running the application locally or on Replit. To help ease any confusion, I have created two branches which can be accessed on Replit. The branch geared for running the app on Replit is `master` while the branch geared for running the app locally will be on `main`.

# Running the app on Replit

- It should not be necessary to reinstall all the packages/dependancies. This is not recommended since it can take a while for Replit to install them all. In addition, Replit tends to remove some dependencies to save on storage. By clicking on `Run` Replit will isntall `flask_wtf` and `flask_sqlalchemy`. In the event the app fails after clicking "Run," with an error related to it's dependencies, you can install ALL dependencies by running `pip install -r requirements.txt` in the console.

  - If by chance you try to run the app a second time after clicking on "Stop", you may have to terminate the port to re-run the app. You can do this by running `kill 1` in the console.

- You should see the server running in the console as well as the app running in Replit's internal browser tool. It is highly recommended to NOT interact with the app in the browser tool. You can run the app in your browser by clicking on "Open in new tab" button near the top right of the window. It will be right under the "Invite" and search button. Once you are viewing the app in your browser and not in Replit's browser, the app is ready to be tested.

![image](https://user-images.githubusercontent.com/76107997/169199250-cd473fc2-dead-47ed-938c-3586aae4e722.png)

# Running the app Locally

- The code on Replit can also be located on GitHub. The main difference the codebase in GitHub and the codebase in Replit, is that the codebase in GitHub has tests that can be ran locally. In addition, the `app.run()` function which is needed to run Replit codebase in the browser is commented-out in the GitHub repo.
- Once you download the code, you should first create an virtual enviornment. You can do this by running `python3 -m venv venv` in your terminal. You'll then need to activate it by running `source venv/bin/activate`
- Once you have initalized your virtual enviornment, you can install all dependancies in the `requirements.txt` file. You can do this by running `pip install -r requirements.txt`
- After all dependancies are installed, you can spin up the app by running `export FLASK_ENV=development; flask run`
- The app will then open in your browser on localhost: 5000.
- Running the app locally will also allow you to run/execute the tests that were written for the app. You can run `python3 -m unittest -v` in your terminal to see summary of the tests.

## Quick Demo Guide

# Create an inventory item

- You can create an inventory item by clicking on the `Create inventory item` button. Since the database has a one-to-one relationship between items and warehouses, a user will have to create a "new" item, but with the same SKU, if they were goign to create inventory in other warehouses. You can see this by first creating an item whose name is "Shirt", with a price of 12.45, whatever quantity you want, an SKU of 123456, and a warehouse location from the drop down. Here is a picture that best describes this. Take note that the SKUs are the same, but the IDs are different.
  ![Create-Item-demo](https://user-images.githubusercontent.com/76107997/169196892-07f00500-fa7b-492b-a4c1-b2b2a2b59f60.png)

# Create a new Warehouse

- You can create a warehouse by clicking on the `Create Warehouse` button. Here you can put in the name of the warehouse you want to create.

# Edit an Item

- Each `Edit` button has a hyperlink containing the items id. This link will take you to a form populated with the information of the item. You can edit any of these fields before submitting and it will appear on the homepage after you submit the requested changeds. All these fields are required to be filled before submission.

# Delete an Item

- While on the `Edit Item` page, you can also delete an item. Once you do so, the page will redirect you to the home page with a status banner.

# View all items

- You can inherently see all items on the homepage. This is particularly evident after adding several items.
