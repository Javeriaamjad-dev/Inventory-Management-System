# Inventory Management System

This is a console-based Inventory Management System developed in Python. The system manages user authentication, product inventory, and includes essential features like product addition, viewing, deletion, stock adjustments, and low stock alerts. It serves as the final project for Batch 63 of PIAIC.

## Features

- **User Authentication**: Admin and User roles with specific permissions.
- **Product Management**: Add, view, delete, and adjust product stock.
- **Stock Alerts**: Low stock alert for products with quantities below 10.

## Prerequisites

- Python 3.x

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Javeriaamjad-dev/Inventory-Management-System.git
   cd Inventory-Management-System/inventory_management_system
   ```

2. **Run the Script**:
   ```bash
   python main.py
   ```

## Usage Guide

1. **Login**:
   - Available users:
     - Admin: `username = "jia"`, `password = "jia498627"`
     - User: `username = "javeriaamjad"`, `password = "javeriaamjad"`

2. **Main Menu Options**:
   - `1. Add Product (Admin Only)`
   - `2. View Products`
   - `3. Delete Product (Admin Only)`
   - `4. Adjust Stock (Admin Only)`
   - `5. Check Stock Levels`
   - `6. Exit`

## Code Overview

- **Classes**:
  - `User`: Manages user authentication.
  - `Product`: Stores product details.

- **Functions**:
  - `login()`: User authentication.
  - `add_product()`: Adds products to inventory (admin only).
  - `view_products()`: Lists products.
  - `delete_product()`: Removes products (admin only).
  - `adjust_stock()`: Changes stock levels (admin only).
  - `check_stock()`: Low stock alert.
  - `safe_input()`: Error-handling for input.

## Example

```bash
Welcome to the Inventory Management System!
Enter username: jia
Enter password: jia498627
Welcome jia!

Options:
1. Add Product (Admin Only)
2. View Products
3. Delete Product (Admin Only)
4. Adjust Stock (Admin Only)
5. Check Stock Levels
6. Exit
Choose an option: 2
No products available.
```

---

**Batch 63 - Final Project**
```
