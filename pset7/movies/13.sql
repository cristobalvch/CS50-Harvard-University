SELECT  DISTINCT p.name FROM people AS p
JOIN stars AS s
ON p.id = s.person_id
WHERE s.movie_id IN
    (SELECT s.movie_id FROM stars AS s
    JOIN people AS p
    ON s.person_id = p.id
    WHERE p.name = 'Kevin Bacon'
    AND p.birth = 1958)
    AND p.name <> 'Kevin Bacon';

