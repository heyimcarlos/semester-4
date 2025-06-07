-- Instructions: Be sure to read the following general instructions carefully:

-- Your files must be in sql script format so that they can be run in SQL Developer and have DBMS_OUTPUT.PUT_LINE for presenting results.

select * from order_items where order_id = 1003;

-- 1. Company application page is being developed for employees to enter a Order number and view customer address information for the order. An Status Shipped indicates that the order has been shipped. In this assignment, you create a block using scalar variables to hold the data retrieved from the database.
/* DECLARE
  v_order_id NUMBER := 1003;
  v_customer_name VARCHAR2(100);
  v_shipping_status VARCHAR2(20);
  v_address VARCHAR2(200);
BEGIN
  BEGIN
    SELECT c.name, c.address, o.status
    INTO v_customer_name, v_address, v_shipping_status
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    WHERE o.order_id = v_order_id;
  EXCEPTION
    WHEN NO_DATA_FOUND THEN
      DBMS_OUTPUT.PUT_LINE('No order found');
    RETURN;
  END;
  DBMS_OUTPUT.PUT_LINE('Customer name: ' || v_customer_name);
  DBMS_OUTPUT.PUT_LINE('Shipping status: ' || v_shipping_status);
  DBMS_OUTPUT.PUT_LINE('Address: ' || v_address);
EXCEPTION
  WHEN OTHERS THEN
    DBMS_OUTPUT.PUT_LINE('An error occurred: ' || SQLERRM);
END; */

-- 2. Company application needs a block to determine whether a customer is rated HIGH, MID, or LOW based on his or her total purchases. The block needs to select the total amount of orders for a specified customer, determine the rating, and then display the results onscreen. The code rates the customer HIGH if total purchases are greater than $200, MID if greater than $100, and LOW if $100 or lower. Use an initialized variable to provide the customer ID.
/* DECLARE
  v_customer_id NUMBER := 2;
  v_total_purchases NUMBER;
  v_customer_rating VARCHAR2(10);
BEGIN
  -- NOTE: Isolate total purchases calc
  BEGIN
    SELECT SUM(oi.quantity * oi.unit_price)
    INTO v_total_purchases
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.customer_id = v_customer_id;
    -- If no orders found, initiate v_total_purchases to 0
    IF v_total_purchases IS NULL THEN
      v_total_purchases := 0;
    END IF;
  EXCEPTION
    WHEN NO_DATA_FOUND THEN
      DBMS_OUTPUT.PUT_LINE('Customer not found or no orders exist.');
  END;
  -- NOTE: Rating selection logic
  IF v_total_purchases > 200 THEN
    v_customer_rating := 'HIGH';
  ELSIF v_total_purchases > 100 THEN
    v_customer_rating := 'MID';
  ELSE
    v_customer_rating := 'LOW';
  END IF;
  DBMS_OUTPUT.PUT_LINE('Customer ID: ' || v_customer_id);
  DBMS_OUTPUT.PUT_LINE('Total Spent: ' || v_total_purchases);
  DBMS_OUTPUT.PUT_LINE('Customer Rating: ' || v_customer_rating);
-- NOTE: Catch all block
EXCEPTION
  WHEN OTHERS THEN
    DBMS_OUTPUT.PUT_LINE('An error occurred: ' || SQLERRM);
END; */
 
