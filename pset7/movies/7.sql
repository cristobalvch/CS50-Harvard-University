SELECT m.title,r.rating FROM movies AS m
JOIN ratings AS r
ON m.id = r.movie_id
WHERE m.year = '2010' AND  r.rating IS NOT NULL
ORDER BY r.rating DESC,m.title;
