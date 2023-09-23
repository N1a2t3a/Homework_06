SELECT s.first_name, s.last_name
FROM students s
JOIN groups gr ON s.group_id = gr.group_id
WHERE gr.group_name = 'Group A';
