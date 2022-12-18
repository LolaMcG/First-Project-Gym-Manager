DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS exercises;
DROP TABLE IF EXISTS clients;


CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    address VARCHAR(255),
    phone_no int,
    gender VARCHAR(255),
    medi_cond VARCHAR(255)
);

CREATE TABLE exercises (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255),
    capacity int,
    instructor VARCHAR(255),
    time VARCHAR(255),
    location VARCHAR(255),
    client_id INT NOT NULL REFERENCES clients(id)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    client_id INT NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
    exercise_id INT NOT NULL REFERENCES exercises(id) ON DELETE CASCADE
);