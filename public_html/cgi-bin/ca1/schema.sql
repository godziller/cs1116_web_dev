
DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS traffic_logs;


CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER KEY,
    title TEXT NOT NULL,
    description TEXT,
    due_date DATE,
    priority TEXT DEFAULT 'High',
    status TEXT DEFAULT 'New' /* Can be New, In Progress, Done, Abandoned */
);

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    surname TEXT,
    first_name TEXT,
    email TEXT,
    password TEXT,
    is_admin INTEGER DEFAULT False   /* boolean to identify if user has admin privleges or not */
);

CREATE TABLE traffic_logs(
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    time TIME,
    ip_addr TEXT,
    user_email TEXT,
    endpoint TEXT
);

/* populate the user table with default admin user */
/* default admin is me, Darren, password is 'Admin' 
Also adding an Admin/Admin user to be intutitive*/
INSERT INTO users (surname, first_name, email, password, is_admin)
VALUES
    ('Counihan', 'Darren', 'darren@counihan.ie', 'scrypt:32768:8:1$Iu4xUOeqB0cOamG7$4a8efeb4991e1a50b23cb5dee9bc2b4a6e4d21aab938b01e14ebbe88a14d151240d77adb9f67730ba69f6f68f518b9bfa2750d015500d35dea652384b4efcaef'
    , TRUE);
INSERT INTO users (surname, first_name, email, password, is_admin)
VALUES
    ('Admin', 'Admin', 'Admin', 'scrypt:32768:8:1$Iu4xUOeqB0cOamG7$4a8efeb4991e1a50b23cb5dee9bc2b4a6e4d21aab938b01e14ebbe88a14d151240d77adb9f67730ba69f6f68f518b9bfa2750d015500d35dea652384b4efcaef'
    , TRUE);

/* adding default layperson to users. checking if is_admin defaults to false
password for derek@ucc.ie is 'derek' */
INSERT INTO users (surname, first_name, email, password)
VALUES
    ('Bridge', 'Derek', 'derek@ucc.ie', 'scrypt:32768:8:1$cKJFN8WjlzNPTjbD$c0c2e5d378889e8fd6aee36e1de6211c2bf1284c808cea525caa30e5174523a9b5e9627f06de86cd2cf88ab0d7c8a07c61a896d009a62f411a0e296afef860ac'
    );


select * from tasks;
select * from users;
select * from traffic_logs;


