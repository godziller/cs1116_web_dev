
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
    (1,10,'testing title', 'testing description', '8/10/2004', 'High', 'New')
; 




