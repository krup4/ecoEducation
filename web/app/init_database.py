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

INSERT INTO users (login, password, isOrganizer) VALUES
    ('Afghanistan','iudvb', TRUE),
    ('oivnoerv','fduivodfv', FALSE),
    ('osidnv','iusdvs',TRUE);

CREATE TABLE IF NOT EXISTS events (
    id SERIAL PRIMARY KEY,
    time TIMESTAMP,
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    name TEXT,
    cost INT,
    tags JSON,
    description TEXT,
    photo TEXT
);
CREATE TABLE IF NOT EXISTS qr_sessions (
    id SERIAL PRIMARY KEY,
    session uuid,
    event_id INT,
    FOREIGN KEY (event_id) REFERENCES events(id)
);
"""
