-- Carlos De La Cruz | 301391100
-- Use a sql sub-query statement to answer the following:

-- Provide the SQL statements using subqueries to satisfy the requests.
-- Only ones with correct result will be awarded mark.
-- The primary key of order_items is a composite key of order_id and item_id

-- 1. List the product that have max quantities ordered in one order.

-- a) HAVING
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

-- b) ROWNUM
SELECT *
FROM (
    SELECT product_id, order_id, SUM(quantity) as total_quantity
    FROM order_items
    GROUP BY product_id, order_id
    ORDER BY SUM(quantity) DESC
)
WHERE ROWNUM = 1;

-- 2. List the name and quantity of the inventory product with minimum quantity (excluding nulls).

-- a) ROWNUM
SELECT p.product_name, MIN(i.total_inventory)
FROM (
    -- total inventory (across all warehouses)
    SELECT product_id, SUM(quantity) total_inventory
    FROM inventories
    WHERE quantity IS NOT NULL
    GROUP BY product_id
    ORDER BY SUM(quantity)
) i
JOIN products p on i.product_id = p.product_id
WHERE ROWNUM = 1
GROUP BY p.product_name;

-- b) HAVING (returns several if tied on low quantity)
SELECT p.product_name, SUM(quantity)
FROM inventories i
JOIN products p ON i.product_id = p.product_id
GROUP BY p.product_name
-- the sum of all inventory quantities of one product that matches the min
HAVING SUM(quantity) = (
    SELECT MIN(SUM(quantity))
    FROM inventories 
    WHERE quantity IS NOT NULL
    GROUP BY product_id
);

-- 3. List the countries with maximum numbers of locations.
SELECT c.country_id, c.country_name, COUNT(*) location_count
FROM countries c
JOIN locations l ON c.country_id = l.country_id
GROUP BY c.country_id, c.country_name
HAVING COUNT(*) = (
    SELECT MAX(COUNT(*))
    FROM locations
    GROUP BY country_id
);

-- 4. List the salesman(s) with maximum number of orders.
SELECT e.employee_id, CONCAT(CONCAT(e.first_name, ' '), e.last_name) name, COUNT(*) order_count
FROM orders o
JOIN employees e ON o.salesman_id = e.employee_id
GROUP BY e.employee_id, CONCAT(CONCAT(e.first_name, ' '), e.last_name)
HAVING COUNT(*) = (
    SELECT MAX(COUNT(*))
    FROM orders
    WHERE salesman_id IS NOT NULL
    GROUP BY salesman_id
);

-- 5. List the customer(s) with max number of orders.
SELECT c.customer_id, c.name, COUNT(*)
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING COUNT(*) = (
    SELECT MAX(COUNT(*)) order_count
    FROM orders
    GROUP BY customer_id
);
