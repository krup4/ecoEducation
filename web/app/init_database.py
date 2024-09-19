command = """
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS qr_sessions;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS organizers;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT,
    full_name TEXT,
    rating INT,
    uuid UUID
);

CREATE TABLE IF NOT EXISTS events (
    id SERIAL PRIMARY KEY,
    uuid UUID,
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

CREATE TABLE IF NOT EXISTS organizers (
    id SERIAL PRIMARY KEY,
    uuid UUID,
    login TEXT,
    password TEXT,
    name TEXT,
    proof TEXT,
    owned_events JSON
);
"""
