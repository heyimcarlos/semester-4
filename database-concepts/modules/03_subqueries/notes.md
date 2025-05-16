# Subqueries

- Subqueries can go in the SELECT, FROM, WHERE, and HAVING clauses.

```sql
-- Subquery in the SELECT clause
SELECT employee_id, last_name,
       (SELECT department_id FROM departments WHERE department_name = 'Sales') AS sales_department
FROM employees;

-- Subquery in the FROM clause
SELECT employee_id, last_name
FROM employees
WHERE department_id = (SELECT department_id FROM departments WHERE department_name = 'Sales');

-- Subquery in the WHERE clause
SELECT employee_id, last_name
FROM employees
WHERE department_id IN (SELECT department_id FROM departments WHERE location_id = 1700);

-- Subquery in the HAVING clause
SELECT department_id, COUNT(*)
FROM employees
GROUP BY department_id
HAVING COUNT(*) > (SELECT AVG(employee_count) FROM (SELECT department_id, COUNT(*) AS employee_count FROM employees GROUP BY department_id));
```

1. one column / one row: gte, gt, le, lte (arithmetic operators)

```sql
-- One column / one row
SELECT *
FROM employees
WHERE employee_id = (SELECT employee_id FROM employees WHERE last_name = 'King');
```

2. one column / multiple rows: IN, ANY, ALL, EXISTS

3. multiple columns / rows:

```sql

```

uncorrelated subquery: a subquery that can be executed independently of the outer query.
