Problem26: Create a Rides table / collection with the fields defined above.
Ans:CREATE TABLE Rides (
    id INT PRIMARY KEY NOT NULL,
    driver_id INT,
    passenger_id INT,
    start_location VARCHAR(255),
    end_location VARCHAR(255),
    distance DECIMAL(5,2),
    ride_time DECIMAL(5,2),
    fare DECIMAL(6,2)
);

Problem27:- Insert five rows / documents into the **`Rides`** table / collection with data of your choice.
Ans:INSERT INTO Rides (id, driver_id, passenger_id, start_location, end_location, distance, ride_time, fare)
VALUES
    (1, 101, 201, '123 Main St', '456 Elm St', 10.75, 20.5, 30.00),
    (2, 102, 202, '555 Oak Ave', '789 Pine Rd', 8.20, 15.75, 25.50),
    (3, 103, 203, '987 Maple Dr', '321 Birch Ln', 5.50, 10.25, 15.75),
    (4, 104, 204, '777 Walnut Rd', '888 Cedar Ave', 3.00, 5.75, 10.25),
    (5, 105, 205, '222 Pine Rd', '111 Oak Ave', 12.40, 25.00, 40.50);

Problem28:Write a query to fetch all rides, ordered by fare in descending order.
Ans:SELECT * FROM Rides ORDER BY fare DESC

Problem29: Write a query to calculate the total distance and total fare for all rides.
Ans:SELECT sum(distance) AS total distance , sum(fare) AS TotalFare FROM Rides 

Problem30:Write a query to calculate the average ride_time of all rides.
Ans:SELECT avg(ride_time) AS AvgRideTime FROM Rides

Problem31:Write a query to fetch all rides whose start_location or end_location contains 'Downtown'.
Ans:SELECT * FROM Rides WHERE start_location LIKE %Downtown% OR end_location LIKE %Downtown%

Problem32:Write a query to count the number of rides for a given driver_id.
Ans:SELECT driver_id ,count(*) AS ride_count FROM Rides GROUP BY driver_id
Ans:SELECT count(*) FROM AS ride_count FROM Rides WHERE driver_id=<given_id>

Problem33:Write a query to update the fare of the ride with id 4.
Ans:UPDATE Rides SET fare = 12.25 WHERE id = 4;

Problem34:Write a query to calculate the total fare for each driver_id.
Ans:SELECT driver_id , sum(fare) AS ToatlFare FROM Rides GROUP BY driver_id.

Problem35:Write a query to delete the ride with id 2.
Ans:DELETE FROM Rides WHERE id=2;
 