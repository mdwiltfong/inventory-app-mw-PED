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
- Jninja
- Bootstrap
- SQLAlchemy

In addition, the app has a full suite of unit tests, integration tests, as well as comments to document the app's functionality. This means the app will support future developers who wish to add to the application.

## What I learned

This project was a great opportunity to learn more about Replit, and the various technologies it uses. For example, SQLITE. Although it behaves similar to PSQL since
it is a relational database, it was nonetheless interesting to see how much carries over from PSQL.

In addition, it was interesting to explore how inventory applications work. I have worked with various inventory systems in the past, as a user, and it's fascinating the amount of relationships are maintained in large scale inventory system.

## How to run/install the application

The instructions to install/run the application will change depending on whether you are running the application locally or on Replit. To help ease any confusion, I have created two branches which can be accessed on Replit. The branch geared for running the app on Replit is `master` while the branch geared for running the app locally will be on `main`.

# Running the app on Replit

- It should not be necessary to reinstall all the packages/dependancies. This is unrecommended since it can take a while for Replit to install them all. In addition, Replit tends to remove some dependencies to save on storage. You'll have to install only two packages by running `pip install flask_wtf` and then `pip install flask_sqlalchemy`. In the event the app fails after clicking "Run," with an error related to it's dependencies you can install ALL dependencies by running `pip install -r requirements.txt` in the console.

- You should see the server running in the console as well as the app running in Replit's internal browser tool. It is highly recommended to NOT interact with the app in the browser tool. You can run the app in your browser by clicking on "Open in new tab" button near the top right of the window. It will be right under the "Invite" and search button. Once you are viewing the app in your browser and not in Replit's browser, the app is ready to be tested.

# Running the app Locally

- The code on Replit can be located on GitHub. The small difference between the GitHub repo and Replit is that the `app.run()` command is commented-out in the GitHub repo. This is because this command is solely used to run the application on Replit.
- Once you download the code, you should first create an virtual enviornment. You can do this by running `python3 -m venv venv` in your terminal. You'll then need to activate it by running `source/bin/activate`
- Once you have initalized your virtual enviornment, you can install all dependancies in the `requirements.txt` file. You can do this by running `pip install -r requirements.txt`
- After all dependancies are installed, you can spin up the app by running `export FLASK_ENV=development; flask run`
- The app will then open in your browser on localhost: 5000.
- Running the app locally will also allow you to run/execute the tests that were written for the app. You can run `python3 -m unittest -v` in your terminal to see summary of the tests.

## Quick Demo Guide

# Create an inventory item

- You can create an inventory item by clicking on the `Create inventory item` button.
