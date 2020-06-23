SELECT DISTINCT p.name FROM people as p
JOIN directors AS D
ON p.id = d.person_id
JOIN ratings as r
ON d.movie_id = r.movie_id
WHERE r.rating >='9.0';