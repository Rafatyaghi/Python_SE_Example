query = "SELECT Count(passengerID) AS total \
        FROM flight, reservation \
        WHERE flight.flightID = reservation.flightID AND Year(flight.arrivalTime) = 2020;"