-- 3. Management wants to include a feature in its application that calculates the total amount (quantity) of a specified item that can be purchased with a given amount of money. Create a block with a WHILE loop to increment the item’s cost until the dollar value is met. Test first with a total spending amount of $100 and product ID of your choice. Then test with an amount and a product of your choice. Use initialized variables to provide the total spending amount and product_ID.
/* DECLARE
  v_spending_amount NUMBER := 640.99;
  v_amount_spent NUMBER := 0;
  v_product_id NUMBER := 10000;
  v_item_cost NUMBER;
  v_total_bought NUMBER := 0;
BEGIN
  BEGIN
    SELECT list_price
    INTO v_item_cost
    FROM products
    WHERE product_id = v_product_id;
  EXCEPTION
    WHEN NO_DATA_FOUND THEN
      DBMS_OUTPUT.PUT_LINE('Product not found.');
      RETURN;
  END;
    WHILE (v_amount_spent + v_item_cost) <= v_spending_amount LOOP
      v_total_bought := v_total_bought + 1;
      v_amount_spent := v_amount_spent + v_item_cost;
    END LOOP;
  DBMS_OUTPUT.PUT_LINE('Product Cost: $' || v_item_cost);
  DBMS_OUTPUT.PUT_LINE('Product ID: ' || v_product_id);
  DBMS_OUTPUT.PUT_LINE('Items bought: ' || v_total_bought);
EXCEPTION
  WHEN OTHERS THEN
    DBMS_OUTPUT.PUT_LINE('An error occurred: ' || SQLERRM);
END; */

-- 4. . Company calculates shipping cost based on the quantity of all items in an order. Assume the quantity column in the Order items table contains the total number of items in an individual basket item. A block is needed to check the quantity provided by an initialized variable and determine the shipping cost. Display the calculated shipping cost onscreen. Test using the Order_IDs 100 and 1003, and apply the shipping rates listed in Table.
/* Quantity of Items Shipping Cost
Up to 300 $50.00
300–600 $75.00
600–1000 $100.00
More than 1000 $120.00 */
DECLARE
  v_order_id NUMBER;
  v_total_item_quantity NUMBER;
  v_shipping_cost NUMBER;
BEGIN
  v_order_id := 1;
  SELECT SUM(quantity)
  INTO v_total_item_quantity
  FROM order_items
  WHERE order_id = v_order_id;

  IF v_total_item_quantity IS NULL THEN
    Raise NO_DATA_FOUND;
  END IF;

  -- Determine shipping cost based on quantity
  IF v_total_item_quantity <= 300 THEN
    v_shipping_cost := 50;
  ELSIF v_total_item_quantity <= 600 THEN
    v_shipping_cost := 75;
  ELSIF v_total_item_quantity <= 1000 THEN
    v_shipping_cost := 100;
  ELSE
    v_shipping_cost := 120;
  END IF;

  DBMS_OUTPUT.PUT_LINE('Order ID: ' || v_order_id);
  DBMS_OUTPUT.PUT_LINE('Total Quantity: ' || v_total_item_quantity);
  DBMS_OUTPUT.PUT_LINE('Shipping Cost: $' || TO_CHAR(v_shipping_cost));
EXCEPTION
  WHEN NO_DATA_FOUND THEN
    DBMS_OUTPUT.PUT_LINE('No order items found for order id ' || v_order_id);
  WHEN OTHERS THEN
    DBMS_OUTPUT.PUT_LINE('An error occurred: ' || SQLERRM);
END;

-- 5. The company application contains a page displaying order summary information, from the Orders table. Create a PL/SQL block with a record variable to retrieve this data and display it onscreen. An initialized variable should provide the Order_ID value. Test the block using the Order ID 100.
/* DECLARE
  v_order_id NUMBER := 100;
  TYPE order_record is RECORD (
    order_id NUMBER,
    customer_id NUMBER,
    order_date DATE,
    status VARCHAR2(20),
    salesman_id NUMBER
  );
  v_order order_record;
BEGIN
  SELECT order_id, customer_id, order_date, status, salesman_id
  INTO v_order.order_id, v_order.customer_id, v_order.order_date, v_order.status, v_order.salesman_id
  FROM orders
  WHERE order_id = v_order_id;

  DBMS_OUTPUT.PUT_LINE('Order ID: ' || v_order.order_id);
  DBMS_OUTPUT.PUT_LINE('Customer ID: ' || v_order.customer_id);
  DBMS_OUTPUT.PUT_LINE('Order Date: ' || TO_CHAR(v_order.order_date, 'YYYY-MM-DD'));
  DBMS_OUTPUT.PUT_LINE('Status: ' || v_order.status);
  DBMS_OUTPUT.PUT_LINE('Salesman ID: ' || v_order.salesman_id);
END; */
