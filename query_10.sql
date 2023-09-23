SELECT s.first_name, s.last_name, sub.subject_name
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects sub ON g.subject_id = sub.subject_id
JOIN teachers t ON sub.teacher_id = t.teacher_id
WHERE s.first_name = 'Oleksandr' AND s.last_name = 'Bohdanets' AND t.first_name = 'Anastasia' AND t.last_name = 'Panko';
