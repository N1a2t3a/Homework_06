SELECT s.first_name, s.last_name, g.grade
FROM students s
JOIN groups gr ON s.group_id = gr.group_id
JOIN grades g ON s.student_id = g.student_id
JOIN subjects sub ON g.subject_id = sub.subject_id
WHERE gr.group_name = 'Group B' AND sub.subject_name = 'Biology';
