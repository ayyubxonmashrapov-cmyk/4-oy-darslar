SHOW DATABASEs;

CREATE DATABASE restaurant_db;

USE restaurant_db;

CREATE TABLE orders(
    id int AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) not NULL,
    dish_name VARCHAR(100) not null,
    category VARCHAR(50) not NULL,
    quantity int NOT NULL,
    price_per_item DECIMAL(10,2) NOT NULL,
    order_date DATE not NULL,
    status VARCHAR(20) NOT NULL,
    table_namber int NOT NULL
);


insert into orders (customer_name, dish_name, category, quantity, price_per_item ,order_date, status, table_namber) VALUES 
('Ali Valiyev', 'Burger', 'Fastfood', 2, 35000.00, '2026-05-01', 'Tayyor', 5),
('Nodira Karimova', 'Plov', 'Milliy', 1, 60000.00, '2026-05-01', 'Yetkazildi', 2);

SELECT * FROM orders ORDER BY order_date desc;

SELECT * from orders ORDER BY quantity * price_per_item DESC LIMIT 3;

SELECT * from orders WHERE category = "Milliy";

SELECT category, AVG(price_per_item) FROM orders GROUP BY category;

SELECT * from orders where status = "tayyorlanmoqda";

SELECT status, count(*) from orders GROUP BY status 
    
SELECT * from orders where table_namber > 5

