query = "SELECT flight.flightID,Count(passengerID) AS total, flight.departureTime \
			FROM flight LEFT OUTER JOIN reservation on flight.flightID = reservation.flightID \
			WHERE Year(flight.departureTime) = 2020 AND Month(flight.departureTime) = 5 \
			GROUP BY flight.flightID;"