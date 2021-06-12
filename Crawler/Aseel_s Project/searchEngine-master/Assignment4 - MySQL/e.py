query = "SELECT passenger.fname, passenger.lname  \
        FROM passenger \
        WHERE countryOfBirthID = (SELECT countryID FROM country WHERE countryName = 'Palestine')  AND passengerID IN ( \
            SELECT passengerID \
            FROM flight, reservation \
            WHERE (flight.direction = '0' AND flight.departureTime <= DATE_ADD(NOW(), INTERVAL 3 HOUR)) \
               OR (flight.direction = '1' AND flight.arrivalTime <= DATE_ADD(NOW(), INTERVAL 3 HOUR)) \
        );"