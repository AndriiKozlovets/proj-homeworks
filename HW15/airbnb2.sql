CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    user_type VARCHAR(10) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE rooms (
    room_id SERIAL PRIMARY KEY,
    host_id INT,
    residents INT,
    price DECIMAL(10, 2),
    ac BOOLEAN,
    refrigerator BOOLEAN,
    FOREIGN KEY (host_id) REFERENCES users(user_id)
);

CREATE TABLE reservations (
    reservation_id SERIAL PRIMARY KEY,
    guest_id INT,
    room_id INT,
    check_in_date DATE,
    check_out_date DATE,
    paid BOOLEAN,
    FOREIGN KEY (guest_id) REFERENCES users(user_id)
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    reservation_id INT,
    rating INT,
    comment TEXT,
    review_comment TEXT,
    FOREIGN KEY (reservation_id) REFERENCES reservations(reservation_id),
);

CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    reservation_id INT,
    amount DECIMAL(10, 2),
    FOREIGN KEY (reservation_id) REFERENCES reservations(reservation_id)
);

ALTER TABLE reservations
ADD COLUMN paid BOOLEAN DEFAULT FALSE;