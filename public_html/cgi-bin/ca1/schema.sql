# Database structure for Users #TODO:

#date, priority and string(description of task), unique task identifier 

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
    userId INTEGER PRIMARY KEY AUTOINCREMENT
    surname TEXT,
    firstname TEXT,
    email TEXT,
    password TEXT,
)

#Database structure for Tasks



# Database structure for Projects
