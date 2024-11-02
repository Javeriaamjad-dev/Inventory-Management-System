# Inventory Management System

A console-based Inventory Management System in Python, designed for user authentication and managing product inventory operations. This project includes features for adding, viewing, deleting, adjusting stock levels, and low-stock alerts. Developed as a final project for Batch 63 of PIAIC Islamabad.

## Features

- **User Authentication**: Admin and User roles with role-based access control.
- **Product Management**: Admins can add, view, delete, and adjust product stock.
- **Stock Alerts**: Alerts for products with stock levels below 10.

## Prerequisites

- Python 3.x

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Javeriaamjad-dev/Inventory-Management-System
   cd Inventory-Management-System
   ```

2. **Run the Script**:
   ```bash
   python inventory_management_system.py
   ```

## Usage Guide

1. **Login**: 
   - Enter a username and password.
   - Sample users:
     - Admin: `username = "jia"`, `password = "jia498627"`
     - User: `username = "javeriaamjad"`, `password = "javeriaamjad"`

2. **Main Menu Options**:
   - `1. Add Product (Admin Only)`: Add new products to inventory.
   - `2. View Products`: List all products with details.
   - `3. Delete Product (Admin Only)`: Remove products from inventory.
   - `4. Adjust Stock (Admin Only)`: Update stock quantities.
   - `5. Check Stock Levels`: Displays low-stock products.
   - `6. Exit`: Exit the application.

## Code Overview

- **Classes**:
  - `User`: Handles user information and authentication.
  - `Product`: Manages product details like ID, name, category, price, and stock.

- **Functions**:
  - `login()`: Authenticates users.
  - `add_product()`: Adds a product to inventory (admin only).
  - `view_products()`: Displays products.
  - `delete_product()`: Deletes a product (admin only).
  - `adjust_stock()`: Adjusts stock (admin only).
  - `check_stock()`: Checks for low stock.
  - `safe_input()`: Safely inputs and casts values.

---

**Batch 63 - Final Project**
```
