query = "SELECT * \
		FROM flight \
		WHERE countryID = ( SELECT countryID \
							FROM country \
							WHERE countryName = 'London');"