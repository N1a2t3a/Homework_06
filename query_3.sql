SELECT g.group_name, AVG(grade) AS average_grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects sub ON g.subject_id = sub.subject_id
JOIN groups gr ON s.group_id = gr.group_id
WHERE sub.subject_name = 'History'
GROUP BY g.group_name;
