
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER KEY,
    title TEXT NOT NULL,
    description TEXT,
    due_date DATE,
    priority TEXT DEFAULT 'High',
    status TEXT DEFAULT 'New'
);

    CREATE TABLE users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        surname TEXT,
        first_name TEXT,
        email TEXT,
        password TEXT
    );


INSERT INTO tasks (id, user_id, title, description, due_date, priority, status)
VALUES
    (2,11,'testing title', 'testing description', '2025-12-08', 'High', 'pending')
    
;

select * from tasks;
SELECT * FROM tasks WHERE user_id = 1
select * from users
DELETE FROM users
DROP TABLE tasks


