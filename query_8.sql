SELECT t.first_name, t.last_name, AVG(g.grade) AS average_grade
FROM teachers t
JOIN subjects sub ON t.teacher_id = sub.teacher_id
JOIN grades g ON sub.subject_id = g.subject_id
GROUP BY t.teacher_id, t.first_name, t.last_name;
