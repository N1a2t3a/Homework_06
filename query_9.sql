SELECT s.first_name, s.last_name, sub.subject_name
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects sub ON g.subject_id = sub.subject_id;
