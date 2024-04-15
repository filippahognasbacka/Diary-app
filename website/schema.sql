CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT NOT NULL,
    first_name TEXT,
    password TEXT NOT NULL

);

CREATE TABLE review (
    id INTEGER PRIMARY KEY,
    data TEXT
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES user (id)

);



