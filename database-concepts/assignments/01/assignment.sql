-- Use a sql sub-query statement to answer the following:

-- Provide the SQL statements using subqueries to satisfy the requests.
-- Only ones with correct result will be awarded mark.
-- The primary key of order_items is a composite key of order_id and item_id

-- 1. List the product that have max quantities ordered in one order.
-- a)
SELECT 
    oi.product_id,
    oi.order_id,
    SUM(oi.quantity) AS total_quantity
FROM
    order_items oi
GROUP BY
    oi.order_id, oi.product_id
HAVING
    SUM(oi.quantity) = (
        SELECT 
            MAX(total_quantity)
        FROM (
            SELECT 
                oi2.order_id,
                SUM(oi2.quantity) AS total_quantity
            FROM 
                order_items oi2
            GROUP BY 
                oi2.order_id, oi2.product_id
        )
    );

-- b)
SELECT *
FROM (
    SELECT product_id, order_id, SUM(quantity) as total_quantity
    FROM order_items
    GROUP BY product_id, order_id
    ORDER BY SUM(quantity) DESC
)
WHERE ROWNUM = 1;

-- 2. List the name and quantity of the inventory product with minimum quantity (excluding nulls).
select * from inventories;

-- a)
SELECT p.product_name, MIN(inv.total_inventory)
FROM (
    -- total inventory (across all warehouses)
    SELECT product_id, SUM(quantity) total_inventory
    FROM inventories
    WHERE quantity IS NOT NULL
    GROUP BY product_id
    ORDER BY SUM(quantity)
) inv
JOIN products p on inv.product_id = p.product_id
WHERE ROWNUM = 1
GROUP BY p.product_name;

-- b)
SELECT p.product_name, SUM(quantity)
FROM inventories i
JOIN products p ON i.product_id = p.product_id
GROUP BY p.product_name
-- the sum of all inventory quantities of one product that matches the min
HAVING SUM(quantity) = (
    -- min total inventory
    SELECT MIN(total_inventory)
    FROM (
        -- total inventory (across all warehouses)
        SELECT SUM(quantity) total_inventory
        FROM inventories 
        WHERE quantity IS NOT NULL
        GROUP BY product_id
    )
);

