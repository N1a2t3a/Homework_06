SELECT t.first_name, t.last_name, sub.subject_name
FROM teachers t
JOIN subjects sub ON t.teacher_id = sub.teacher_id;
