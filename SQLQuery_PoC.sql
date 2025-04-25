CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE sneakers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    brand VARCHAR(100),
    size FLOAT,
    color VARCHAR(50),
    category_id INT,
    price DECIMAL(10, 2),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);


INSERT INTO categories (name) VALUES ('Sports'), ('Casual'), ('Running');

INSERT INTO sneakers (name, brand, size, color, category_id, price) 
VALUES 
    ('Air Max 2024', 'Nike', 42, 'Black', 1, 120.00),
    ('Superstar', 'Adidas', 43, 'White', 2, 85.00),
    ('UltraBoost', 'Adidas', 44, 'Gray', 3, 180.00);


SELECT s.name, s.brand, s.size, s.color, s.price, c.name AS category
FROM sneakers s
JOIN categories c ON s.category_id = c.id
WHERE s.name LIKE '%Air%' OR s.brand LIKE '%Nike%' OR c.name LIKE '%Sports%';

INSERT INTO sneakers (name, brand, size, color, category_id, price) 
VALUES ('New Sneaker', 'Nike', 42, 'Red', 1, 150.00);
