import psycopg
import pytest


def test_reject_negative_product_price(db_connection):
    with pytest.raises(psycopg.errors.CheckViolation):
        with db_connection.transaction():
            db_connection.execute(
                """
                INSERT INTO products
                    (product_name, sku, price, stock_quantity)
                VALUES
                    ('Invalid Price Product', 'TEST-NEG-PRICE', -10.00, 5)
                """
            )


def test_reject_negative_product_stock(db_connection):
    with pytest.raises(psycopg.errors.CheckViolation):
        with db_connection.transaction():
            db_connection.execute(
                """
                INSERT INTO products
                    (product_name, sku, price, stock_quantity)
                VALUES
                    ('Invalid Stock Product', 'TEST-NEG-STOCK', 10.00, -5)
                """
            )


def test_reject_invalid_customer_email(db_connection):
    with pytest.raises(psycopg.errors.CheckViolation):
        with db_connection.transaction():
            db_connection.execute(
                """
                INSERT INTO customers
                    (first_name, last_name, email)
                VALUES
                    ('Test', 'Invalid', 'not-an-email')
                """
            )


def test_reject_order_with_nonexistent_customer(db_connection):
    with pytest.raises(psycopg.errors.ForeignKeyViolation):
        with db_connection.transaction():
            db_connection.execute(
                """
                INSERT INTO orders (customer_id, status)
                VALUES (9999, 'pending')
                """
            )


def test_reject_duplicate_customer_email(db_connection):
    with pytest.raises(psycopg.errors.UniqueViolation):
        with db_connection.transaction():
            db_connection.execute(
                """
                INSERT INTO customers (first_name, last_name, email)
                VALUES ('Duplicate', 'Customer', 'marcus.reed@example.com')
                """
            )


def test_reject_null_customer_email(db_connection):
    with pytest.raises(psycopg.errors.NotNullViolation):
        with db_connection.transaction():
            db_connection.execute(
                """
                INSERT INTO customers (first_name, last_name, email)
                VALUES ('Missing', 'Email', NULL)
                """
            )


def test_reject_zero_order_item_quantity(db_connection):
    with pytest.raises(psycopg.errors.CheckViolation):
        with db_connection.transaction():
            db_connection.execute(
                """
                INSERT INTO order_items
                    (order_id, product_id, quantity, unit_price)
                VALUES
                    (1, 2, 0, 79.99)
                """
            )


def test_reject_order_item_with_nonexistent_product(db_connection):
    with pytest.raises(psycopg.errors.ForeignKeyViolation):
        with db_connection.transaction():
            db_connection.execute(
                """
                INSERT INTO order_items
                    (order_id, product_id, quantity, unit_price)
                VALUES
                    (1, 9999, 1, 10.00)
                """
            )


def test_reject_duplicate_product_in_order(db_connection):
    with pytest.raises(psycopg.errors.UniqueViolation):
        with db_connection.transaction():
            db_connection.execute(
                """
                INSERT INTO order_items
                    (order_id, product_id, quantity, unit_price)
                VALUES
                    (1, 1, 1, 24.99)
                """
            )


def test_reject_negative_payment_amount(db_connection):
    with pytest.raises(psycopg.errors.CheckViolation):
        with db_connection.transaction():
            db_connection.execute(
                """
                INSERT INTO payments
                    (order_id, amount, payment_method, payment_status)
                VALUES
                    (1, -25.00, 'credit_card', 'completed')
                """
            )


def test_reject_invalid_payment_method(db_connection):
    with pytest.raises(psycopg.errors.CheckViolation):
        with db_connection.transaction():
            db_connection.execute(
                """
                INSERT INTO payments
                    (order_id, amount, payment_method, payment_status)
                VALUES
                    (1, 25.00, 'cash', 'completed')
                """
            )


def test_reject_invalid_payment_status(db_connection):
    with pytest.raises(psycopg.errors.CheckViolation):
        with db_connection.transaction():
            db_connection.execute(
                """
                INSERT INTO payments
                    (order_id, amount, payment_method, payment_status)
                VALUES
                    (1, 25.00, 'credit_card', 'unknown')
                """
            )


def test_reject_duplicate_payment_for_order(db_connection):
    with pytest.raises(psycopg.errors.UniqueViolation):
        with db_connection.transaction():
            db_connection.execute(
                """
                INSERT INTO payments
                    (order_id, amount, payment_method, payment_status)
                VALUES
                    (1, 89.97, 'credit_card', 'completed')
                """
            )
