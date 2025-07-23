CREATE TABLE IF NOT EXISTS bills (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    customer_name TEXT,
    item TEXT,
    quantity INTEGER,
    price REAL
)