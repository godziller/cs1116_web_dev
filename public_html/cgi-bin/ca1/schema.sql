
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userId INTEGER KEY,
    title TEXT NOT NULL,
    description TEXT,
    due_date DATE,
    priority TEXT DEFAULT 'High',
    status TEXT DEFAULT 'New'
);

CREATE TABLE users (
    userId INTEGER PRIMARY KEY AUTOINCREMENT,
    surname TEXT,
    firstname TEXT,
    email TEXT,
    password TEXT
);


INSERT INTO tasks (id, userId, title, description, due_date, priority, status)
VALUES
    (2,11,'testing title', 'testing description', '2025-12-08', 'High', 'pending')
    
;

select * from tasks;

select * from users
DELETE FROM tasks



