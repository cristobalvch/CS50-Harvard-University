SELECT AVG(r.rating) FROM ratings AS r
JOIN movies AS m
ON r.movie_id = m.id
WHERE m.year ='2012';