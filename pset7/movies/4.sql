SELECT COUNT(*) AS 'Number of movies with IMDb rating of 10.0'
FROM movies AS m
JOIN ratings AS r
ON  m.id = r.movie_id
WHERE r.rating =10.0;
