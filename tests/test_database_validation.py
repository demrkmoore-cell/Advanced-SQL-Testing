def test_customer_count(db_connection):
    result = db_connection.execute(
        "SELECT COUNT(*) FROM customers"
    ).fetchone()

    assert result[0] == 3


def test_product_count(db_connection):
    result = db_connection.execute(
        "SELECT COUNT(*) FROM products"
    ).fetchone()

    assert result[0] == 4


def test_order_count(db_connection):
    result = db_connection.execute(
        "SELECT COUNT(*) FROM orders"
    ).fetchone()

    assert result[0] == 3


def test_order_payment_reconciliation(db_connection):
    result = db_connection.execute(
        """
        SELECT COUNT(*)
        FROM (
            SELECT
                o.order_id,
                SUM(oi.quantity * oi.unit_price) AS order_total,
                p.amount AS payment_amount
            FROM orders o
            JOIN order_items oi ON o.order_id = oi.order_id
            JOIN payments p ON o.order_id = p.order_id
            GROUP BY o.order_id, p.amount
            HAVING SUM(oi.quantity * oi.unit_price) <> p.amount
        ) AS mismatches
        """
    ).fetchone()

    assert result[0] == 0


def test_referential_integrity(db_connection):
    result = db_connection.execute(
        """
        SELECT COUNT(*)
        FROM orders o
        LEFT JOIN customers c ON o.customer_id = c.customer_id
        WHERE c.customer_id IS NULL
        """
    ).fetchone()

    assert result[0] == 0


def test_product_inventory_nonnegative(db_connection):
    result = db_connection.execute(
        """
        SELECT COUNT(*)
        FROM products
        WHERE stock_quantity < 0
        """
    ).fetchone()

    assert result[0] == 0


from decimal import Decimal


def test_first_order_total(db_connection):
    result = db_connection.execute(
        """
        SELECT SUM(quantity * unit_price)
        FROM order_items
        WHERE order_id = 1
        """
    ).fetchone()

    assert result[0] == Decimal("89.97")
