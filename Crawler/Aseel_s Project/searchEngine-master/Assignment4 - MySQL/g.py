query = "SELECT passenger.*, Count(flightID) AS allFights \
        FROM passenger \
        LEFT OUTER JOIN reservation on passenger.passengerID = reservation.passengerID \
        GROUP BY passenger.passengerID \
        ORDER BY Count(flightID) DESC \
        LIMIT 5 \
        ;"