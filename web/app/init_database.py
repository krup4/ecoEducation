command = """
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS events

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    OAuth INT,
    username TEXT,
    password TEXT,
    rating INT,
    uuid uuid
);

CREATE TABLE IF NOT EXISTS events (
    id SERIAL PRIMARY KEY,
    uuid uuid,
    time TIMESTAMP,
    adress TEXT,
    name TEXT,
    cost INT,
    tags JSON,
    description TEXT,
);

CREATE TABLE IF NOT EXISTS qr_sessions (
    id SERIAL PRIMARY KEY,
    session uuid,
    event_id INT,
    FOREIGN KEY (event_id) REFERENCES events(id)
);
"""
