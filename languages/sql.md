- acid
        - atomicity: each tx fails/succeeds completely (vs. some steps in the tx succeeding, even with loss of power, process interruption, etc)
        - consistency: each tx links valid states
        - isolation: concurrent tx = sequential tx
        - durability: completed tx are in non-volatile memory (retained if system crashes)

    - transactions:
        - support start, lock object, execution, atomic commit or roll back of operation(s) in the transaction object
        - other transaction types or applications: distributed transactions across multiple network nodes, multi-layer/nested transactions, object transactions, file system transactions



- db: SQL queries, database admin
	- Data definition language or DDL allows to execute queries that define the data schema like CREATE, DROP and ALTER table
	- Data manipulation Language or DML is used to access or manipulate data in the database (insert/delete rows)
	- primary key vs. unique constraint: Primary key cannot have NULL value
	- foreign key identifies a row in another table
	- Views in SQL: virtual tables, created by selecting columns, with optional conditions

	- get max value of a column (salary) given a group defined by another column (department)
		SELECT Id, Departmentid, MAX(Salary) FROM employees e GROUP BY e.DepartmentId;

	- sub queries

		SELECT article, dealer, price FROM  shop s1 WHERE price = (SELECT MAX(s2.price) FROM shop s2 WHERE s1.article = s2.article);

		SELECT s1.article, dealer, s1.price FROM shop s1 JOIN (
		  SELECT article, MAX(price) AS price
		  FROM shop
		  GROUP BY article) AS s2
		  ON s1.article = s2.article AND s1.price = s2.price;

		SELECT * FROM employees e
		   JOIN (SELECT MAX(video_id) AS id FROM videos GROUP BY video_category) max
		      ON s.video_id = max.id

		SELECT * from employees e LEFT JOIN departments d on e.departmentId = d.id where (SELECT MAX(e2.salary) from employees e2 WHERE e2.departmentId = d.id);

		SELECT * from employees e LEFT JOIN departments d on e.departmentId = d.id where e.salary = (SELECT MAX(e.salary) from e where e.departmentId = d.id);

	- joins

		- join three tables
			SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
			FROM ((Orders
			INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
			INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID); 

	    - inner join (default join):
	    	- selects all rows from both tables that the condition satisfies (value of the common field is the same)
	    
	    - outer joins

		    - left (outer) JOIN:
		    	- returns all rows of table on left side of join, and matching rows for table on right side of join.
		    	- contains null for rows with no matching row on right side
		    
		    - right (outer) join:
		       	- returns all rows of table on right side of join, and matching rows for table on left side of join.
		    	- contains null for rows with no matching row on left side
		    
		    - full join:
		    	- returns all rows of tables on left & right side of join
		    	- contains null for rows with no matching row on right or left side
		    