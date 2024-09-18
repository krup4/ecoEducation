command = """
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    login TEXT,
    password TEXT,
    isOrganizer BOOLEAN
);

INSERT INTO users (login, password, isOrganizer) VALUES
    ('Afghanistan','iudvb', TRUE),
    ('oivnoerv','fduivodfv', FALSE),
    ('osidnv','iusdvs',TRUE);
"""
