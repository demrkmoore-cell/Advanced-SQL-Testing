SELECT
    product_id,
    product_name,
    sku,
    stock_quantity,
    CASE
        WHEN stock_quantity >= 0 THEN 'PASS'
        ELSE 'FAIL'
    END AS stock_check
FROM products
ORDER BY product_id;
