INSERT INTO customers (first_name, last_name, email) VALUES
('Marcus', 'Reed', 'marcus.reed@example.com'),
('Tiana', 'Brooks', 'tiana.brooks@example.com'),
('Jordan', 'Cole', 'jordan.cole@example.com');

INSERT INTO products (product_name, sku, price, stock_quantity) VALUES
('Wireless Mouse', 'WM-100', 24.99, 50),
('Mechanical Keyboard', 'MK-200', 79.99, 25),
('USB-C Hub', 'UH-300', 39.99, 40),
('Monitor Stand', 'MS-400', 54.99, 15);

INSERT INTO orders (customer_id, status) VALUES
(1, 'delivered'),
(2, 'processing'),
(1, 'pending');

INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
(1, 1, 2, 24.99),
(1, 3, 1, 39.99),
(2, 2, 1, 79.99),
(3, 4, 1, 54.99);

INSERT INTO payments (order_id, amount, payment_method, payment_status, paid_at) VALUES
(1, 89.97, 'credit_card', 'completed', CURRENT_TIMESTAMP),
(2, 79.99, 'paypal', 'completed', CURRENT_TIMESTAMP),
(3, 54.99, 'debit_card', 'pending', NULL);
