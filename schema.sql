CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT NOT NULL,
    first_name TEXT,
    password TEXT NOT NULL
);

CREATE TABLE entry (
    id SERIAL PRIMARY KEY,
    data TEXT,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE entries (
    id SERIAL PRIMARY KEY,
    entry_text TEXT NOT NULL,
    user_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)

);


CREATE TABLE entry_notes (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL DEFAULT '',
    content TEXT NOT NULL,
    entry_id INTEGER,
    filename TEXT,
    user_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (entry_id) REFERENCES entry (id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users (id)
);


CREATE TABLE pictures_files (
    id SERIAL PRIMARY KEY,
    filename TEXT NOT NULL,
    file_data BYTEA NOT NULL,
    entry_note_id INTEGER,
    user_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (entry_note_id) REFERENCES entry_notes (id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
