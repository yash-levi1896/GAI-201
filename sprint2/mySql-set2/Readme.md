Problem16:Create a Restaurants table / collection with the fields defined above.
Ans:CREATE TABLE Restaurants (
    id INT PRIMARY KEY NOT NULL,
    name VARCHAR(100),
    cuisine_type VARCHAR(100),
    location VARCHAR(255),
    average_rating DECIMAL(3,2),
    delivery_available BOOLEAN
);

Proble17:Insert five rows / documents into the Restaurants table / collection with data of your choice.

Ans:INSERT INTO Restaurants (id, name, cuisine_type, location, average_rating, delivery_available)
VALUES
    (1, 'Tasty Bites', 'Italian', '123 Main St', 4.5, TRUE),
    (2, 'Spice House', 'Indian', '555 Oak Ave', 4.2, TRUE),
    (3, 'Sushi Delight', 'Japanese', '987 Maple Dr', 4.8, TRUE),
    (4, 'Burger Joint', 'American', '777 Walnut Rd', 4.0, TRUE),
    (5, 'Mama Mia Pizzeria', 'Italian', '222 Pine Rd', 4.6, TRUE);

Problem18:Write a query to fetch all restaurants, ordered by average_rating in descending order.

Ans:SELECT * FROM Restaurants ORDER BY average_rating DESC

Problem19:Write a query to fetch all restaurants that offer delivery_available and have an average_rating of more than 4.

Ans:SELECT * Restaurants WHERE delivery_available=TRUE AND average_rating > 4

Problem20:Write a query to fetch all restaurants where the cuisine_type field is not set or is null.

Ans: SELECT * FROM Restaurants WHERE cuisine_type IS NULL;

Problem21:Write a query to count the number of restaurants that have delivery_available.

Ans:SELECT count(*) FROM Restaurants WHERE delivery_available=TRUE

Problem22:Write a query to fetch all restaurants whose location contains 'New York'.

Ans: SELECT * FROM Restaurants WHERE location LIKE %New York%

Problem23:Write a query to calculate the average average_rating of all restaurants.

Ans:SELECT avg(average_rating) AS AvgRating FROM Restaurants

Problem24:Write a query to fetch the top 5 restaurants when ordered by average_rating in descending order.

Ans:SELECT TOP 5 * FROM Restaurants ORDER BY average_rating DESC

Problem25:Write a query to delete the restaurant with id 3.
Ans:DELETE FROM Restaurants WHERE id=3;