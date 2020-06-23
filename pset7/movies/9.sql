SELECT DISTINCT p.name  FROM stars AS s
JOIN people AS p
ON s.person_id = p.id
JOIN movies AS m
ON s.movie_id = m.id
WHERE m.year = 2004
ORDER BY p.birth;
