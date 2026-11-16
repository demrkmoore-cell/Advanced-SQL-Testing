CREATE TEMP TABLE inventory_validation_results AS
SELECT
    product_id,
    product_name,
    sku,
    stock_quantity,
    CASE
        WHEN stock_quantity >= 0 THEN 'PASS'
        ELSE 'FAIL'
    END AS stock_check
FROM products;

SELECT
    product_id,
    product_name,
    sku,
    stock_quantity,
    stock_check
FROM inventory_validation_results
ORDER BY product_id;

DO $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM inventory_validation_results
        WHERE stock_check = 'FAIL'
    ) THEN
        RAISE EXCEPTION
            'Inventory validation failed: one or more products have negative stock.';
    END IF;
END
$$;
