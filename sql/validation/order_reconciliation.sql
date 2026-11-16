SELECT
    o.order_id,
    c.first_name || ' ' || c.last_name AS customer,
    o.status,
    SUM(oi.quantity * oi.unit_price) AS order_total,
    p.amount AS payment_amount,
    p.payment_status,
    p.amount - SUM(oi.quantity * oi.unit_price) AS difference
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products pr ON oi.product_id = pr.product_id
JOIN payments p ON o.order_id = p.order_id
GROUP BY
    o.order_id,
    c.first_name,
    c.last_name,
    o.status,
    p.amount,
    p.payment_status
ORDER BY o.order_id;
