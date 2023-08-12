Problem36:Write a query to find the ride with the highest and lowest fare
Ans:SELECT max(fare) AS MaxFare,min(fare) AS MinFare FROM Rides

Problem37:Write a query to find the average fare and distance for each driver_id.
Ans:SELECT avg(fare) AS AvgFare,avg(distance) AS AvgDistance FROM Rides GROUP BY driver_id

Problem38:Write a query to find driver_id that have completed more than 5 rides.
Ans:SELECT count(*),dirver_id FROM Rides GROUP BY driver_id HAVING count>5

Problem39:Assuming there is another collection/table called Drivers with driver_id and name fields, write a query to find the name of the driver with the highest fare.

Ans:SELECT Drivers.name FROM Rides JOIN Drivers ON Rides.driver_id = Drivers.driver_id ORDER BY Rides.fare DESC LIMIT 1;

Problem40:Write a query to find the top 3 drivers who have earned the most from fares. Return the drivers' ids and total earnings.
Ans:SELECT driver_id, SUM(fare) AS total_earnings FROM Rides GROUP BY driver_id ORDER BY total_earnings DESC LIMIT 3;

Problem41:Assuming there's a ride_date field of date type in the Rides table / collection, write a query to find all rides that happened in the last 7 days.

Ans: SELECT * FROM Rides WHERE ride_date >= CURRENT_DATE - INTERVAL 7 DAY;

Problem42:Write a query to find all rides where the end_location is not set.
Ans:SELECT * FROM Rides WHERE end_location IS NULL;

Problem43:Write a query to calculate the fare per mile for each ride and return the ride ids and their fare per mile, ordered by fare per mile in descending order.
Ans:SELECT id AS ride_id, fare / distance AS fare_per_mile FROM Rides WHERE distance > 0 ORDER BY fare_per_mile DESC;

Problem44:Assuming there's another collection/table Passengers with passenger_id and name fields, write a query to return a list of all rides including the driver's name and passenger's name.

Ans:SELECT Rides.id AS ride_id, Drivers.name AS driver_name, Passenger.name AS passenger_name FROM Rides  JOIN Drivers  ON Rides.driver_id = Drivers.driver_id JOIN Passengers  ON Rides.passenger_id = Passenger.passenger_id;

Problem45:Write a query to add a tip field to the Rides table / collection.

Ans:ALTER TABLE Rides ADD tip DECIMAL(6,2);
