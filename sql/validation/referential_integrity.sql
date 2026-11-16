CREATE TEMP TABLE referential_integrity_results AS
SELECT
    'orders_without_customers' AS check_name,
    COUNT(*) AS failures
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL

UNION ALL

SELECT
    'items_without_orders',
    COUNT(*)
FROM order_items oi
LEFT JOIN orders o ON oi.order_id = o.order_id
WHERE o.order_id IS NULL

UNION ALL

SELECT
    'items_without_products',
    COUNT(*)
FROM order_items oi
LEFT JOIN products p ON oi.product_id = p.product_id
WHERE p.product_id IS NULL;

SELECT check_name, failures
FROM referential_integrity_results
ORDER BY check_name;

DO $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM referential_integrity_results
        WHERE failures > 0
    ) THEN
        RAISE EXCEPTION
            'Referential integrity validation failed: one or more orphaned records were found.';
    END IF;
END
$$;
