SELECT p.name FROM people AS p
JOIN stars AS s
ON p.id = s.person_id
JOIN movies AS m
ON s.movie_id = m.id
WHERE m.title ='Toy Story';