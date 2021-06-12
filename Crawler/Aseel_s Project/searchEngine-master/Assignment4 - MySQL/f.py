query = "SELECT country.countryName, COUNT(fliNO) AS allFlights, ROUND(AVG(passTotal), 0) AS average \
		FROM (SELECT flight.flightID AS fliNO, flight.countryID AS counNO, Count(passengerID) AS passTotal \
			FROM flight LEFT OUTER JOIN reservation on flight.flightID = reservation.flightID \
			GROUP BY flight.flightID \
			) AS q1 \
		LEFT OUTER JOIN country on counNO = country.countryID \
		GROUP BY q1.counNO \
		;"

            #SELECT country.name, COUNT(flightID) AS total
#FROM country LEFT OUTER JOIN flight on flight.countryID = country.countryID 
#GROUP BY country.countryID

# left join with country table
# 
#  
# SELECT couNO, AVG(passTotal), COUNT(fliNO)
# FROM (	SELECT flight.flightNo AS fliNO, flight.countryID AS couNO, Count(passID) AS passTotal
# 	FROM flight LEFT OUTER JOIN pass_flight on flight.flightID = pass_flight.flightID 
# 	GROUP BY flight.flightID
#      )
# GROUP BY couNO
