SELECT m.title FROM movies AS m
JOIN ratings AS r
ON m.id = r.movie_id
WHERE r.movie_id IN
    (SELECT s.movie_id FROM stars AS s
    JOIN people AS p
    ON s.person_id = p.id
    WHERE p.name = 'Chadwick Boseman')
ORDER BY r.rating DESC LIMIT 5;