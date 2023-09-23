SELECT s.first_name, s.last_name, AVG(g.grade) AS average_grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects sub ON g.subject_id = sub.subject_id
WHERE sub.subject_name = 'Mathematics'
GROUP BY s.student_id, s.first_name, s.last_name
ORDER BY average_grade DESC

