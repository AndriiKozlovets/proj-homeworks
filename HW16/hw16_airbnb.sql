-- 1. SQL queries for table creation for a data model

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
    FOREIGN KEY (guest_id) REFERENCES users(user_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    guest_id INT,
    host_id INT,
    room_id INT,
    rating INT,
    comment TEXT,
    review_comment TEXT,
    FOREIGN KEY (guest_id) REFERENCES users(user_id),
    FOREIGN KEY (host_id) REFERENCES users(user_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

-- 2. 3 rows (using INSERT queries) for each table in the data model

-- Add 3 users
INSERT INTO users (user_type, first_name, last_name, email)
VALUES 
    ('host', 'Andrii', 'Kozlovets', 'andrii.k@gmail.com'),
    ('host', 'Maksym', 'Havryliuk', 'maks.g@gmail.com'),
    ('guest', 'Vlad', 'Isniuk', 'vlad.i@gmail.com');

-- Add 3 rooms
INSERT INTO rooms (host_id, residents, price, ac, refrigerator)
VALUES 
    (1, 4, 100.00, TRUE, TRUE),
    (1, 2, 75.00, TRUE, FALSE),
    (2, 3, 120.00, TRUE, TRUE);

-- Add 3 reservations
INSERT INTO reservations (guest_id, room_id, check_in_date, check_out_date, paid)
VALUES 
    (3, 1, '2023-10-01', '2023-10-05', TRUE),
    (3, 2, '2023-10-10', '2023-10-15', TRUE),
    (1, 3, '2023-10-03', '2023-10-07', TRUE);

-- Add 3 reviews
INSERT INTO reviews (guest_id, host_id, room_id, rating, comment, review_comment)
VALUES 
    (3, 1, 1, 5, 'Great experience!', 'Thank you Andrii!'),
    (3, 1, 2, 4, 'Nice place, but could use a fridge.', 'Appreciate the feedback.'),
    (1, 2, 3, 5, 'Amazing host and property!', 'Thank you Maksym!');

-- 3.1. User who had the biggest amount of reservations

SELECT 
    u.user_id,
    CONCAT(u.first_name, ' ', u.last_name) AS user_name,
    COUNT(r.reservation_id) AS num_reservations
FROM users u
JOIN reservations r ON u.user_id = r.guest_id
GROUP BY u.user_id
ORDER BY num_reservations DESC
LIMIT 1;

-- 3.2. Host who earned the biggest amount of money for the last month

SELECT 
    u.user_id AS host_id,
    CONCAT(u.first_name, ' ', u.last_name) AS host_name,
    SUM(rm.price) AS earnings
FROM users u
JOIN rooms rm ON u.user_id = rm.host_id
JOIN reservations rs ON rm.room_id = rs.room_id
WHERE rs.check_in_date >= CURRENT_DATE - INTERVAL '1 month'
GROUP BY u.user_id
ORDER BY earnings DESC
LIMIT 1;

-- 3.3. Host with the best average rating

SELECT 
    u.user_id AS host_id,
    CONCAT(u.first_name, ' ', u.last_name) AS host_name,
    ROUND(AVG(rev.rating), 2) AS avg_rating
FROM users u
JOIN rooms rm ON u.user_id = rm.host_id
JOIN reviews rev ON rm.room_id = rev.room_id
GROUP BY u.user_id
ORDER BY avg_rating DESC
LIMIT 1;
