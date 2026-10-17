# ⌚ Watch Store Web Application

A web-based Watch Store application built using Flask and MySQL. Users can browse watches, search for products, add watches to their cart, and manage their shopping cart.

## Features

- User Login
- Browse Watch Products
- Search Watches
- Add Products to Cart
- View Shopping Cart
- Remove Items from Cart
- MySQL Database Integration

## Technologies Used

- **Frontend:** HTML, CSS
- **Backend:** Python, Flask
- **Database:** MySQL
- **Tools:** VS Code, Git, GitHub

## Project Structure

```text
Watch/
├── app.py
├── database.sql
├── templates/
│   ├── login.html
│   ├── home.html
│   ├── search.html
│   └── cart.html
└── static/
    ├── CSS/
    │   └── style.css
    └── images/
```

## How to Run the Project

1. Install Python and MySQL.
2. Install the required Python packages:

   ```bash
   pip install flask mysql-connector-python
   ```

3. Open MySQL and execute the SQL commands in `database.sql`.
4. Configure your MySQL connection credentials securely using environment variables.
5. Run the application:

   ```bash
   python app.py
   ```

6. Open the local URL displayed in your terminal in a web browser.

## Security Note

Do not upload database passwords, secret keys, or other credentials to a public repository. Use environment variables to store sensitive information.

## Author

**Nisitha K.**

GitHub: https://github.com/KNisitha
