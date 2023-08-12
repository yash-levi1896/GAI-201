Problem1: Create a Customers table / collection with the following fields: id (unique identifier), name, email, address, and phone_number.

Ans:CREATE TABLE Customers (
    id INT PRIMARY KEY NOT NULL,
    name VARCHAR(100),
    email VARCHAR(100),
    address VARCHAR(255),
    phone_number INT
);
Problem2: Insert five rows / documents into the Customers table / collection with data of your choice.
Ans:INSERT INTO Customers (id, name, email, address, phone_number)
VALUES
    (1, 'Alice Johnson', 'alice@example.com', '123 Main St, City', 1234567890),
    (2, 'Bob Smith', 'bob@example.com', '456 Elm Rd, Town', 9876543210),
    (3, 'Carol Davis', 'carol@example.com', '789 Oak Ave, Village', 5551234567),
    (4, 'David Brown', 'david@example.com', '321 Pine St, Hamlet', 1112223333),
    (5, 'Eve Williams', 'eve@example.com', '555 Maple Dr, Suburb', 9998887777);

Problem3: Write a query to fetch all data from the Customers table / collection.

Ans: SELECT * FROM Customers

Problem4: Write a query to select only the name and email fields for all customers.

Ans: SELECT name , email FROM Customers

Problem5:Write a query to fetch the customer with the id of 3.

Ans: SELECT * FROM Customers WHERE id=3

Problem6:Write a query to fetch all customers whose name starts with 'A'.

Ans: SELECT * FROM Customers WHERE name LIKE A%

Problem7: Write a query to fetch all customers, ordered by name in descending order.

Ans:SELECT * FROM Customers ORDER BY name DESC

Problem8:Write a query to update the address of the customer with id 4.
Ans:UPDATE Customers SET address = 'xyz street' WHERE id = 4;

Problem9:Write a query to fetch the top 3 customers when ordered by id in ascending order.

Ans:SELECT * FROM Customers ORDER BY id LIMIT 3

Problem10:Write a query to delete the customer with id 2.
Ans:DELETE FROM Customers WHERE id = 2;

Problem11: Write a query to count the number of customers.
Ans: SELECT count(*) FROM Customers

Problem12:- Write a query to fetch all customers except the first two when ordered by **`id`** in ascending order.

Ans:SELECT * FROM Customers ORDER BY id OFFSET 2;

Problem13:Write a query to fetch all customers whose id is greater than 2 and name starts with 'B'.

Ans:SELECT * FROM Customers WHERE id > 2 AND name LIKE B%.

Problem14:Write a query to fetch all customers whose id is less than 3 or name ends with 's'.

Ans:SELECT * FROM Customers WHERE id < 3 AND name LIKE %s.

Problem15:Write a query to fetch all customers where the phone_number field is not set or is null.

Ans: SELECT * FROM Customers WHERE phone_number IS NULL;