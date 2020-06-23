SELECT m.title FROM movies as m
JOIN stars AS s
ON m.id = s.movie_id
WHERE s.person_id =
    (SELECT p.id FROM people AS p
    WHERE  p.name = 'Helena Bonham Carter')
INTERSECT
SELECT m.title FROM movies as m
JOIN stars AS s
ON m.id = s.movie_id
WHERE s.person_id =
    (SELECT p.id FROM people AS p
    WHERE  p.name = 'Johnny Depp');
