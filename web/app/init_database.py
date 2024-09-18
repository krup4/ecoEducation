command = """
DROP TABLE IF EXISTS users;
<<<<<<< HEAD
DROP TABLE IF EXISTS events
DROP TABLE IF EXISTS qr_sessions;
=======
DROP TABLE IF EXISTS qr_sessions;
DROP TABLE IF EXISTS events;
>>>>>>> e23981ea22c925059d9bf5224d8a075a87fb27fb

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT,
    full_name TEXT,
    rating INT,
    uuid UUID
);

CREATE TABLE IF NOT EXISTS events (
<<<<<<< HEAD
    id SERIAL PRIMARY KEY,username
    uuid uuid,
=======
    id SERIAL PRIMARY KEY,
    uuid UUID,
>>>>>>> e23981ea22c925059d9bf5224d8a075a87fb27fb
    time TIMESTAMP,
    adress TEXT,
    name TEXT,
    cost INT,
    tags JSON,
    description TEXT
);

CREATE TABLE IF NOT EXISTS qr_sessions (
    id SERIAL PRIMARY KEY,
    session UUID,
    event_id INT,
    FOREIGN KEY (event_id) REFERENCES events(id)
);
"""
