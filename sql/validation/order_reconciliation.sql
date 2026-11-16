CREATE TEMP TABLE order_reconciliation_results AS
WITH order_totals AS (
    SELECT
        o.order_id,
        c.first_name || ' ' || c.last_name AS customer,
        o.status,
        COUNT(oi.order_item_id) AS item_count,
        COALESCE(SUM(oi.quantity * oi.unit_price), 0)::NUMERIC(10, 2)
            AS order_total,
        p.amount AS payment_amount,
        p.payment_status
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    LEFT JOIN order_items oi ON o.order_id = oi.order_id
    LEFT JOIN payments p ON o.order_id = p.order_id
    GROUP BY
        o.order_id,
        c.first_name,
        c.last_name,
        o.status,
        p.amount,
        p.payment_status
)
SELECT
    order_id,
    customer,
    status,
    item_count,
    order_total,
    payment_amount,
    payment_status,
    CASE
        WHEN item_count = 0 THEN 'FAIL: no order items'
        WHEN payment_amount IS NULL THEN 'FAIL: missing payment'
        WHEN payment_amount <> order_total THEN 'FAIL: amount mismatch'
        ELSE 'PASS'
    END AS reconciliation_status
FROM order_totals;

SELECT *
FROM order_reconciliation_results
ORDER BY order_id;

DO $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM order_reconciliation_results
        WHERE reconciliation_status <> 'PASS'
    ) THEN
        RAISE EXCEPTION
            'Order reconciliation failed: one or more orders have missing items, missing payments, or mismatched totals.';
    END IF;
END
$$;
