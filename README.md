# Batch 63 - Inventory Management System

This is a console-based **Inventory Management System** developed as a final project for Batch 63 at PIAIC. The system implements role-based access control, allowing **Admins** to manage inventory and **Users** to view and purchase products. Designed for beginners, it provides a simple yet effective way to learn basic programming and inventory management concepts.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [System Functions](#system-functions)
    - [Admin Functions](#admin-functions)
    - [User Functions](#user-functions)
  - [Usage Flow](#usage-flow)
- [Code Overview](#code-overview)

---

## Features

### Admin
- **Add Products**: Create new products with essential details.
- **View Inventory**: See a list of all available products.
- **Delete Products**: Remove products from the inventory.
- **Adjust Stock**: Modify stock levels for existing products.
- **Check Stock Levels**: Identify products that need restocking.
- **Search Products**: Find specific products easily.

### User
- **View Inventory**: Explore available products.
- **Buy Products**: Purchase items by entering the product ID and quantity.
- **Check Stock Levels**: View alerts for low-stock products.
- **Search Products**: Look up products by name.

---

## Getting Started

### Prerequisites
- Python 3.x should be installed on your machine.

### Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/Inventory-Management-System.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Inventory-Management-System/inventory_management_system
   ```
3. Run the application:
   ```bash
   python main.py
   ```

---

## Usage

### System Functions

#### Admin Functions
- **Add Product**: Enter product details to add a new item.
- **View Products**: Displays all products with their information.
- **Delete Product**: Remove a product using its ID.
- **Adjust Stock**: Update the stock quantity for products.
- **Check Stock Levels**: Displays products that are low on stock.
- **Search Product**: Search products using keywords from their names.

#### User Functions
- **View Products**: Browse through all products.
- **Buy Product**: Input product ID and quantity to purchase items.
- **Check Stock Levels**: Alerts for items that are low on stock.
- **Search Product**: Find products by name.

### Usage Flow
1. **Main Menu**:
   - **Register** as an Admin or User.
   - **Login** with your credentials.
   - **Exit** to close the application.

2. **Admin Menu**:
   - Manage inventory by adding, deleting, and adjusting products.

3. **User Menu**:
   - Explore products, make purchases, and search inventory.

4. **Logout**:
   - Return to the main menu to log in or exit.

---

## Code Overview

### Key Classes
- **User Class**: Manages user roles and authentication.
- **Product Class**: Handles product details and inventory management.

### Main Functions
- **login()**: Authenticates users.
- **register_user()**: Creates new user accounts.
- **add_product()**: Adds new products for Admins.
- **adjust_stock()**: Adjusts product stock levels.
- **delete_product()**: Deletes a product by ID.
- **view_products()**: Displays all products in the inventory.
- **buy_product()**: Processes product purchases.
- **search_product()**: Searches for products by name.
- **check_stock()**: Displays low-stock products.
